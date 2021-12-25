import heapq

n2i = {
    'corridor': 0,
    'roomA': 1,
    'roomB': 2,
    'roomC': 3,
    'roomD': 4,
}

room_cor_pos = {'A': 2, 'B': 4, 'C': 6, 'D': 8}

energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

start_state_example = [
    ('',) * 11,  # 'corridor'
    ('B', 'A'),  # 'roomA'
    ('C', 'D'),  # 'roomB'
    ('B', 'C'),  # 'roomC'
    ('D', 'A'),  # 'roomD'
]

start_state_real = [
    ('',) * 11,  # 'corridor'
    ('C', 'B'),  # 'roomA'
    ('D', 'A'),  # 'roomB'
    ('D', 'B'),  # 'roomC'
    ('A', 'C'),  # 'roomD'
]

final_state = [
    ('',) * 11,  # 'corridor'
    ('A', 'A'),  # 'roomA'
    ('B', 'B'),  # 'roomB'
    ('C', 'C'),  # 'roomC'
    ('D', 'D'),  # 'roomD'
]


def copy_state(state):
    return [tuple(state[i]) for i in range(len(state))]


def find_path_from_room(room_type, room_name, target_corridor_pos, state, pod, changed_room, initial_steps):
    path_exist = True
    current_corridor = state[n2i['corridor']]
    corridor_pos = room_cor_pos[room_type]
    steps = initial_steps
    while path_exist and corridor_pos != target_corridor_pos:
        if current_corridor[corridor_pos]:
            path_exist = False
        corridor_pos += 1 if target_corridor_pos > corridor_pos else -1
        steps += 1

    cost = 0
    new_state = None
    if path_exist:
        lcor = list(current_corridor)
        lcor[target_corridor_pos] = pod
        new_corridor = tuple(lcor)
        new_state = copy_state(state)
        new_state[n2i['corridor']] = new_corridor
        new_state[n2i[room_name]] = changed_room
        cost = steps * energy[pod]

    return path_exist, cost, new_state


def find_path_from_corridor(init_cor_pos, pod, state, target_room_name, changed_room, initial_steps):
    current_corridor = state[n2i['corridor']]
    corridor_pos = init_cor_pos
    target_corridor_pos = room_cor_pos[pod]
    path_exist = True
    steps = initial_steps
    while path_exist and corridor_pos != target_corridor_pos:
        corridor_pos += 1 if target_corridor_pos > corridor_pos else -1
        steps += 1
        if current_corridor[corridor_pos]:
            path_exist = False

    cost = 0
    new_state = None
    if path_exist:
        lcor = list(current_corridor)
        lcor[init_cor_pos] = ''
        new_corridor = tuple(lcor)
        new_state = copy_state(state)
        new_state[n2i['corridor']] = new_corridor
        new_state[n2i[target_room_name]] = changed_room
        cost = steps * energy[pod]

    return path_exist, cost, new_state


def relax_path(state, new_state, cost, dists, bag):
    tnew_state = tuple(new_state)
    new_dist = dists[state] + cost
    if (tnew_state not in dists) or (new_dist < dists[tnew_state]):
        dists[tnew_state] = new_dist
        new_elem = (new_dist, tnew_state)
        state_idx = -1
        try:
            state_idx = [e[1] for e in bag].index(tnew_state)
            found = True
        except ValueError:
            found = False
        if found:
            elem = bag[state_idx]
            bag.remove(elem)
            heapq.heapify(bag)
        heapq.heappush(bag, new_elem)


def use_case(start_state):
    tstart_state = tuple(start_state)
    dists = {tstart_state: 0}
    bag = []
    heapq.heappush(bag, (0, tstart_state))
    # (prio, state) is an element of the heap

    possible_target_positions = [0, 1, 3, 5, 7, 9, 10]
    while len(bag) > 0:
        prio, state = heapq.heappop(bag)

        for room_type in ['A', 'B', 'C', 'D']:
            room_name = f'room{room_type}'
            room_idx = n2i[room_name]
            room_content = state[room_idx]
            if pod := room_content[0]:
                if pod != room_type or room_content[1] != room_type:
                    for target_corridor_pos in possible_target_positions:
                        path_exist, cost, new_state = find_path_from_room(room_type,
                                                                          room_name,
                                                                          target_corridor_pos,
                                                                          state,
                                                                          pod,
                                                                          changed_room=('', room_content[1]),
                                                                          initial_steps=1)
                        if path_exist:
                            relax_path(state, new_state, cost, dists, bag)
            elif pod := room_content[1]:
                if pod != room_type:
                    for target_corridor_pos in possible_target_positions:
                        path_exist, cost, new_state = find_path_from_room(room_type,
                                                                          room_name,
                                                                          target_corridor_pos,
                                                                          state,
                                                                          pod,
                                                                          changed_room=('', ''),
                                                                          initial_steps=2)
                        if path_exist:
                            relax_path(state, new_state, cost, dists, bag)

        current_corridor = state[n2i['corridor']]
        for init_cor_pos, pod in enumerate(current_corridor):
            if pod:
                target_room_name = f'room{pod}'
                target_room_idx = n2i[target_room_name]
                target_room_content = state[target_room_idx]

                if ('', '') == target_room_content:
                    path_exist, cost, new_state = find_path_from_corridor(init_cor_pos,
                                                                          pod,
                                                                          state,
                                                                          target_room_name,
                                                                          changed_room=('', pod),
                                                                          initial_steps=2)
                    if path_exist:
                        relax_path(state, new_state, cost, dists, bag)
                elif ('', pod) == target_room_content:
                    path_exist, cost, new_state = find_path_from_corridor(init_cor_pos,
                                                                          pod,
                                                                          state,
                                                                          target_room_name,
                                                                          changed_room=(pod, pod),
                                                                          initial_steps=1)
                    if path_exist:
                        relax_path(state, new_state, cost, dists, bag)

    tfinal_state = tuple(final_state)
    energy_final_state = dists[tfinal_state]
    return energy_final_state


def main():
    for start_state in [start_state_example, start_state_real]:
        print(use_case(start_state))


if __name__ == '__main__':
    main()

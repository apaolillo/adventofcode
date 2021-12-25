from collections import deque

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

NB_ROOMS = 4
start_state_example = [
    ('',) * 11,  # 'corridor'
    ('B', 'D', 'D', 'A'),  # 'roomA'
    ('C', 'C', 'B', 'D'),  # 'roomB'
    ('B', 'B', 'A', 'C'),  # 'roomC'
    ('D', 'A', 'C', 'A'),  # 'roomD'
]

start_state_real = [
    ('',) * 11,  # 'corridor'
    ('C', 'D', 'D', 'B'),  # 'roomA'
    ('D', 'C', 'B', 'A'),  # 'roomB'
    ('D', 'B', 'A', 'B'),  # 'roomC'
    ('A', 'A', 'C', 'C'),  # 'roomD'
]

# NB_ROOMS = 2
# start_state_example = [
#     ('',) * 11,  # 'corridor'
#     ('B', 'A'),  # 'roomA'
#     ('C', 'D'),  # 'roomB'
#     ('B', 'C'),  # 'roomC'
#     ('D', 'A'),  # 'roomD'
# ]
#
# start_state_real = [
#     ('',) * 11,  # 'corridor'
#     ('C', 'B'),  # 'roomA'
#     ('D', 'A'),  # 'roomB'
#     ('D', 'B'),  # 'roomC'
#     ('A', 'C'),  # 'roomD'
# ]

final_state = [
    ('',) * 11,  # 'corridor'
    ('A', 'A', 'A', 'A'),  # 'roomA'
    ('B', 'B', 'B', 'B'),  # 'roomB'
    ('C', 'C', 'C', 'C'),  # 'roomC'
    ('D', 'D', 'D', 'D'),  # 'roomD'
]

# final_state = [
#     ('',) * 11,  # 'corridor'
#     ('A', 'A'),  # 'roomA'
#     ('B', 'B'),  # 'roomB'
#     ('C', 'C'),  # 'roomC'
#     ('D', 'D'),  # 'roomD'
# ]

# final_state = [
#     ('', '', '', 'B', '', '', '', '', '', '', ''),  # 'corridor'
#     ('B', 'A'),  # 'roomA'
#     ('C', 'D'),  # 'roomB'
#     ('', 'C'),  # 'roomC'
#     ('D', 'A'),  # 'roomD'
# ]
# final_state = [
#     ('', '', '', 'B', '', '', '', '', '', '', ''),  # 'corridor'
#     ('B', 'A'),  # 'roomA'
#     ('', 'D'),  # 'roomB'
#     ('C', 'C'),  # 'roomC'
#     ('D', 'A'),  # 'roomD'
# ]

# MEMO = set()


def copy_state(state):
    return [tuple(state[i]) for i in range(len(state))]


def find_path_from_room(room_type, room_name, target_corridor_pos, state, pod, changed_room, initial_steps):
    path_exist = True
    current_corridor = state[n2i['corridor']]
    corridor_pos = room_cor_pos[room_type]
    steps = initial_steps
    if current_corridor[corridor_pos]:
        path_exist = False
    while path_exist and corridor_pos != target_corridor_pos:
        corridor_pos += 1 if target_corridor_pos > corridor_pos else -1
        steps += 1
        if current_corridor[corridor_pos]:
            path_exist = False

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


def relax_path(prio, new_state, cost, dists, bag, prev, state):
    tnew_state = tuple(new_state)
    new_dist = prio + cost
    if (tnew_state not in dists) or (new_dist < dists[tnew_state]):
        dists[tnew_state] = new_dist
        prev[tnew_state] = state
        new_elem = (new_dist, tnew_state)
        bag.append(new_elem)


def use_case(start_state):
    # MEMO.clear()
    tstart_state = tuple(start_state)
    dists = {tstart_state: 0}
    prev = {tstart_state: None}
    bag = deque()
    bag.append((0, tstart_state))
    # (prio, state) is an element of the heap

    possible_target_positions = [0, 1, 3, 5, 7, 9, 10]
    while len(bag) > 0:
        prio, state = bag.popleft()

        for room_type in ['A', 'B', 'C', 'D']:
            room_name = f'room{room_type}'
            room_idx = n2i[room_name]
            room_content = state[room_idx]
            nb_rooms = len(room_content)
            i = 0
            while i < nb_rooms and not room_content[i]:
                i += 1
            j = i + 1
            the_rest_are_at_home = True
            while the_rest_are_at_home and j < nb_rooms:
                if room_content[j] != room_type:
                    the_rest_are_at_home = False
                j += 1
            if i < nb_rooms:
                pod = room_content[i]
                if pod != room_type or not the_rest_are_at_home:
                    for target_corridor_pos in possible_target_positions:
                        lchanged_room = list(room_content)
                        lchanged_room[i] = ''
                        path_exist, cost, new_state = find_path_from_room(room_type,
                                                                          room_name,
                                                                          target_corridor_pos,
                                                                          state,
                                                                          pod,
                                                                          changed_room=tuple(lchanged_room),
                                                                          initial_steps=i+1)
                        if path_exist:
                            relax_path(prio, new_state, cost, dists, bag, prev, state)
            # elif pod := room_content[1]:
            #     if pod != room_type:
            #         for target_corridor_pos in possible_target_positions:
            #             path_exist, cost, new_state = find_path_from_room(room_type,
            #                                                               room_name,
            #                                                               target_corridor_pos,
            #                                                               state,
            #                                                               pod,
            #                                                               changed_room=('', ''),
            #                                                               initial_steps=2)
            #             if path_exist:
            #                 relax_path(state, new_state, cost, dists, bag)

        current_corridor = state[n2i['corridor']]
        for init_cor_pos, pod in enumerate(current_corridor):
            if pod:
                target_room_name = f'room{pod}'
                target_room_idx = n2i[target_room_name]
                target_room_content = state[target_room_idx]

                occupants = [occupant for occupant in target_room_content if occupant]
                occupants_at_home = [o == pod for o in occupants]
                can_go_to_room = all(occupants_at_home)
                nb_occupants = len(occupants)
                if can_go_to_room and nb_occupants < NB_ROOMS:
                    target_pos = NB_ROOMS - 1 - nb_occupants
                    lchanged_room = list(target_room_content)
                    lchanged_room[target_pos] = pod
                    path_exist, cost, new_state = find_path_from_corridor(init_cor_pos,
                                                                          pod,
                                                                          state,
                                                                          target_room_name,
                                                                          changed_room=tuple(lchanged_room),
                                                                          initial_steps=target_pos+1)
                    if path_exist:
                        relax_path(prio, new_state, cost, dists, bag, prev, state)
                # elif ('', pod) == target_room_content:
                #     path_exist, cost, new_state = find_path_from_corridor(init_cor_pos,
                #                                                           pod,
                #                                                           state,
                #                                                           target_room_name,
                #                                                           changed_room=(pod, pod),
                #                                                           initial_steps=1)
                #     if path_exist:
                #         relax_path(state, new_state, cost, dists, bag)

    tfinal_state = tuple(final_state)
    energy_final_state = dists[tfinal_state]
    p = prev[tfinal_state]
    pp = prev[p]
    ppp = prev[pp]
    return energy_final_state


def main():
    for start_state in [
        start_state_example,
        start_state_real,
    ]:
        print(use_case(start_state))


if __name__ == '__main__':
    main()

import heapq

start_state_example = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#  
  #########  """

start_state_real = """
#############
#...........#
###C#D#D#A###
  #B#A#B#C#  
  #########  """

final_state = """
#############
#...........#
###A#B#C#D###
  #A#B#C#D#  
  #########  """

energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}


def locate_pods(state):
    pods = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
    }

    for i, line in enumerate(state.splitlines()):
        for j, c in enumerate(line):
            if c in ['A', 'B', 'C', 'D']:
                pods[c].append((i, j))

    return pods


def lstate_copy(lstate):
    return [list(s) for s in lstate]


def lstate2state(lstate):
    return '\n'.join([''.join(e) for e in lstate])


def use_case(start_state):
    print(start_state)
    lstart_state = start_state.splitlines()
    nrows = len(lstart_state)
    ncols = len(lstart_state[0])
    # inf = float('inf')

    dists = {start_state: 0}
    bag = []
    heapq.heappush(bag, (0, start_state))
    # (prio, string) is an element of the heap
    while len(bag) > 0:
        prio, state = heapq.heappop(bag)
        lstate = state.splitlines()
        pods = locate_pods(state)
        for pod_type in pods:
            for pod in pods[pod_type]:
                i, j = pod
                for ii, jj in [
                    (i-1, j),
                    (i, j+1),
                    (i+1, j),
                    (i, j-1),
                ]:
                    if 0 <= ii < nrows and 0 <= jj < ncols:
                        c = lstate[ii][jj]
                        if '.' == c:
                            uv_cost = energy[pod_type]
                            new_lstate = lstate_copy(lstate)
                            new_lstate[ii][jj] = pod_type
                            new_lstate[i][j] = '.'
                            new_state = lstate2state(new_lstate)
                            new_dist = dists[state] + uv_cost
                            if (new_state not in dists) or (new_dist < dists[new_state]):
                                dists[new_state] = new_dist
                                new_elem = (new_dist, new_state)
                                state_idx = -1
                                try:
                                    state_idx = [e[1] for e in bag].index(state)
                                    found = True
                                except ValueError:
                                    found = False
                                if found:
                                    elem = bag[state_idx]
                                    bag.remove(elem)
                                    heapq.heapify(bag)
                                heapq.heappush(bag, new_elem)

    print()
    return 0


def main():
    use_case(start_state_example.lstrip())
    # use_case(start_state_real.lstrip())


if __name__ == '__main__':
    main()

from typing import List

deltas = {
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
}

rev_deltas = {v: k for k, v in deltas.items()}


def add(pos1, pos2):
    return [pos1[0]+pos2[0], pos1[1]+pos2[1]]


def diff(pos1, pos2):
    return [pos1[0]-pos2[0], pos1[1]-pos2[1]]


def dist(pos1, pos2):
    d = diff(pos1, pos2)
    r = (d[0]**2) + (d[1]**2)
    return r


def update_pos_i(i,
                 old_rope,
                 new_rope) -> List[int]:
    assert i > 0
    #new_pos_h
    #old_pos_h
    #old_pos_t
    delta_prev = diff(new_rope[i-1], old_rope[i-1])  # n-o=d => o+d=n
    di = dist(new_rope[i-1], old_rope[i])

    k = i
    while delta_prev[0] == delta_prev[1]:
        delta_prev = diff(new_rope[k - 1], old_rope[k - 1])
        k -= 1

        # t_delta = [0, -1 if delta[1] < 0 else 1]
        # new_pos_t = diff(new_pos_h, t_delta)
        # return new_pos_t

    if delta_prev[0] > delta_prev[1]:
        delta_cur = [-1 if delta_prev[0] < 0 else 1, 0]
    else:  # delta_prev[0] < delta_prev[1]
        delta_cur = [0, -1 if delta_prev[1] < 0 else 1]

    old_pos_i = new_rope[i-1]
    new_pos_i = diff(new_rope[i-1], delta_cur)
    new_rope[i] = new_pos_i

    print()



def dist1(p1, p2) -> bool:
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if p1 == [p2[0]+i, p2[1]+j]:
                return True
    return False


def print_map(rope):
    nrows = 25
    ncols = 30
    m = [['.' for j in range(ncols)] for i in range(nrows)]
    for i in range(len(rope)-1, -1, -1):
        m[rope[i][0]][rope[i][1]] = str(i)
    for line in m:
        print(''.join(line))
    print()


def main():
    filename = 'example.txt'
    # filename = 'example2.txt'
    # filename = 'input.txt'
    with open(filename, 'r') as f:
        moves = [(lambda dire, nb: (dire, int(nb)))(*line.strip().split())
                 for line in f.readlines()]

    all_pos_t = {(0, 0)}
    s = list((0, 0))
    rope = [list(s) for _ in range(10)]
    old_rope = [r for r in rope]
    print_map(rope)
    for move in moves:
        d, n = move
        di, dj = deltas[d]
        for k in range(n):
            old_rope[0] = list(rope[0])
            rope[0][0] += di
            rope[0][1] += dj

            for i in range(1, 10):
                old_rope[i] = list(rope[i])
                if rope[i-1] != rope[i] and not dist1(rope[i-1], rope[i]):
                    update_pos_i(i, old_rope, rope)
                # print_map(rope)

            print('(d,n,k)', d, n, k)
            print_map(rope)
            all_pos_t.add(tuple(rope[9]))
        print_map(rope)

    print(all_pos_t)
    print(len(all_pos_t))


if __name__ == '__main__':
    main()

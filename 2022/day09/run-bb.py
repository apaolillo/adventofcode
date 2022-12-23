from typing import List

deltas = {
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
}

rev_deltas = {v: k for k, v in deltas.items()}


def new_pos_t(pos_h,
              old_pos_h,
              old_pos_t,
              d) -> List[int]:
    dd = d
    if old_pos_h != pos_h:
        delta = (pos_h[0]-old_pos_h[0], pos_h[1]-old_pos_h[1])
        if delta[0] != 0 and delta[1] != 0:
            sigma = (-old_pos_h[0]+old_pos_t[0], -old_pos_h[1]+old_pos_t[1])
            sigma = (abs(old_pos_h[0]-pos_h[0]), abs(old_pos_h[1]-pos_h[1]))
            if sigma[0] > sigma[1]:
                sigma = [sigma[0], 0]
            else:
                sigma = [0, sigma[1]]
            # result = [pos_h[0] + sigma[0], pos_h[1] + sigma[1]]
            result = [pos_h[0] + sigma[0], pos_h[1] + sigma[1]]
            return result
        else:
            ddelta = (delta[0]//abs(delta[0]) if delta[0] else delta[0], delta[1]//abs(delta[1]) if delta[1] else delta[1])
            dd = rev_deltas[tuple(ddelta)]

    match dd:
        case 'R':
            return [pos_h[0], pos_h[1]-1]
        case 'U':
            return [pos_h[0]+1, pos_h[1]]
        case 'D':
            return [pos_h[0]-1, pos_h[1]]
        case 'L':
            return [pos_h[0], pos_h[1] + 1]
        case _:
            raise ValueError(f'unsupported dir: {d}')


def dist1(p1, p2) -> bool:
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if p1 == [p2[0]+i, p2[1]+j]:
                return True
    return False


def print_map(rope):
    return
    nrows = 100
    ncols = 100
    m = [['.' for j in range(ncols)] for i in range(nrows)]
    for i in range(len(rope)-1, -1, -1):
        m[rope[i][0]][rope[i][1]] = str(i)
    for line in m:
        print(''.join(line))
    print()


def main():
    filename = 'example.txt'
    filename = 'example2.txt'
    # filename = 'input.txt'
    with open(filename, 'r') as f:
        moves = [(lambda dire, nb: (dire, int(nb)))(*line.strip().split())
                 for line in f.readlines()]

    all_pos_t = {(0, 0)}
    s = list((0, 0))
    rope = [list(s) for _ in range(10)]
    old_rope = [r for r in rope]
    print_map(rope)
    for d, n in moves:
        di, dj = deltas[d]
        for k in range(n):
            old_rope[0] = list(rope[0])
            rope[0][0] += di
            rope[0][1] += dj

            for i in range(1, 10):
                if rope[i-1] != rope[i] and not dist1(rope[i-1], rope[i]):
                    old_rope[i] = list(rope[i])
                    rope[i] = new_pos_t(rope[i-1], old_rope[i-1], rope[i], d)
                print_map(rope)
            print_map(rope)

            all_pos_t.add(tuple(rope[9]))
        print_map(rope)

    print(all_pos_t)
    print(len(all_pos_t))


if __name__ == '__main__':
    main()

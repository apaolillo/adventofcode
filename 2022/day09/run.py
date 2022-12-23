from typing import List


def new_pos_t(pos_h, d) -> List[int]:
    match d:
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


def main():
    filename = 'example.txt'
    filename = 'input.txt'
    with open(filename, 'r') as f:
        moves = [(lambda dire, nb: (dire, int(nb)))(*line.strip().split())
                 for line in f.readlines()]

    deltas = {
        'R': (0, 1),
        'U': (-1, 0),
        'L': (0, -1),
        'D': (1, 0),
    }

    all_pos_t = {(0, 0)}
    s = list((0, 0))
    pos_h = list(s)
    pos_t = list(s)
    for d, n in moves:
        di, dj = deltas[d]
        for _ in range(n):
            pos_h[0] += di
            pos_h[1] += dj

            if pos_h != pos_t and not dist1(pos_h, pos_t):
                pos_t = new_pos_t(pos_h, d)
                all_pos_t.add(tuple(pos_t))
        print(d, n)

    print(all_pos_t)
    print(len(all_pos_t))


if __name__ == '__main__':
    main()

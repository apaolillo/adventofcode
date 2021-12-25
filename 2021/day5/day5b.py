import re

# INPUT_FILENAME = 'sample-input.txt'
INPUT_FILENAME = 'input.txt'


def main():
    lines = list()
    with open(INPUT_FILENAME, 'r') as ifile:
        for sline in ifile:
            m = re.match(r'\s*(?P<x1>\d+),(?P<y1>\d+)\s+->\s+(?P<x2>\d+),(?P<y2>\d+)',
                         sline.strip())
            if m is None:
                raise ValueError('Error parsing input.')
            gd = m.groupdict()
            p1 = (int(gd['x1']), int(gd['y1']))
            p2 = (int(gd['x2']), int(gd['y2']))
            line = (p1, p2)
            lines.append(line)
    points = sum([list(line) for line in lines], start=[])
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    max_x = max(xs)
    max_y = max(ys)
    board = [[0]*(max_y+1) for _ in range(0, max_x+1)]

    for line in lines:
        # print(line)
        p1, p2 = line
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            x = x1
            for y in range(min(y1, y2), max(y1, y2) + 1):
                board[x][y] += 1
        elif y1 == y2:
            y = y1
            for x in range(min(x1, x2), max(x1, x2) + 1):
                board[x][y] += 1
        else:
            pp1, pp2 = sorted([p1, p2])
            x_op = 1 if pp1[0] < pp2[0] else -1
            y_op = 1 if pp1[1] < pp2[1] else -1
            pp0 = (pp1[0], pp1[1])
            while pp0 != pp2:
                x, y = pp0
                board[x][y] += 1
                pp0 = (x + x_op, y + y_op)
            x, y = pp0
            board[x][y] += 1

    result = 0
    for x in range(0, max_x + 1, 1):
        for y in range(0, max_y + 1, 1):
            n = board[y][x]
            c = int(n) if n > 0 else '.'
            # print(c, end='')
            if n > 1:
                result += 1
        # print()
    print(f'result: {result}')


if __name__ == '__main__':
    main()

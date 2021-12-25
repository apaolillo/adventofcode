from __future__ import annotations

# from typing import Union
# from functools import reduce


def parse_range(srange):
    left, right = [int(e) for e in srange.split('=')[-1].split('..')]
    return left, right


def parse_line(line):
    line2 = line.strip()

    if line2.startswith('on '):
        line3 = line2[3:]
        light_on = True
    elif line2.startswith('off '):
        line3 = line2[4:]
        light_on = False
    else:
        raise ValueError('Unknown switch value')

    xr, yr, zr = [parse_range(srange) for srange in line3.split(',')]

    return light_on, xr, yr, zr


def is_small(c):
    _, xr, yr, zr = c
    x1, x2 = xr
    y1, y2 = yr
    z1, z2 = zr
    xb = -50 <= x1 <= 50 and -50 <= x2 <= 50
    yb = -50 <= y1 <= 50 and -50 <= y2 <= 50
    zb = -50 <= z1 <= 50 and -50 <= z2 <= 50
    result = all([xb, yb, zb])
    return result


def count_on(cube_ranges):
    S = set()

    for c in cube_ranges:
        turn_on, xr, yr, zr = c
        x1, x2 = xr
        y1, y2 = yr
        z1, z2 = zr

        if turn_on:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        S.add((x, y, z))
        else:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        if (x, y, z) in S:
                            S.remove((x, y, z))

    result = len(S)
    return result


def usecase(filename):
    with open(filename, 'r') as input_file:
        cube_ranges = [parse_line(line) for line in input_file]
    small_cube_ranges = [c for c in cube_ranges if is_small(c)]

    result = count_on(small_cube_ranges)
    print(f'result = {result}')


def main():
    usecase('sample-input.txt')
    usecase('input.txt')


if __name__ == '__main__':
    main()

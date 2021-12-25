from math import prod
from collections import deque


# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'


def get_low_points(hmap):
    nrows = len(hmap)
    ncols = len(hmap[0])
    lows = []
    for i in range(nrows):
        for j in range(ncols):
            current = hmap[i][j]
            coords = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            actual_coords = [(ii, jj)
                             for (ii, jj) in coords
                             if 0 <= ii < nrows and 0 <= jj < ncols]
            neighbours = [hmap[ii][jj] for (ii, jj) in actual_coords]
            points = sorted([current] + neighbours)
            if points[0] == current and points[1] > points[0]:
                lows.append((i,j))
    return lows


def basin_size(low_point, hmap):
    queue = deque()
    nrows = len(hmap)
    ncols = len(hmap[0])
    marked = [[False]*ncols for _ in range(nrows)]

    start = low_point
    queue.append(start)
    size = 0
    while len(queue) > 0:
        i, j = queue.popleft()
        marked[i][j] = True
        size += 1
        coords = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        actual_coords = [(ii, jj)
                         for (ii, jj) in coords
                         if 0 <= ii < nrows and 0 <= jj < ncols and hmap[ii][jj] < 9 and (not marked[ii][jj])]
        for p in actual_coords:
            ii, jj = p
            marked[ii][jj] = True
            queue.append(p)
    return size


def main():
    with open(_INPUT_FILENAME, 'r') as input_file:
        hmap = [[int(c) for c in line.strip()] for line in input_file]

    lows = get_low_points(hmap)
    basin_sizes = [basin_size(low_point=p, hmap=hmap) for p in lows]
    sorted_basin_sizes = sorted(basin_sizes, reverse=True)
    largest_basin_sizes = sorted_basin_sizes[:3]
    result = prod(largest_basin_sizes)

    print(result)


if __name__ == '__main__':
    main()

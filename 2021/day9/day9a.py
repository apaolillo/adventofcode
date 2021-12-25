
# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'


def main():
    with open(_INPUT_FILENAME, 'r') as input_file:
        hmap = [[int(c) for c in line.strip()] for line in input_file]
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
                lows.append(current)
    result = sum([e+1 for e in lows])
    print(result)


if __name__ == '__main__':
    main()

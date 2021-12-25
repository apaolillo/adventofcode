
# _INPUT_FILE_NAME = 'sample-input.txt'
_INPUT_FILE_NAME = 'input.txt'


def expand_matrix(src_matrix):
    nrows = len(src_matrix)
    ncols = len(src_matrix[0])
    dst_matrix = []
    for i in range(nrows * 5):
        if i - nrows < 0:
            line = []
            for j in range(ncols * 5):
                if j - ncols < 0:
                    line.append(src_matrix[i][j])
                else:
                    val = line[j - ncols] + 1
                    if val > 9:
                        val = 1
                    line.append(val)
            dst_matrix.append(line)
        else:
            new_line = [e + 1 if e < 9 else 1 for e in dst_matrix[i - nrows]]
            dst_matrix.append(new_line)

    return dst_matrix


def get_result(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    inf = float('inf')

    dists = [[inf] * ncols for _ in range(nrows)]
    dists[0][0] = 0

    start = (0, 0, 0)
    bag = [start]

    while len(bag) > 0:
        p = min(bag)
        bag.remove(p)

        d, i, j = p

        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < nrows and 0 <= jj < ncols:
                uv_cost = matrix[ii][jj]
                if dists[i][j] + uv_cost < dists[ii][jj]:
                    dists[ii][jj] = dists[i][j] + uv_cost
                    v = (ii, jj)
                    vv = (dists[ii][jj], ii, jj)
                    try:
                        vidx = [(p[1], p[2]) for p in bag].index(v)
                        bag[vidx] = vv
                    except ValueError:
                        bag.append(vv)

    return dists[nrows-1][ncols-1]


def main():
    with open(_INPUT_FILE_NAME, 'r') as input_file:
        matrix = [[int(e) for e in line.strip()] for line in input_file]
    # print(matrix)
    matrix2 = expand_matrix(matrix)
    result = get_result(matrix2)
    print(result)


if __name__ == '__main__':
    main()

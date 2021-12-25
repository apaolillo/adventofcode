from collections import deque

# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'

N = 100


def next_step(input_matrix):
    matrix = [[e for e in line] for line in input_matrix]

    nrows = len(matrix)
    ncols = len(matrix[0])
    queue = deque()

    nb_flashes = 0

    for i in range(nrows):
        for j in range(ncols):
            queue.append((i, j))
    while len(queue) > 0:
        i, j = queue.popleft()
        if matrix[i][j] < 10:
            matrix[i][j] += 1
            if matrix[i][j] == 10:
                nb_flashes += 1
                for ii, jj in [(i-1, j-1), (i-1, j), (i-1, j+1),
                               (i, j-1), (i, j+1), (i+1, j-1),
                               (i+1, j), (i+1, j+1)]:
                    if 0 <= ii < nrows and 0 <= jj < ncols:
                        queue.append((ii, jj))
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i][j] > 9:
                matrix[i][j] = 0

    return matrix, nb_flashes


def print_matrix(m):
    print('\n'.join([''.join([str(c) for c in line]) for line in m]))


def main():
    with open(_INPUT_FILENAME, 'r') as input_file:
        matrix = [[int(c) for c in line.strip()]
                  for line in input_file.readlines()]

    nrows = len(matrix)
    ncols = len(matrix[0])
    nelem = nrows * ncols

    i = 1
    while True:
        matrix, nb = next_step(matrix)
        if nb == nelem:
            break
        i += 1
    print(i)


if __name__ == '__main__':
    main()

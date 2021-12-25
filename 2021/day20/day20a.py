from __future__ import annotations

# from typing import Union
# from functools import reduce

# _INPUT_FILE_NAME = 'sample-input.txt'
_INPUT_FILE_NAME = 'input.txt'


def get_next(image, algo_string, border_char='.'):
    nrows = len(image)
    ncols = len(image[0])
    ext = 7
    nrows2 = nrows + ext + ext
    ncols2 = ncols + ext + ext
    edge = border_char * ext
    line_edge = border_char * ncols2
    image2_head = [list(line_edge) for _ in range(ext)]
    image2_body = [list(f'{edge}{line}{edge}') for line in image]
    image2_tail = [list(line_edge) for _ in range(ext)]
    image2 = image2_head + image2_body + image2_tail
    assert nrows2 == len(image2)
    assert ncols2 == len(image2[0])
    image3 = [[image2[i][j] for j in range(ncols2)] for i in range(nrows2)]

    def image2_get(iii, jjj):
        if 0 <= iii < nrows2 and 0 <= jjj < ncols2:
            return image2[iii][jjj]
        else:
            return border_char

    for i in range(nrows2):
        for j in range(ncols2):
            coords = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1), (i, j), (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1),
            ]
            rows_in_range = all([0 <= ii < nrows2 for ii, _ in coords])
            cols_in_range = all([0 <= jj < ncols2 for _, jj in coords])
            if rows_in_range and cols_in_range:
                convolution = [image2_get(ii, jj) for ii, jj in coords]
                bconvolution = ''.join(['1' if '#' == c else '0' for c in convolution])
                iconvolution = int(bconvolution, base=2)
                new_char = algo_string[iconvolution]
                image3[i][j] = new_char
    image4 = [''.join(line) for line in image3]
    border_char2 = algo_string[0b111111111] if '#' == border_char else algo_string[0]
    return image4, border_char2


def nb_lits(image):
    nrows = len(image)
    ncols = len(image[0])
    result = 0
    for i in range(nrows):
        for j in range(ncols):
            if '#' == image[i][j]:
                result += 1
    return result


def print_matrix(image):
    for line in image:
        print(line)
    print()


def usecase(filename):
    with open(filename, 'r') as input_file:
        algo_string = input_file.readline().strip()
        assert 512 == len(algo_string)
        empty = input_file.readline().strip()
        assert '' == empty
        image = [line.strip() for line in input_file]

    print_matrix(image)
    image2, bc2 = get_next(image, algo_string)
    print_matrix(image2)
    image3, bc3 = get_next(image2, algo_string, bc2)
    print_matrix(image3)
    result = nb_lits(image3)
    print(result)


def main():
    usecase('sample-input.txt')
    usecase('input.txt')


if __name__ == '__main__':
    main()

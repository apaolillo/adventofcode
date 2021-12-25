from __future__ import annotations

# from typing import Union
# from functools import reduce

# _INPUT_FILE_NAME = 'sample-input.txt'
from sys import stderr

_INPUT_FILE_NAME = 'input.txt'

def extend_image(image, ext=100):
    border_char = '.'
    nrows = len(image)
    ncols = len(image[0])
    nrows2 = nrows + ext + ext
    ncols2 = ncols + ext + ext
    edge = border_char * ext
    line_edge = border_char * ncols2
    image2_head = [list(line_edge) for _ in range(ext)]
    image2_body = [list(f'{edge}{line}{edge}') for line in image]
    image2_tail = [list(line_edge) for _ in range(ext)]
    image2 = image2_head + image2_body + image2_tail
    return image2


def image2_gett(iii, jjj, im, bc):
    if 0 <= iii < len(im) and 0 <= jjj < len(im[iii]):
        return im[iii][jjj]
    else:
        return bc


def get_next(src_image,
             dst_image,
             algo_string,
             border_char='.'):
    nrows = len(src_image)
    ncols = len(dst_image[0])
    nrows2 = nrows
    ncols2 = ncols



    for i in range(nrows2):
        for j in range(ncols2):
            coords = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1), (i, j), (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1),
            ]
            # rows_in_range = all([0 <= ii < nrows2 for ii, _ in coords])
            # cols_in_range = all([0 <= jj < ncols2 for _, jj in coords])
            if True:
                convolution = [image2_gett(ii, jj, src_image, border_char) for ii, jj in coords]
                bconvolution = ''.join(['1' if '#' == c else '0' for c in convolution])
                iconvolution = int(bconvolution, base=2)
                new_char = algo_string[iconvolution]
                dst_image[i][j] = new_char
    border_char2 = algo_string[0b111111111] if '#' == border_char else algo_string[0]
    return border_char2


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
        print(''.join(line))
    print(nb_lits(image))
    print()


def usecase(filename):
    with open(filename, 'r') as input_file:
        algo_string = input_file.readline().strip()
        assert 512 == len(algo_string)
        empty = input_file.readline().strip()
        assert '' == empty
        src_image = [line.strip() for line in input_file]

    # image = extend_image(src_image)
    next_src_image = extend_image(src_image, ext=100)
    next_dst_image = [['' for j in range(len(next_src_image[i]))] for i in range(len(next_src_image))]
    bc = '.'
    print_matrix(next_src_image)
    for i in range(50):
        bc = get_next(
            src_image=next_src_image,
            dst_image=next_dst_image,
            algo_string=algo_string,
            border_char=bc,
        )
        # print_matrix(next_dst_image)
        tmp = next_src_image
        next_src_image = next_dst_image
        next_dst_image = tmp
        print(i, file=stderr, flush=True)
    # print_matrix(image)
    print_matrix(next_src_image)
    # result = nb_lits(next_dst_image)
    # print(result)


def main():
    # usecase('sample-input.txt')
    usecase('input.txt')


if __name__ == '__main__':
    main()

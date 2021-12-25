
def print_board(board):
    nrows = len(board)
    for i in range(nrows):
        print(''.join(board[i]))
    print()


def next_step(board, board_tmp):
    nrows = len(board)
    ncols = len(board[0])

    moved = False

    # >
    for i in range(nrows):
        assert ncols == len(board[i])
        j = 0
        while j < ncols:
            board_tmp[i][j] = board[i][j]
            if '>' == board[i][j]:
                jj = (j+1) % ncols
                if '.' == board[i][jj]:
                    moved = True
                    board_tmp[i][jj] = '>'
                    board_tmp[i][j] = '.'
                    j += 1
            j += 1

    # v
    for j in range(ncols):
        i = 0
        while i < nrows:
            board[i][j] = board_tmp[i][j]
            if 'v' == board[i][j]:
                ii = (i+1) % nrows
                if '.' == board_tmp[ii][j]:
                    moved = True
                    board[ii][j] = 'v'
                    board[i][j] = '.'
                    i += 1
            i += 1

    return moved


def use_case(filename):
    with open(filename, 'r') as ifile:
        board1 = [list(line.strip()) for line in ifile]
    board2 = [[e for e in row] for row in board1]
    marks = [[False]*len(line) for line in board1]

    i = 1
    while moved := next_step(board=board1, board_tmp=board2):
        i += 1
    print(f'Result: {i}')


def main():
    use_case('sample-input.txt')
    use_case('input.txt')


if __name__ == '__main__':
    main()

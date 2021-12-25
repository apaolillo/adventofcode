
# INPUT_FILENAME = 'sample-input.txt'
INPUT_FILENAME = 'input.txt'


def get_data(input_filename):
    with open(input_filename, 'r') as input_file:
        file_content = input_file.read()
    file_lines = file_content.strip().splitlines()
    list_numbers = [int(e)
                    for e in file_lines[0].strip().split(',')]
    i = 1
    n = len(file_lines)
    boards = []
    while i < n:
        empty = file_lines[i]
        assert '' == empty
        i += 1
        board = []
        for _ in range(5):
            line = [int(e) for e in file_lines[i].split()]
            board.append(line)
            i += 1
        boards.append(board)

    return list_numbers, boards


def prepare_index(boards):
    index = dict()  # maps numbers to their position in boards
    for k in range(len(boards)):
        board = boards[k]
        for i in range(len(board)):
            line = board[i]
            assert len(line) == 5
            for j in range(5):
                n = line[j]
                if n not in index:
                    index[n] = []
                index[n].append((k, i, j))
    return index


def is_winning(crosses, i, j):
    line_checked = [crosses[ii][j] for ii in range(5)]
    col_checked = [crosses[i][jj] for jj in range(5)]
    return all(line_checked) or all(col_checked)


def compute_score(board, crosses, n):
    elements = [board[i][j] * (0 if crosses[i][j] else 1)
                for i in range(5)
                for j in range(5)]
    sum_board = sum(elements)
    result = sum_board * n
    return result


def play_game():
    list_numbers, boards = get_data(INPUT_FILENAME)
    crosses = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]
    index = prepare_index(boards)

    winners = []
    trigger_numbers = []

    for n in list_numbers:
        if n in index:
            for pos in index[n]:
                k, i, j = pos
                crosses[k][i][j] = True
                if is_winning(crosses[k], i, j):
                    if k not in winners:
                        winners.append(k)
                        trigger_numbers.append(n)
    last_winner = winners[-1]

    crosses = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]
    for n in list_numbers:
        if n in index:
            for pos in index[n]:
                k, i, j = pos
                crosses[k][i][j] = True
                if k == last_winner:
                    if is_winning(crosses[k], i, j):
                        return compute_score(boards[k], crosses[k], n)


def main():
    print(play_game())


if __name__ == '__main__':
    main()

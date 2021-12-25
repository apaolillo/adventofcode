
# _INPUT_FILE_NAME = 'sample-input.txt'
_INPUT_FILE_NAME = 'input.txt'


def init_paper(points):
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    nrows = max_y + 1
    ncols = max_x + 1
    paper = [[False]*ncols for _ in range(nrows)]

    for (x, y) in points:
        paper[y][x] = True

    return paper


def juxtapose(line0, line1):
    return [a or b for a, b in zip(line0, line1)]


def fold_it_x(paper, x):
    j = x
    new_paper = []
    for line in paper:
        lline = line[:j]
        rline = line[j+1:][::-1]

        if len(lline) > len(rline):
            for jj in range(len(rline)):
                lline[-1-jj] = lline[-1-jj] or rline[-1-jj]
            new_line = lline
        else:
            for jj in range(len(lline)):
                rline[-1 - jj] = rline[-1 - jj] or lline[-1 - jj]
            new_line = rline
        new_paper.append(new_line)
    return new_paper


def fold_it_y(paper, y):
    i = y
    nrows = len(paper)

    if nrows // 2 >= i:
        new_nrows = nrows - i - 1
        new_paper = []
        for ii in range(new_nrows):
            line = paper[nrows - 1 - ii]
            new_paper.append(list(line))
        for ii in range(i):
            new_paper[-1-ii] = juxtapose(new_paper[-1-ii], paper[i-1-ii])
    else:
        new_nrows = i
        new_paper = []
        for ii in range(new_nrows):
            line = paper[ii]
            new_paper.append(list(line))
        for ii in range(nrows - new_nrows - 1):
            new_paper[-1-ii] = juxtapose(new_paper[-1-ii],
                                         paper[i+1+ii])
    return new_paper


def fold_it(paper,
            axis,
            coord):
    if 'y' == axis:
        new_paper = fold_it_y(paper=paper, y=coord)
    elif 'x' == axis:
        new_paper = fold_it_x(paper=paper, x=coord)
    else:
        raise ValueError('Unknown axis')

    return new_paper

def print_paper(paper):
    for i in range(len(paper)):
        line = ''.join(['#' if paper[i][j] else '.' for j in range(len(paper[i]))])
        print(line)


def count_points(paper):
    return sum([paper[i][j]
                for i in range(len(paper))
                for j in range(len(paper[i]))])


def main():
    with open(_INPUT_FILE_NAME, 'r') as input_file:
        points = []
        while True:
            line = input_file.readline().strip()
            if line:
                ls = line.split(',')
                point = (int(ls[0]), int(ls[1]))
                points.append(point)
            else:
                break
        folds = []
        for line in input_file:
            fold_right = line.strip().split('fold along ')[1].split('=')
            axis = fold_right[0]
            coord = int(fold_right[1])
            folds.append((axis, coord))
    paper = init_paper(points)
    print_paper(paper)
    for axis, coord in folds:
        paper = fold_it(paper, axis, coord)
        print()
        print_paper(paper)
        print(count_points(paper))


if __name__ == '__main__':
    main()

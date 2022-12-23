import functools
import itertools
import math



def main():
    # filename = 'example.txt'
    filename = 'input.txt'

    with open(filename, 'r') as f:
        forest = [line.strip() for line in f.readlines()]

    # print(forest)
    # print(forest[0][1])
    # print(forest[1][0])

    nb_rows = len(forest)
    nb_cols = len(forest[0])

    nb_visibles = (2 * (nb_rows + nb_cols)) - 4
    # nb_visibles = 0
    for i in range(1, nb_rows-1):
        for j in range(1, nb_cols-1):
            current_tree = forest[i][j]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visible = True
            for ii, jj in directions:
                visible = True
                in_limits = True
                k = 1
                while visible and in_limits:
                    iii = i + (k * ii)
                    jjj = j + (k * jj)
                    if 0 <= iii < nb_rows and 0 <= jjj < nb_rows:
                        next_tree = forest[iii][jjj]
                        if next_tree >= current_tree:
                            visible = False
                    else:
                        in_limits = False
                    k += 1
                if visible:
                    break
            if visible:
                nb_visibles += 1
    print(nb_visibles)

    highest_score = 0
    for i in range(nb_rows):
        for j in range(nb_cols):
            current_tree = forest[i][j]

            directions = [
                (-1, 0),
                (0, -1),
                (0, 1),
                (1, 0),
            ]
            scores = []
            for ii, jj in directions:
                highest_tree = current_tree
                nb_visible_trees = 0
                visible = True
                in_limits = True
                k = 1
                while visible and in_limits:
                    iii = i + (k * ii)
                    jjj = j + (k * jj)
                    coord_next = (iii, jjj)
                    if 0 <= iii < nb_rows and 0 <= jjj < nb_rows:
                        next_tree = forest[iii][jjj]
                        if next_tree >= highest_tree:
                            highest_tree = next_tree
                            visible = False
                        nb_visible_trees += 1
                    else:
                        in_limits = False
                    k += 1
                scores.append(nb_visible_trees)
            current_score = functools.reduce(lambda x, y: x * y, scores)
            print(i, j, scores, current_score)

            if current_score > highest_score:
                highest_score = current_score
    print(highest_score)


if __name__ == '__main__':
    main()

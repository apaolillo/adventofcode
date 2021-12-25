
# _INPUT_FILE_NAME = 'sample-input1.txt'
# _INPUT_FILE_NAME = 'sample-input2.txt'
# _INPUT_FILE_NAME = 'sample-input3.txt'
_INPUT_FILE_NAME = 'input.txt'


def is_big(vertex):
    return vertex.isupper()


class PathFinder:
    def __init__(self, successors):
        self._succ = successors

    def count_paths(self):
        return self._nb_paths('start', 'end', set())

    def _nb_paths(self,
                  src,
                  dst,
                  visited):
        result = 0
        for next_v in self._succ[src]:
            if next_v == dst:
                result += 1
            elif is_big(next_v) or next_v not in visited:
                result += self._nb_paths(next_v, dst, visited | {src})
        return result


def main():
    with open(_INPUT_FILE_NAME, 'r') as input_file:
        edges = [tuple(line.strip().split('-')) for line in input_file]
    succ = dict()
    for e in edges:
        v1, v2 = e
        if v1 not in succ:
            succ[v1] = []
        succ[v1].append(v2)
        if v2 not in succ:
            succ[v2] = []
        succ[v2].append(v1)

    # print(edges)
    # print(succ)
    pf = PathFinder(successors=succ)
    result = pf.count_paths()
    print(result)


if __name__ == '__main__':
    main()

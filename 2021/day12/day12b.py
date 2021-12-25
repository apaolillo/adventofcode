
# _INPUT_FILE_NAME = 'sample-input1.txt'
# _INPUT_FILE_NAME = 'sample-input2.txt'
# _INPUT_FILE_NAME = 'sample-input3.txt'
_INPUT_FILE_NAME = 'input.txt'


def is_big(vertex):
    return vertex.isupper()


def is_small(vertex):
    return not is_big(vertex)


class PathFinder:
    def __init__(self, successors):
        self._succ = successors

    def count_paths(self):
        exceptions = [None] + [v
                               for v in self._succ
                               if v not in ['start', 'end'] and is_small(v)]
        paths = [self._count_paths_exception(exception_v=v)
                 for v in exceptions]
        return sum(paths)

    def _count_paths_exception(self,
                               exception_v):
        return self._nb_paths(
            src='start',
            dst='end',
            visits_available={v: 1 if v != exception_v else 2
                              for v in self._succ if is_small(v)},
            exception=exception_v,
        )

    def _nb_paths(self,
                  src,
                  dst,
                  visits_available,
                  exception=None):
        result = 0
        for next_v in self._succ[src]:
            if next_v == dst:
                if exception is None:
                    result += 1
                else:
                    if visits_available[exception] == 0 or (visits_available[exception] == 1 and src == exception):
                        result += 1  # otherwise it's already counted
            elif is_big(next_v) or visits_available[next_v] > 0:
                result += self._nb_paths(
                    src=next_v,
                    dst=dst,
                    visits_available={v: visits_available[v] - (1 if v == src else 0)
                                      for v in visits_available},
                    exception=exception,
                )
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

import itertools
from functools import lru_cache


a = [1, 1, 1, 1, 26, 1, 26, 1, 26, 26, 1, 26, 26, 26]
b = [14, 11, 12, 11, -10, 15, -14, 10, -4, -3, 13, -3, -9, -12]
c = [16, 3, 2, 7, 13, 6, 10, 11, 6, 5, 11, 4, 4, 6]


def run_s(start, end, input_string):
    inputs = tuple(map(int, list(input_string)))
    return run(start, end, inputs)


def run(start, end, input_tuple):
    w, x, y, z = 0, 0, 0, 0
    for i in range(start, end):
        w = input_tuple[i]
        x = z % 26
        z //= a[i]
        x += b[i]
        x = 1 if x != w else 0
        y = (25 * x) + 1
        z *= y
        z += (w + c[i]) * x
    return w, x, y, z


@lru_cache(maxsize=None)
def findtuple(i=0, z=0):
    if i == 14:
        return z == 0, ''

    paths = []
    for w in range(1, 10, 1):# range(9, -1, -1):
        x = z % 26
        z2 = z // a[i]
        x += b[i]
        x = 1 if x != w else 0
        y = (25 * x) + 1
        z2 *= y
        z2 += (w + c[i]) * x

        paths.append((z2, w))

    # sorted_paths = sorted(paths)
    paths_dec = [(z2, w) for z2, w in paths if z2 <= z]
    paths_inc = [(z2, w) for z2, w in paths if z2 > z]

    for z2, w in paths_dec + paths_inc:
        found, ws = findtuple(i+1, z2)
        if found:
            return True, str(w) + ws

    return False, ''


def inputs2str(inputs):
    return ''.join(map(str, inputs))


def main():
    mins = []
    possible_values = list(range(9, 0, -1))
    # possible_values = list(range(1, 10, 1))
    possible_values_vectors = [list(possible_values) for _ in range(7)]
    inputs = -1
    for inputs in itertools.product(*possible_values_vectors):
        w, x, y, z = run(0, len(inputs), inputs)
        i = inputs2str(inputs)
        # print(i, w, x, y, z)

        zelem = (z, int(i))
        if len(mins) < 10:
            mins.append(zelem)
        elif zelem < (zp := max(mins)):
            mins.remove(zp)
            mins.append(zelem)
            mins.sort()

        if z == 0:
            break
    print(mins)


def main2():
    print(run(0, 14, '99999999999999'))


def main3():
    possible_values = list(range(9, 0, -1))
    # possible_values = list(range(1, 10, 1))
    possible_values_vectors = [list(possible_values) for _ in range(14)]
    for inputs in itertools.product(*possible_values_vectors):
        w, x, y, z = run(0, len(inputs), inputs)
        i = inputs2str(inputs)

        if z == 0:
            print(i)
            break


def main4():
    w, x, y, z = run_s(0, 14, '06130800700804')
    print(w, x, y, z)
    print()
    found, ws = findtuple()
    print(found)
    print(ws)


if __name__ == '__main__':
    main4()

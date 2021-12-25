
from collections import Counter


# _INPUT_FILE_NAME = 'sample-input.txt'
_INPUT_FILE_NAME = 'input.txt'

# N = 10
N = 40


def get_count_from_string(string):
    result = dict()
    for i in range(len(string) - 1):
        key = string[i:i+2]
        if key not in result:
            result[key] = 0
        result[key] += 1
    return result


def get_count_from_count(counter, single_counter, rules):
    result = dict()
    for k in counter:
        new_c = rules[k]
        left = k[0] + new_c
        right = new_c + k[1]
        nb = counter[k]

        if left not in result:
            result[left] = 0
        result[left] += nb

        if right not in result:
            result[right] = 0
        result[right] += nb

        if new_c not in single_counter:
            single_counter[new_c] = 0
        single_counter[new_c] += nb

    return result, single_counter


def main():
    with open(_INPUT_FILE_NAME, 'r') as input_file:
        template = input_file.readline().strip()
        empty = input_file.readline().strip()
        assert '' == empty
        rules = dict([tuple(e.strip()
                            for e in line.strip().split('->'))
                      for line in input_file])
    counter = get_count_from_string(template)
    sc = dict(Counter(template))
    for i in range(N):
        counter, sc = get_count_from_count(counter, sc, rules)
    print(sc)

    result = max(sc.values()) - min(sc.values())
    print(result)


if __name__ == '__main__':
    main()

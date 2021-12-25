
from collections import Counter


_INPUT_FILE_NAME = 'sample-input.txt'
# _INPUT_FILE_NAME = 'input.txt'

N = 10
N = 40


def get_count_from_string(string, rules):
    result = dict()
    for i in range(len(string) - 1):
        key = string[i:i+2]
        val = rules[key]
        if val not in result:
            result[val] = 0
        result[val] += 1
    return result

def get_count_from_count(counter, rules):
    result = dict()
    for k in counter:
        nb = counter[k]
        rules[nb]


def get_next(src, rules):
    result = ''
    for i in range(len(src) - 1):
        key = src[i:i+2]
        val = rules[key]
        result += src[i] + val
    result += src[-1]
    return result


def main():
    with open(_INPUT_FILE_NAME, 'r') as input_file:
        template = input_file.readline().strip()
        empty = input_file.readline().strip()
        assert '' == empty
        rules = dict([tuple(e.strip()
                            for e in line.strip().split('->'))
                      for line in input_file])
    string = template
    print(string)
    counter = get_count_from_string(template, rules)
    for i in range(N):
        print(i, len(string))
        string = get_next(string, rules)
        c = Counter(string)
        print(c)
        # print(string)
    c = Counter(string)
    result = max(c.values()) - min(c.values())
    print(result)


if __name__ == '__main__':
    main()

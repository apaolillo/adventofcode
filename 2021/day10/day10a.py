
from collections import deque

# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'


def get_score(string):
    stack = deque()

    match_par = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    n = len(string)
    i = 0
    while i < n:
        if string[i] in ['(', '[', '{', '<']:
            stack.append(match_par[string[i]])
        elif string[i] in [')', ']', '}', '>']:
            if len(stack) > 0:
                e = stack.pop()
                if e != string[i]:  # corrupt, e is illegal
                    return score[string[i]]
            else:  # corrupt, no open match in stack
                return score[string[i]]
        i += 1

    return 0  # correct or incomplete


def main():
    with open(_INPUT_FILENAME, 'r') as input_file:
        scores = [get_score(line.strip()) for line in input_file]

    result = sum(scores)
    print(result)


if __name__ == '__main__':
    main()

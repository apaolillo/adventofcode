
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

    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
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
                    return 0
            else:  # corrupt, no open match in stack
                return 0
        i += 1

    # valid or incomplete starts here
    score = 0
    while len(stack) > 0:
        e = stack.pop()
        score *= 5
        score += score_map[e]

    return score


def main():
    with open(_INPUT_FILENAME, 'r') as input_file:
        scores = [get_score(line.strip()) for line in input_file]

    actual_scores = sorted([s for s in scores if s > 0])
    n = len(actual_scores)
    n2 = n // 2
    result = actual_scores[n2]
    print(result)


if __name__ == '__main__':
    main()

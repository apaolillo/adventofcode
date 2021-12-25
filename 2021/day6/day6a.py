
_INPUT_FILENAME = 'sample-input.txt'
# _INPUT_FILENAME = 'input.txt'


def steps(current_step):
    def dec(e):
        if e == 0:
            return 6
        else:
            return e - 1

    nb_new = len([i for i in current_step if i == 0])
    next_step = [dec(i) for i in current_step] + ([8] * nb_new)
    return next_step
    # nb_new = 0
    # for i in range(len(current_step)):
    #     if current_step[i] == 0:
    #         nb_new += 1
    #     current_step[i] = dec(current_step[i])
    # return current_step + [8] * nb_new


def main():
    with open(_INPUT_FILENAME, 'r') as ifile:
        fc = ifile.read().strip()
    init = [int(i) for i in fc.split(',')]
    current = init
    days = 80
    # days = 256
    for i in range(days+1):
        # current_s = ','.join([str(f) for f in current])
        # print(f'After {i} days: {current_s}')
        prev = current
        current = steps(current)
        print(i, len(prev))
    result = len(prev)
    print(f'result = {result}')


if __name__ == '__main__':
    main()

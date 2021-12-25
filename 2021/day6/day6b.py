
# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'


def main():
    with open(_INPUT_FILENAME, 'r') as ifile:
        fc = ifile.read().strip()
    init = [int(i) for i in fc.split(',')]
    # days = 80
    days = 256
    shifter = [0 for _ in range(9)]
    for i in init:
        shifter[i] += 1
    for n in range(1, days + 1):
        head = shifter[0]
        shifter = shifter[1:] + [head]
        shifter[6] += head
    result = sum(shifter)
    print(f'result = {result}')


if __name__ == '__main__':
    main()

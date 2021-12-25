
# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'


def main():
    result = 0
    with open(_INPUT_FILENAME, 'r') as input_file:
        for line in input_file:
            signals_s, number_s = line.strip().split('|')
            signals = signals_s.strip().split()
            digits = number_s.strip().split()

            lengths = [len(d) for d in digits if len(d) in [2, 3, 4, 7]]  # 7segment: 1, 7, 4, 8
            result += len(lengths)
    print(result)


if __name__ == '__main__':
    main()

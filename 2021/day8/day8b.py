
# _INPUT_FILENAME = 'sample-input.txt'
# _INPUT_FILENAME = 'sample-input2.txt'
_INPUT_FILENAME = 'input.txt'


def get_mapping(signals):
    mappings = dict()
    signals2 = [s for s in signals]

    mappings[1] = [s for s in signals if len(s) == 2][0]
    mappings[4] = [s for s in signals if len(s) == 4][0]
    mappings[7] = [s for s in signals if len(s) == 3][0]
    mappings[8] = [s for s in signals if len(s) == 7][0]

    signals2.remove(mappings[1])
    signals2.remove(mappings[4])
    signals2.remove(mappings[7])
    signals2.remove(mappings[8])

    mappings[3] = [s for s in signals2
                   if len(s) == 5 and all([c in s for c in mappings[1]])][0]
    signals2.remove(mappings[3])

    mappings[9] = [s for s in signals2
                   if len(s) == 6 and all([c in s for c in mappings[3]])][0]
    signals2.remove(mappings[9])

    mappings[5] = [s for s in signals2
                   if len(s) == 5 and all([c in mappings[9] for c in s])][0]
    signals2.remove(mappings[5])

    mappings[2] = [s for s in signals2
                   if len(s) == 5][0]
    signals2.remove(mappings[2])

    mappings[0] = [s for s in signals2
                   if len(s) == 6 and all([c in s for c in mappings[1]])][0]
    signals2.remove(mappings[0])

    mappings[6] = signals2[0]

    return mappings


def use_case(signals, digits):
    def sort_digits(d):
        return ''.join(sorted(d))

    mapping = get_mapping(signals)
    rev_mapping = {sort_digits(mapping[k]): k for k in mapping}
    actual_digits = [rev_mapping[sort_digits(d)] for d in digits]
    number = int(''.join([str(d) for d in actual_digits]))
    return number


def main():
    result = 0
    with open(_INPUT_FILENAME, 'r') as input_file:
        for line in input_file:
            signals_s, number_s = line.strip().split('|')
            signals = signals_s.strip().split()
            digits = number_s.strip().split()

            result += use_case(signals, digits)
    print(result)


if __name__ == '__main__':
    main()

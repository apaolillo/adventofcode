
# _INPUT_FILENAME = 'sample-input.txt'
_INPUT_FILENAME = 'input.txt'


def main():
    with open(_INPUT_FILENAME, 'r') as input_file:
        fc = input_file.read().strip()
    init_pos = [int(i) for i in fc.split(',')]
    min_pos = min(init_pos)
    max_pos = max(init_pos)

    def fuel(pos):
        costs = [abs(e-pos) for e in init_pos]
        new_costs = [(n*(n+1)) // 2 for n in costs]
        return sum(new_costs)

    pos_fuel = [(pos, fuel(pos)) for pos in range(min_pos, max_pos + 1)]
    sorted_pos_fuel = sorted(pos_fuel, key=lambda e: e[1])
    result = sorted_pos_fuel[0][1]
    print(result)


if __name__ == '__main__':
    main()

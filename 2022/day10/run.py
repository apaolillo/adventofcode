
if __name__ == '__main__':
    filename = 'example.txt'
    filename = 'input.txt'
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    x = 1
    cycles = 1
    max_cycle = 1+(len(lines)*2)
    interesting_cycles = list(range(20, max_cycle, 40))
    result = 0

    def add_result(current_cycle,
                   x):
        if current_cycle in interesting_cycles:
            result = x * current_cycle
        else:
            result = 0
        return result

    for line in lines:
        if line.startswith('noop'):
            cycles += 1
            result += add_result(cycles, x)
        elif line.startswith('addx '):
            _, val_s = line.split()
            val = int(val_s)

            cycles += 1
            result += add_result(cycles, x)

            x += val
            cycles += 1
            result += add_result(cycles, x)
        else:
            raise ValueError(f'unknown instruction: {line}')

    print(result)

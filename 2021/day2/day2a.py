
import sys
import numpy as np

if __name__ == '__main__':
    input_filename = str(sys.argv[1])
    with open(input_filename, 'r') as input_file:
        fc = input_file.read()

    split = fc.split()
    commands = split[::2]
    amounts = [int(e) for e in split[1::2]]
    position = np.asarray((0, 0, 0))  # (horiz, depth, aim)
    cmd_dict = {
        'down': lambda pos, amount: pos + np.asarray((0, 0, amount)),
        'up': lambda pos, amount: pos + np.asarray((0, 0, -amount)),
        'forward': lambda pos, amount: pos + np.asarray((amount, pos[2]*amount, 0)),
    }
    for c, a in zip(commands, amounts):
        position = cmd_dict[c](position, a)
    res = position[0] * position[1]
    print(res)

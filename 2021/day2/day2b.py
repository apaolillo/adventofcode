
import sys
import numpy as np

if __name__ == '__main__':
    input_filename = str(sys.argv[1])
    with open(input_filename, 'r') as input_file:
        fc = input_file.read()

    split = fc.split()
    commands = split[::2]
    amounts = [int(e) for e in split[1::2]]
    pos = np.asarray((0, 0))  # (horiz, depth)
    cmd_dict = {
        'forward': np.asarray((1, 0)),
        'up': np.asarray((0, -1)),
        'down': np.asarray((0, 1)),
    }
    for c, a in zip(commands, amounts):
        pos += a * cmd_dict[c]
    res = pos[0] * pos[1]
    print(res)


import sys
import numpy as np

if __name__ == '__main__':
    input_filename = str(sys.argv[1])
    with open(input_filename, 'r') as input_file:
        fc = input_file.read()
    depths = [int(e) for e in fc.split()]

    depths0 = np.asarray(depths[0:-2])
    depths1 = np.asarray(depths[1:-1])
    depths2 = np.asarray(depths[2:])

    depths = depths0 + depths1 + depths2

    depths1 = np.asarray(depths[:-1])
    depths2 = np.asarray(depths[1:])
    has_increased = [e > 0 for e in depths2-depths1]
    result = has_increased.count(True)

    str_increased = ['N/A - no previous measurement'] + ['increased' if e else 'decreased'
                                                         for e in has_increased]

    for nb, s in zip(depths, str_increased):
        print(f'{nb} ({s})')
    print(f'Result: {result}')


import sys
import numpy as np

if __name__ == '__main__':
    input_filename = str(sys.argv[1])
    with open(input_filename, 'r') as input_file:
        depths = [int(e) for e in input_file.read().split()]
        depths1 = np.asarray(depths[:-1])
        depths2 = np.asarray(depths[1:])
        has_increased = [e > 0 for e in depths2-depths1]
        result = has_increased.count(True)

    str_increased = ['N/A - no previous measurement'] + ['increased' if e else 'decreased'
                                                         for e in has_increased]

    for nb, s in zip(depths, str_increased):
        print(f'{nb} ({s})')
    print(f'Result: {result}')

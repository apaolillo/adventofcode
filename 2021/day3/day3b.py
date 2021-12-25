
def get_rate(numbers,
             is_o2):
    nb_bits = len(numbers[0])

    assert all([len(n) == nb_bits for n in numbers])

    current_numbers = [n for n in numbers]
    i = 0
    while len(current_numbers) > 1:
        nb_ones = sum([elem[i] == '1' for elem in current_numbers])
        nb_zeros = sum([elem[i] == '0' for elem in current_numbers])
        bit_o2 = '1' if nb_ones >= nb_zeros else '0'
        bit_co2 = '0' if nb_zeros <= nb_ones else '1'
        bit = bit_o2 if is_o2 else bit_co2
        current_numbers = [n for n in current_numbers if n[i] == bit]
        i += 1
    assert(1 == len(current_numbers))
    result = int(current_numbers[0], base=2)
    return result


def get_life_support(numbers):
    o2_rate = get_rate(numbers, is_o2=True)
    co2_rate = get_rate(numbers, is_o2=False)
    result = o2_rate * co2_rate
    return result


if __name__ == '__main__':
    input_filename = 'input.txt'
    # input_filename = 'sample-input.txt'
    with open(input_filename, 'r') as input_file:
        fc = input_file.read()
    split = fc.split()
    print(get_life_support(split))


def get_energy_consumption(split):
    nb_bits = len(split[0])

    assert all([len(n) == nb_bits for n in split])

    gamma = ''
    for i in range(nb_bits):
        nb_ones = sum([elem[i] == '1' for elem in split])
        nb_zeros = sum([elem[i] == '0' for elem in split])
        if nb_ones >= nb_zeros:
            gamma += '1'
        else:
            gamma += '0'
    epsilon = ''.join(['1' if b == '0' else '0' for b in gamma])
    gamma_i = int(gamma, base=2)
    epsilon_i = int(epsilon, base=2)
    consumption = gamma_i * epsilon_i
    return consumption


if __name__ == '__main__':
    input_filename = 'input.txt'
    with open(input_filename, 'r') as input_file:
        fc = input_file.read()
    splitted = fc.split()
    print(get_energy_consumption(splitted))

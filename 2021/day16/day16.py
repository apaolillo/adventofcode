from functools import reduce


class Parser:
    def __init__(self, bitstream):
        self._bitstream = bitstream

    def parse(self, i=0):
        version = int(self._bitstream[i:i+3], base=2)
        type_id = int(self._bitstream[i+3:i+6], base=2)
        if 4 == type_id:  # literal
            number_bits = []
            keep_reading = True
            ii = i+6
            while keep_reading:
                keep_reading = '1' == self._bitstream[ii]
                bits = self._bitstream[ii+1:ii+5]
                number_bits.append(bits)
                ii += 5
            # while ii % 4 != 0:
            #     ii += 1
            payload = int(''.join(number_bits), base=2)
            return {
                'version': version,
                'type_id': type_id,
                'literal': payload,
                '_i': ii,
            }
        else:  # operator
            length_type_id = int(self._bitstream[i+6], base=2)
            if 1 == length_type_id:
                nb_subpackets = int(self._bitstream[i + 7:i + 18], base=2)
                subpackets = []
                ii = i + 18
                for _ in range(nb_subpackets):
                    subpacket = self.parse(i=ii)
                    subpackets.append(subpacket)
                    ii = subpacket['_i']
                return {
                    'version': version,
                    'type_id': type_id,
                    'subpackets': subpackets,
                    '_i': ii,
                }
            else:  # 0, 15-bit number of bits in the subpackets
                subpackets_length = int(self._bitstream[i+7:i+22], base=2)
                subpackets = []
                ii = i + 22
                while ii < i+22+subpackets_length:
                    subpacket = self.parse(i=ii)
                    subpackets.append(subpacket)
                    ii = subpacket['_i']
                return {
                    'version': version,
                    'type_id': type_id,
                    'subpackets': subpackets,
                    '_i': ii,
                }


def sum_version_number(packet):
    result = packet['version']
    if 'subpackets' in packet:
        for subpacket in packet['subpackets']:
            result += sum_version_number(subpacket)
    return result


def bsum(values):
    return sum(values)


def bproduct(values):
    return reduce(lambda x, y: x*y, values)


def bmin(values):
    return min(values)


def bmax(values):
    return max(values)


def bgt(values):
    return 1 if values[0] > values[1] else 0


def blt(values):
    return 1 if values[0] < values[1] else 0


def beq(values):
    return 1 if values[0] == values[1] else 0


def value(packet):
    type_id = packet['type_id']
    if 4 == type_id:
        return packet['literal']
    else:
        subpackets = packet['subpackets']
        subvalues = [value(sp) for sp in subpackets]
        ops = {
            0: bsum,
            1: bproduct,
            2: bmin,
            3: bmax,
            5: bgt,
            6: blt,
            7: beq,
        }
        fun = ops[type_id]
        return fun(subvalues)


def use_case(hexstring):
    # nb = eval(f'0x{hexstring}')
    hex2bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    nb = ''.join([hex2bin[c] for c in hexstring])
    parser = Parser(nb)
    packet = parser.parse()
    result_version = sum_version_number(packet)
    result_value = value(packet)
    print(result_version, result_value)


def use_file(filename):
    with open(filename, 'r') as input_file:
        fc = input_file.read().strip()
    return use_case(fc)


def main():
    use_file('sample-input1.txt')
    use_case('38006F45291200')
    use_case('EE00D40C823060')
    use_case('8A004A801A8002F478')
    use_case('620080001611562C8802118E34')
    use_case('C0015000016115A2E0802F182340')
    use_case('A0016C880162017C3686B18A3D4780')
    use_file('input.txt')


if __name__ == '__main__':
    main()

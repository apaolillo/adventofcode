

def parse_range(srange):
    left, right = [int(e) for e in srange.split('=')[-1].split('..')]
    return left, right


def parse_line(line):
    line2 = line.strip()

    if line2.startswith('on '):
        line3 = line2[3:]
        light_on = True
    elif line2.startswith('off '):
        line3 = line2[4:]
        light_on = False
    else:
        raise ValueError('Unknown switch value')

    xr, yr, zr = [parse_range(srange) for srange in line3.split(',')]

    return light_on, xr, yr, zr


def intersect_interval(I1, I2):
    intervals = sorted([I1, I2])
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    return b1 >= a2


def intersect_cubes(ci, cj):
    _, xir, yir, zir = ci
    xi1, xi2 = xir
    yi1, yi2 = yir
    zi1, zi2 = zir

    _, xjr, yjr, zjr = cj
    xj1, xj2 = xjr
    yj1, yj2 = yjr
    zj1, zj2 = zjr

    inter_x = intersect_interval((xi1, xi2), (xj1, xj2))
    inter_y = intersect_interval((yi1, yi2), (yj1, yj2))
    inter_z = intersect_interval((zi1, zi2), (zj1, zj2))

    return all([inter_x, inter_y, inter_z])


def get_gross_lights(cube):
    _, xr, yr, zr = cube
    x1, x2 = xr
    xl = x2 - x1 + 1
    y1, y2 = yr
    yl = y2 - y1 + 1
    z1, z2 = zr
    zl = z2 - z1 + 1
    return xl * yl * zl


def intersected_interval(I1, I2):
    intervals = sorted([I1, I2])
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    return a2, min(b1, b2)


def intersected_cube(ci, cj):
    if not intersect_cubes(ci, cj):
        return False, 0
    else:
        _, xir, yir, zir = ci
        xi1, xi2 = xir
        yi1, yi2 = yir
        zi1, zi2 = zir

        _, xjr, yjr, zjr = cj
        xj1, xj2 = xjr
        yj1, yj2 = yjr
        zj1, zj2 = zjr

        inter_x = intersected_interval((xi1, xi2), (xj1, xj2))
        inter_y = intersected_interval((yi1, yi2), (yj1, yj2))
        inter_z = intersected_interval((zi1, zi2), (zj1, zj2))

        res_c = True, inter_x, inter_y, inter_z
        return True, res_c


def get_net_lights(i, cubes):
    current_cube = cubes[i]
    future_cubes = cubes[i + 1:]
    inter_cubes_results = [intersected_cube(current_cube, future_cube)
                           for future_cube in future_cubes]
    inter_cubes = [c for b, c in inter_cubes_results if b]
    inter_cubes_net_lights = [get_net_lights(j, inter_cubes) for j in range(len(inter_cubes))]
    sum_icnl = sum(inter_cubes_net_lights)
    result = get_gross_lights(current_cube) - sum_icnl
    return result


def usecase2(filename):
    with open(filename, 'r') as input_file:
        cubes = [parse_line(line) for line in input_file]

    C = len(cubes)
    all_net_lights = [get_net_lights(i, cubes) for i in range(C) if cubes[i][0]]
    result = sum(all_net_lights)
    print(f'result = {result}')


def main():
    usecase2('sample-input2.txt')
    usecase2('input.txt')


if __name__ == '__main__':
    main()

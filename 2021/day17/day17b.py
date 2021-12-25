
target_x_min = 128
target_x_max = 160
target_y_min = -142
target_y_max = -88

# target_x_min = 20
# target_x_max = 30
# target_y_min = -10
# target_y_max = -5


def step(x_pos, y_pos, x_vel, y_vel):
    x_pos += x_vel
    if x_vel != 0:
        x_vel += -1 if x_vel > 0 else 1
    y_pos += y_vel
    y_vel -= 1

    return x_pos, y_pos, x_vel, y_vel


def in_target(x_pos, y_pos):
    is_x = target_x_min <= x_pos <= target_x_max
    is_y = target_y_min <= y_pos <= target_y_max
    return is_x and is_y


def too_deep(y_pos):
    return y_pos < target_y_min


def too_far(x_pos):
    return x_pos > target_x_max


def fire(x_vel, y_vel):
    x_pos, y_pos = 0, 0
    y_pos_max = 0
    while True:
        x_pos, y_pos, x_vel, y_vel = step(x_pos, y_pos, x_vel, y_vel)
        y_pos_max = y_pos if y_pos > y_pos_max else y_pos_max

        if in_target(x_pos, y_pos):
            return y_pos_max, True, False, False
        td = too_deep(y_pos)
        tf = too_far(x_pos)
        if td or tf:
            return y_pos_max, False, tf, td


def search():
    the_max = (0, 0, 1)
    x_bound = target_x_max + 1
    x_bound = 2*(target_x_max + 1)
    for x in range(-x_bound, x_bound):
        y = -1000

        max_y, reached, is_too_far, is_too_deep = fire(x, y)
        stop = is_too_far or is_too_deep
        if reached:
            if max_y > the_max[0]:
                the_max = (max_y, x, y)
        while not stop:
            y += 1
            max_y, reached, is_too_far, is_too_deep = fire(x, y)
            stop = y < 1000  # is_too_far or is_too_deep
            if reached:
                if max_y >= the_max[0]:
                    the_max = (max_y, x, y)
    return the_max


def search2():
    mib = -1000
    mab = 1000
    solutions = []
    for x in range(0, 2*(target_x_max + 1)):
        for y in range(mib, mab):
            max_y, reached, is_too_far, is_too_deep = fire(x, y)
            if reached:
                solutions.append((max_y, x, y))
                print(f'\t{x},{y},{max_y}')
    return solutions



def search3():
    kept_max_y = -1
    x_res = 0
    y_res = 0
    for x in range(0, 2*(target_x_max + 1)):
        y = -100
        previous_max_y = kept_max_y
        stop = False
        while not stop:
            max_y, reached, is_too_far, is_too_deep = fire(x, y)
            while not (is_too_far or is_too_deep):
                y += 1
                max_y, reached, is_too_far, is_too_deep = fire(x, y)
                if reached:
                    if max_y > kept_max_y:
                        print(x,)
                        kept_max_y = max_y
                        x_res = x
                        y_res = y
            if kept_max_y > previous_max_y:
                stop = False
                previous_max_y = kept_max_y
            else:
                stop = True
    return kept_max_y, x_res, y_res


def search4():
    y = target_y_min - 1
    nb = 0
    while True:
        for x in range(0, 2*(target_x_max + 1)):
            max_y, reached, is_too_far, is_too_deep = fire(x, y)
            if reached:
                nb += 1
        print(nb)
        y += 1

def main():
    print(fire(7, 2))
    print(fire(17, -4))
    print(fire(6, 9))
    # print(search())
    # print(search2())
    print(search4())


if __name__ == '__main__':
    main()

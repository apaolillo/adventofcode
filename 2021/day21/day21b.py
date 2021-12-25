
import itertools

# p1start = 4
# p2start = 8
p1start = 4
p2start = 2

RESULTS = dict()


def g(s1, s2, p1, p2, turn_p1):
    if (s1, s2, p1, p2, turn_p1) in RESULTS:
        return RESULTS[(s1, s2, p1, p2, turn_p1)]

    possible_rolls = [1, 2, 3]
    res_p1 = 0
    res_p2 = 0
    if turn_p1:
        for rolls3 in itertools.product(possible_rolls, possible_rolls, possible_rolls):
            roll = sum(rolls3)
            new_p1 = (p1 + roll) % 10
            new_s1 = s1 + new_p1 + 1
            if new_s1 >= 21:
                res_p1 += 1
            else:
                r1, r2 = g(new_s1, s2, new_p1, p2, False)
                res_p1 += r1
                res_p2 += r2
    else:
        for rolls3 in itertools.product(possible_rolls, possible_rolls, possible_rolls):
            roll = sum(rolls3)
            new_p2 = (p2 + roll) % 10
            new_s2 = s2 + new_p2 + 1
            if new_s2 >= 21:
                res_p2 += 1
            else:
                r1, r2 = g(s1, new_s2, p1, new_p2, True)
                res_p1 += r1
                res_p2 += r2

    RESULTS[(s1, s2, p1, p2, turn_p1)] = res_p1, res_p1
    return res_p1, res_p1


def main():
    result = g(
        s1=0,
        s2=0,
        p1=p1start-1,
        p2=p2start-1,
        turn_p1=True,
    )
    print(result)


if __name__ == '__main__':
    main()

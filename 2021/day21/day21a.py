
# p1start = 4
# p2start = 8
p1start = 4
p2start = 2


def main():
    p1pos = p1start - 1
    p2pos = p2start - 1
    k = 0
    i = 0
    s1 = 0
    s2 = 0
    turn_p1 = True
    while s1 < 1000 and s2 < 1000:
        shift = 0
        k += 3
        for _ in range(3):
            shift += i+1
            i += 1
            i %= 100
        if turn_p1:
            p1pos += shift
            p1pos %= 10
            s1 += p1pos + 1
            turn_p1 = False
            print(f'P1 rolls {shift}, moves to {p1pos+1} and score {s1}')
        else:
            p2pos += shift
            p2pos %= 10
            s2 += p2pos + 1
            turn_p1 = True
            print(f'P2 rolls {shift}, moves to {p2pos + 1} and score {s2}')
    result = min(s1, s2) * k
    print(result)


if __name__ == '__main__':
    main()

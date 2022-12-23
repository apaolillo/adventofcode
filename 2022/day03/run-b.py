with open("input.txt") as f:
    # with open('ex.txt') as f:
    fc = f.read()


def prio(e):
    if e.islower():
        prio = ord(e) - ord("a") + 1
    else:
        prio = ord(e) - ord("A") + 27
    return prio


def go(usecase):
    n = len(usecase)
    b1 = usecase[: n // 2]
    b2 = usecase[n // 2 :]
    elems = list(set([e for e in b1 if e in b2]))
    assert len(elems) == 1
    # assert len(elems) == 2 and elems[0] == elems[1]
    return prio(elems[0])


usecases = [uc.strip() for uc in fc.splitlines()]
sols = [go(u) for u in usecases]
print(sols)
print(sum(sols))


def common(pack3):
    a, b, c = pack3
    badges = list(set([e for e in a if e in b and e in c]))
    assert len(badges) == 1
    return prio(badges[0])


groupsof3 = [usecases[i : i + 3] for i in range(0, len(usecases), 3)]
solsb = [common(g) for g in groupsof3]
print(solsb)
print(sum(solsb))

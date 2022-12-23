with open("input.txt") as f:
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

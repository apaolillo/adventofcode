# with open('example.txt') as f:
with open("input.txt") as f:
    fc = f.read()
print(fc)


def gr0(rs):
    a, b = [int(e) for e in rs.split("-")]
    return range(a, b + 1)


def gr(line):
    g1, g2 = line.strip().split(",")
    res1 = gr0(g1)
    res2 = gr0(g2)
    return res1, res2


def isin(subr, overr):
    a = subr.start in overr
    b = (subr.stop - 1) in overr
    return a and b


def getsol(range1, range2):
    return isin(range1, range2) or isin(range2, range1)


if __name__ == "__main__":
    grs = [gr(l) for l in fc.splitlines()]
    sols = [getsol(r1, r2) for r1, r2 in grs]
    print(sols)
    print(sum(sols))

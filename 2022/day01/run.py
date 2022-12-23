def themax(e):
    return sum(map(lambda x: int(x.strip()), e.splitlines()))


if __name__ == "__main__":
    fc = open("input.txt").read().strip().split("\n\n")
    fcl = [themax(e) for e in fc]
    # print(max(fcl))

    print(sum(sorted(fcl)[-3:]))

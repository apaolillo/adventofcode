p1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# A, X rock
# B, Y paper
# C, Z scissor


def score(him, you):
    score = p1[you]
    match you:
        case "X":
            match him:
                case "A":
                    score += 3
                case "B":
                    score += 0
                case "C":
                    score += 6
        case "Y":
            match him:
                case "A":
                    score += 6
                case "B":
                    score += 3
                case "C":
                    score += 0
        case "Z":
            match him:
                case "A":
                    score += 0
                case "B":
                    score += 6
                case "C":
                    score += 3
    return score


with open("input.txt") as f:
    rounds = [l.split() for l in f.readlines()]

print(rounds)
print(sum([score(a, b) for a, b in rounds]))

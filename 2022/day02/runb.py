p1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# A rock
# B paper
# C scissor

# X lose
# Y draw
# Z win


def score(him, req):
    score = 0
    match req:
        case "Z":  # win
            score += 6
            match him:
                case "A":
                    score += 2
                case "B":
                    score += 3
                case "C":
                    score += 1
        case "Y":  # draw
            score += 3
            match him:
                case "A":
                    score += 1
                case "B":
                    score += 2
                case "C":
                    score += 3
        case "X":  # lose
            score += 0
            match him:
                case "A":
                    score += 3
                case "B":
                    score += 1
                case "C":
                    score += 2
    return score


with open("input.txt") as f:
    # with open('ex.txt') as f:
    rounds = [l.split() for l in f.readlines()]

print(rounds)
scores = [score(a, b) for a, b in rounds]
print(scores)
print(sum(scores))

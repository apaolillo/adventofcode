"""
    [D]
[N] [C]
[Z] [M] [P]
"""

stacks = [
    ["N", "Z"],
    ["D", "C", "M"],
    ["P"],
]

instr = [
    (1, 2, 1),
    (3, 1, 3),
    (2, 2, 1),
    (1, 1, 2),
]

stacks = [
    [
        "J",
        "F",
        "C",
        "N",
        "D",
        "B",
        "W",
    ],
    [
        "T",
        "S",
        "L",
        "Q",
        "V",
        "Z",
        "P",
    ],
    [
        "T",
        "J",
        "G",
        "B",
        "Z",
        "P",
    ],
    [
        "C",
        "H",
        "B",
        "Z",
        "J",
        "L",
        "T",
        "D",
    ],
    [
        "S",
        "J",
        "B",
        "V",
        "G",
    ],
    [
        "Q",
        "S",
        "P",
    ],
    [
        "N",
        "P",
        "M",
        "L",
        "F",
        "D",
        "V",
        "B",
    ],
    [
        "R",
        "L",
        "D",
        "B",
        "F",
        "M",
        "S",
        "P",
    ],
    [
        "R",
        "T",
        "D",
        "V",
    ],
]

instr = [
    (4, 9, 6),
    (7, 2, 5),
    (3, 5, 2),
    (2, 2, 1),
    (2, 8, 4),
    (1, 6, 9),
    (1, 9, 4),
    (7, 1, 2),
    (5, 2, 3),
    (5, 7, 4),
    (5, 6, 3),
    (1, 7, 6),
    (2, 6, 9),
    (3, 2, 4),
    (4, 5, 6),
    (2, 7, 3),
    (2, 9, 3),
    (1, 5, 2),
    (11, 4, 3),
    (1, 2, 9),
    (1, 9, 3),
    (2, 1, 6),
    (5, 8, 5),
    (7, 5, 4),
    (2, 5, 6),
    (6, 6, 4),
    (17, 3, 4),
    (1, 8, 3),
    (11, 4, 7),
    (1, 6, 4),
    (3, 4, 2),
    (2, 2, 6),
    (8, 3, 1),
    (8, 3, 9),
    (3, 9, 6),
    (3, 1, 3),
    (11, 7, 5),
    (1, 6, 4),
    (4, 9, 6),
    (3, 1, 4),
    (1, 2, 3),
    (1, 6, 9),
    (24, 4, 9),
    (2, 6, 5),
    (1, 1, 2),
    (1, 1, 3),
    (12, 9, 6),
    (5, 4, 2),
    (4, 2, 3),
    (5, 6, 3),
    (13, 6, 7),
    (1, 5, 6),
    (9, 5, 3),
    (4, 7, 5),
    (1, 6, 1),
    (3, 5, 1),
    (14, 9, 4),
    (2, 7, 9),
    (13, 4, 9),
    (1, 4, 7),
    (4, 7, 9),
    (3, 5, 1),
    (8, 3, 9),
    (4, 1, 4),
    (8, 3, 7),
    (3, 7, 6),
    (4, 4, 2),
    (3, 1, 9),
    (6, 2, 6),
    (3, 3, 1),
    (7, 9, 7),
    (2, 6, 5),
    (1, 5, 3),
    (3, 7, 5),
    (5, 7, 4),
    (2, 1, 4),
    (5, 5, 9),
    (6, 4, 1),
    (6, 7, 8),
    (22, 9, 3),
    (7, 1, 8),
    (4, 9, 6),
    (1, 4, 5),
    (8, 6, 4),
    (7, 8, 1),
    (1, 6, 4),
    (1, 9, 4),
    (1, 1, 2),
    (1, 2, 5),
    (1, 9, 8),
    (11, 3, 7),
    (1, 6, 2),
    (2, 1, 5),
    (1, 8, 2),
    (1, 7, 8),
    (4, 5, 7),
    (1, 6, 9),
    (6, 3, 1),
    (6, 3, 1),
    (15, 7, 5),
    (1, 3, 1),
    (1, 3, 6),
    (1, 6, 8),
    (14, 5, 1),
    (16, 1, 3),
    (2, 8, 9),
    (1, 7, 4),
    (3, 9, 8),
    (3, 8, 7),
    (2, 3, 5),
    (1, 7, 1),
    (6, 8, 5),
    (2, 2, 9),
    (1, 7, 2),
    (2, 9, 2),
    (5, 4, 7),
    (3, 2, 7),
    (14, 1, 5),
    (2, 4, 7),
    (8, 7, 6),
    (1, 1, 5),
    (1, 7, 4),
    (1, 7, 5),
    (1, 1, 8),
    (12, 3, 4),
    (1, 8, 7),
    (3, 4, 1),
    (1, 6, 2),
    (8, 5, 2),
    (1, 7, 6),
    (1, 1, 7),
    (6, 6, 2),
    (1, 1, 2),
    (14, 5, 7),
    (1, 6, 4),
    (4, 4, 7),
    (1, 1, 6),
    (1, 5, 6),
    (2, 3, 1),
    (14, 7, 5),
    (10, 4, 7),
    (1, 1, 9),
    (1, 5, 9),
    (11, 5, 1),
    (6, 7, 6),
    (1, 4, 6),
    (1, 3, 7),
    (2, 1, 5),
    (13, 2, 1),
    (10, 6, 7),
    (4, 5, 2),
    (1, 9, 1),
    (1, 3, 6),
    (2, 5, 2),
    (1, 9, 3),
    (1, 3, 1),
    (21, 7, 5),
    (1, 6, 4),
    (4, 5, 1),
    (1, 4, 1),
    (6, 2, 3),
    (1, 3, 6),
    (1, 3, 8),
    (1, 8, 7),
    (1, 7, 3),
    (9, 5, 3),
    (24, 1, 4),
    (1, 3, 7),
    (11, 3, 8),
    (1, 7, 3),
    (1, 2, 4),
    (2, 2, 1),
    (2, 3, 5),
    (1, 6, 5),
    (10, 4, 6),
    (2, 6, 4),
    (5, 1, 2),
    (1, 6, 7),
    (8, 8, 6),
    (4, 2, 7),
    (8, 6, 7),
    (1, 2, 8),
    (1, 8, 3),
    (1, 7, 4),
    (3, 4, 1),
    (2, 6, 7),
    (4, 1, 9),
    (3, 6, 7),
    (10, 7, 4),
    (2, 3, 9),
    (2, 6, 9),
    (2, 1, 8),
    (2, 9, 5),
    (4, 5, 6),
    (3, 8, 1),
    (4, 4, 8),
    (5, 8, 4),
    (1, 8, 2),
    (5, 5, 9),
    (1, 6, 1),
    (2, 1, 7),
    (22, 4, 8),
    (4, 8, 7),
    (2, 6, 7),
    (1, 2, 6),
    (16, 8, 9),
    (3, 7, 4),
    (1, 5, 9),
    (2, 6, 7),
    (1, 8, 2),
    (1, 2, 3),
    (24, 9, 3),
    (1, 1, 7),
    (3, 5, 1),
    (4, 4, 6),
    (15, 3, 6),
    (18, 6, 2),
    (3, 3, 2),
    (4, 1, 6),
    (4, 7, 3),
    (1, 3, 9),
    (4, 2, 1),
    (1, 8, 7),
    (3, 9, 6),
    (1, 9, 3),
    (4, 7, 3),
    (2, 4, 2),
    (1, 1, 2),
    (7, 3, 5),
    (8, 6, 1),
    (1, 9, 2),
    (3, 7, 5),
    (1, 4, 8),
    (3, 1, 7),
    (5, 7, 6),
    (3, 5, 2),
    (3, 7, 3),
    (5, 5, 9),
    (5, 3, 6),
    (1, 8, 3),
    (5, 9, 7),
    (7, 2, 4),
    (11, 2, 7),
    (7, 1, 6),
    (1, 1, 9),
    (5, 3, 6),
    (5, 2, 1),
    (1, 3, 9),
    (1, 3, 7),
    (6, 6, 2),
    (10, 6, 7),
    (5, 6, 7),
    (28, 7, 8),
    (2, 9, 1),
    (1, 6, 3),
    (4, 7, 5),
    (1, 3, 6),
    (7, 2, 7),
    (6, 7, 3),
    (1, 5, 9),
    (1, 6, 2),
    (1, 7, 3),
    (1, 9, 1),
    (4, 5, 2),
    (5, 3, 5),
    (2, 2, 8),
    (4, 4, 7),
    (1, 4, 7),
    (2, 3, 6),
    (5, 7, 1),
    (2, 5, 8),
    (2, 5, 8),
    (2, 5, 3),
    (2, 3, 1),
    (2, 6, 7),
    (31, 8, 3),
    (2, 8, 5),
    (2, 7, 4),
    (7, 1, 4),
    (2, 5, 1),
    (3, 2, 8),
    (2, 4, 6),
    (3, 1, 2),
    (6, 4, 8),
    (1, 1, 8),
    (1, 6, 5),
    (11, 8, 9),
    (1, 6, 8),
    (1, 4, 1),
    (1, 8, 7),
    (1, 5, 8),
    (3, 2, 1),
    (2, 4, 3),
    (1, 8, 1),
    (7, 3, 6),
    (12, 3, 2),
    (1, 7, 9),
    (4, 6, 1),
    (1, 6, 3),
    (12, 9, 3),
    (1, 6, 4),
    (1, 1, 7),
    (1, 4, 1),
    (1, 7, 2),
    (1, 6, 5),
    (1, 5, 6),
    (5, 3, 1),
    (1, 6, 4),
    (7, 2, 1),
    (3, 2, 6),
    (1, 4, 5),
    (3, 3, 2),
    (4, 2, 8),
    (1, 6, 4),
    (1, 4, 9),
    (1, 5, 1),
    (11, 1, 5),
    (10, 1, 8),
    (2, 6, 4),
    (1, 2, 9),
    (1, 2, 4),
    (18, 3, 5),
    (4, 1, 4),
    (3, 1, 2),
    (14, 8, 5),
    (2, 2, 6),
    (1, 3, 2),
    (2, 2, 7),
    (3, 4, 1),
    (2, 4, 3),
    (2, 3, 4),
    (2, 6, 9),
    (1, 7, 1),
    (3, 1, 4),
    (4, 9, 7),
    (31, 5, 2),
    (25, 2, 4),
    (13, 4, 2),
    (10, 2, 3),
    (2, 5, 7),
    (5, 2, 9),
    (7, 5, 7),
    (5, 7, 4),
    (1, 5, 8),
    (2, 7, 3),
    (11, 4, 8),
    (1, 7, 3),
    (1, 1, 4),
    (2, 5, 3),
    (3, 2, 9),
    (8, 9, 6),
    (10, 8, 2),
    (5, 3, 2),
    (1, 7, 3),
    (3, 7, 3),
    (15, 2, 1),
    (11, 1, 3),
    (1, 8, 2),
    (8, 6, 5),
    (1, 2, 6),
    (1, 6, 1),
    (12, 3, 7),
    (1, 2, 9),
    (2, 4, 1),
    (3, 1, 8),
    (1, 8, 7),
    (3, 3, 4),
    (1, 4, 7),
    (15, 7, 9),
    (1, 7, 5),
    (4, 1, 8),
    (6, 8, 6),
    (1, 6, 2),
    (5, 5, 1),
    (2, 6, 8),
    (1, 2, 7),
    (1, 8, 2),
    (1, 7, 1),
    (1, 5, 8),
    (6, 3, 1),
    (4, 3, 8),
    (7, 8, 5),
    (1, 2, 4),
    (2, 4, 2),
    (3, 6, 4),
    (5, 9, 3),
    (4, 1, 4),
    (10, 5, 9),
    (8, 1, 7),
    (1, 2, 1),
    (1, 1, 9),
    (20, 9, 2),
    (12, 2, 3),
    (17, 4, 3),
    (6, 7, 2),
    (5, 3, 8),
    (20, 3, 5),
    (2, 9, 4),
    (3, 3, 1),
    (1, 7, 1),
    (6, 3, 6),
    (4, 2, 3),
    (4, 5, 3),
    (1, 1, 9),
    (6, 6, 1),
    (3, 8, 4),
    (1, 9, 8),
    (2, 2, 1),
    (3, 3, 2),
    (1, 3, 6),
    (1, 7, 4),
    (3, 3, 6),
    (6, 1, 5),
    (9, 2, 4),
    (3, 2, 5),
    (2, 6, 5),
    (16, 4, 8),
    (18, 8, 6),
    (1, 4, 5),
    (2, 6, 7),
    (4, 1, 7),
    (22, 5, 6),
    (1, 4, 9),
    (4, 7, 6),
    (11, 6, 5),
    (9, 5, 2),
    (2, 2, 3),
    (2, 7, 2),
    (1, 1, 7),
    (9, 6, 2),
    (1, 5, 1),
    (1, 8, 9),
    (18, 6, 8),
    (1, 7, 4),
    (4, 5, 1),
    (2, 5, 2),
    (2, 2, 5),
    (1, 9, 5),
    (1, 5, 9),
    (1, 9, 1),
    (1, 9, 2),
    (1, 4, 8),
    (4, 1, 4),
    (2, 6, 5),
    (1, 1, 9),
    (3, 6, 7),
    (1, 6, 9),
    (1, 9, 8),
    (2, 5, 9),
    (3, 3, 5),
    (7, 2, 3),
    (1, 1, 3),
    (2, 5, 9),
    (1, 5, 7),
    (10, 8, 3),
    (10, 8, 9),
    (3, 4, 3),
    (9, 2, 1),
    (4, 9, 6),
    (5, 1, 9),
    (2, 5, 9),
    (1, 6, 4),
    (4, 7, 2),
    (7, 2, 9),
    (3, 6, 8),
    (1, 1, 3),
    (2, 8, 5),
    (1, 8, 1),
    (18, 3, 6),
    (15, 9, 2),
    (8, 9, 1),
    (2, 9, 2),
    (2, 4, 9),
    (2, 9, 7),
    (12, 6, 3),
    (7, 1, 7),
    (12, 2, 5),
    (7, 3, 2),
    (4, 3, 4),
    (2, 7, 6),
    (7, 7, 8),
    (1, 4, 2),
    (4, 1, 8),
    (5, 3, 1),
    (9, 8, 3),
    (1, 8, 7),
    (2, 1, 2),
    (4, 6, 7),
    (11, 2, 5),
    (2, 4, 6),
    (1, 8, 2),
    (7, 3, 2),
    (1, 2, 4),
    (4, 6, 1),
    (7, 5, 8),
    (2, 3, 1),
    (7, 2, 3),
    (6, 5, 1),
    (1, 4, 2),
    (8, 1, 6),
    (3, 2, 9),
]


if __name__ == "__main__":
    for nb, src, dst in instr:
        crates, new_stack = stacks[src - 1][:nb], stacks[src - 1][nb:]
        stacks[src - 1] = new_stack
        stacks[dst - 1] = crates + stacks[dst - 1]

    result = "".join([stack[0] for stack in stacks])
    print(result)

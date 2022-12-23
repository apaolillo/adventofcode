"""
mjqjpqmgbljsphdztnvjfqwrcgsmlb: 7
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
"""

strings = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

exercise = "a"  # or 'b'
shift = 4 if exercise == "a" else 14

with open("input.txt") as f:
    fc = f.read().strip()
strings.append(fc)

for string in strings:
    for i in range(len(string)):
        seq = string[i : i + shift]
        if shift == len(set(seq)):
            print(i + shift)
            break

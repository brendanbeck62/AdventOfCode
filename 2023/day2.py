import os
import re

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def part1(in_str):
    acc = 0
    for line in in_str.split("\n"):
        if not line: continue
        print(line)
        id = re.match(r"Game (\d*):", line)[1]
        line = line.split(':')[1].strip()

        for reveal in line.split(';'):
            reveal = reveal.strip()

            is_impossible = False
            for subset in reveal.split(', '):
                n, color = subset.split()
                if int(n) > limits[color]:
                    is_impossible = True
                    break
            if is_impossible:
                break
        else:
            acc += int(id)
    return acc

def part2(in_str):
    acc = 0
    for line in in_str.split("\n"):
        if not line: continue
        print(line)
        id = re.match(r"Game (\d*):", line)[1]
        line = line.split(':')[1].strip()

        mins = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for reveal in line.split(';'):
            reveal = reveal.strip()
            for subset in reveal.split(', '):
                n, color = subset.split()
                mins[color] = max(int(n), mins[color])
        print(mins, mins['red'] * mins['green'] * mins['blue'])
        acc += mins['red'] * mins['green'] * mins['blue']
    return acc


DAY = os.path.basename(__file__).split(".")[0]
#FILE = "example1.txt"
# FILE = "example2.txt"
FILE = "in.txt"

with open(f"{DAY}/{FILE}", "r") as f:
    in_str = f.read()

print("Part 1:", part1(in_str))
print("Part 2:", part2(in_str))

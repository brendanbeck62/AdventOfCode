import os

def part1(in_str):
    for line in in_str.split('\n'):
        if not line: continue
        pass

def part2(in_str):
    for line in in_str.split('\n'):
        if not line: continue
        pass

DAY = os.path.basename(__file__).split('.')[0]
FILE = "example1.txt"
#FILE = "example2.txt"
#FILE = "in.txt"

with open(f"{DAY}/{FILE}", 'r') as f:
    in_str = f.read()

print('Part 1:', part1(in_str))
print('Part 2:', part2(in_str))
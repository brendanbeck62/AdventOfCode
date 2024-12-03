import os

def part1(in_str):
    for line in in_str.split('\n'):
        if not line: continue
        # solution here
        pass
    return

def part2(in_str):
    for line in in_str.split('\n'):
        if not line: continue
        # solution here
        pass
    return

FILE = "example1.txt"
#FILE = "example2.txt"
#FILE = "in.txt"

with open(FILE, 'r') as f:
    in_str = f.read()

print("============================================================")
print("                        PART 1")
print("============================================================")
print('Part 1: ', part1(in_str))
print("============================================================")
print("                        PART 2")
print("============================================================")
print('Part 2:', part2(in_str))
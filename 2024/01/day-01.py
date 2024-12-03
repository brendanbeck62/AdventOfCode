import os

def part1(in_str):
    a1 = []
    a2 = []
    for line in in_str.split('\n'):
        if not line: continue
        line_split = line.split(" ")
        a1.append(line_split[0])
        a2.append(line_split[-1])
    a1.sort()
    a2.sort()
    sum = 0
    for index, v1 in enumerate(a1):
        sum += abs(int(v1) - int(a2[index]))
    return sum

def part2(in_str):
    a1 = []
    a2 = []
    for line in in_str.split('\n'):
        if not line: continue
        line_split = line.split(" ")
        a1.append(line_split[0])
        a2.append(line_split[-1])
    sim_score = 0
    for v1 in a1:
        sim_score += int(v1) * a2.count(v1)
    return sim_score

#FILE = "example1.txt"
#FILE = "example2.txt"
FILE = "in.txt"

with open(FILE, 'r') as f:
    in_str = f.read()

print('Part 1:', part1(in_str))
print('Part 2:', part2(in_str))
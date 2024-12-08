import itertools
import operator
import os

VIS=False

def concat(a,b):
    return int(f"{a}{b}")

def solve(ans, vals, ops):
    if VIS: print(f"\n{ans}: {vals}")
    combos = list(itertools.product(ops, repeat=len(vals) - 1))
    for fn in combos:
        running = vals[0]
        if VIS: print(f"\t{running}",end='')
        for gap in range(0, len(vals)-1):
            running = fn[gap](running, vals[gap+1])
            if VIS: print (f" {fn[gap].__name__} {vals[gap+1]} = {running}",end='')
        if VIS: print()
        if running == ans:
            if VIS: print("FOUND")
            return running
    return 0

def part1(in_str):
    sum = 0

    ops = [operator.add, operator.mul]
    for line in in_str.split('\n'):
        if not line: continue
        eq = line.split(':')
        ans = int(eq[0])
        vals = list(map(int, eq[1].strip().split(" ")))
        sum += solve(ans, vals, ops)
    return sum

def part2(in_str):
    sum = 0

    ops = [operator.add, operator.mul, concat]
    for line in in_str.split('\n'):
        if not line: continue
        eq = line.split(':')
        ans = int(eq[0])
        vals = list(map(int, eq[1].strip().split(" ")))
        sum += solve(ans, vals, ops)
    return sum

#FILE = f"{os.path.dirname(__file__)}/example1.txt"
#FILE = f"{os.path.dirname(__file__)}/example2.txt"
FILE = f"{os.path.dirname(__file__)}/in.txt"

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
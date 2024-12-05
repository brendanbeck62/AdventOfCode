import os
import re

def part1(in_str):
    total = 0
    for line in in_str.split('\n'):
        if not line: continue
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        # matches looks like [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
        total += sum((int(x) * int(y)) for x,y in matches)
    return total

def part2(in_str):
    total = 0
    in_str = f"do(){in_str}don't()"
    print("\nLINE:")
    print(in_str)
    do_donts = re.findall(r"do\(\)(.*?)don't\(\)", in_str)
    for do_dont in do_donts:
        print()
        print(do_dont)
        muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", do_dont)
        # matches looks like [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
        print(muls)
        total += sum((int(x) * int(y)) for x,y in muls)
    return total

def part2_2(in_str):
    # this sucks... no capture groups bla. idk what the bug in mine was
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", in_str)
    res = 0
    flag = True
    for match in matches:
        if match == "do()":
            flag = True
        elif match =="don't()":
            flag = False
        else:
            if flag:
                x, y = map (int, match[4:-1].split(","))
                res += x * y
    return res

#FILE = "example1.txt"
#FILE = "example2.txt"
FILE = "in.txt"

with open(FILE, 'r') as f:
    in_str = f.read()

print("============================================================")
print("                        PART 1")
print("============================================================")
print('Part 1: ', part1(in_str)) #155955228
print("============================================================")
print("                        PART 2")
print("============================================================")
print('Part 2: ', part2_2(in_str)) #101681733
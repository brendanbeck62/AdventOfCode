import os
import re
import math

def part1(in_str):
    """Generate a set of every coordinate that is adjacent to a symbol.
    Then check if each integer's coordinate is in that set. If so, sum it's value.
    O(2n) where n = number of lines of data
    """
    lines = in_str.split('\n')

    # ^ = match everything EXCEPT . and \d (digit)
    symbol_regex = r'[^.\d]'
    # Build a set of every cell (row, col) that is adjacent to a symbol
    symbol_adjacent = set()
    for i, line in enumerate(lines):
        for m in re.finditer(symbol_regex, line):
            j = m.start()
            # i,j = row,col of symbol
            # NOTE: don't have to care about boundary checking because
            # there are not symbols on a boundary in the data
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    # matches all digits
    number_regex = r'\d+'
    acc = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            # if there is a coordinate in the symbol table that matches
            # the digit coordinate, add the digit to the sum
            # span returns (start, end) of the match, splatting it will do for each.
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                acc += int(m.group())
    return acc

def part2(in_str):
    """Create a dict that is key=(row,col) and value=[partNumInt]
    This allows for tracking each gear's position, and how many
    Digits there are adjacent to it. If there are exactly 2 values
    in the value of the dict, that key is a valid gear and the values
    should be processed.
    """
    lines = in_str.split('\n')

    # match only * characters
    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    # match all digits
    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            # for each digit
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    # if the r,c is the known position of a gear
                    # add the gear to the dict value list
                    if (r, c) in gears:
                        gears[(r,c)].append(int(m.group()))

    acc = 0
    for nums in gears.values():
        if len(nums) == 2:
            acc += nums[0]*nums[1]

    return acc


DAY = os.path.basename(__file__).split('.')[0]
#FILE = "example1.txt"
#FILE = "example2.txt"
FILE = "in.txt"

with open(f"{DAY}/{FILE}", 'r') as f:
    in_str = f.read()

print('Part 1:', part1(in_str))
print('Part 2:', part2(in_str))
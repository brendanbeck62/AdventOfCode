import os
import re

def part1(in_str):
    first_last = []
    for line in in_str.split('\n'):
        nums = [x for x in line if x.isdigit()]
        if nums:
            first_last.append(f"{nums[0]}{nums[-1]}")
    acc = 0
    for val in first_last:
        acc += int(val)
    return acc

def part2(in_str):
    def get_digit(x):
        return x if x.isnumeric() else str(letter_digits.index(x))

    letter_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    acc = 0

    for line in in_str.split('\n'):
        print(line)
        digits = re.findall(regex, line)
        print(digits)
        acc += int(get_digit(digits[0]) + get_digit(digits[-1]))

    return acc

DAY = os.path.basename(__file__).split('.')[0]
#FILE = "example1.txt"
#FILE = "example2.txt"
FILE = "in.txt"

with open(f"{DAY}/{FILE}", 'r') as f:
    in_str = f.read()

print('Part 1:', part1(in_str))
print('Part 2:', part2(in_str))
import os

def part1(in_str):

    zeros = 0
    pos = 50
    for line in in_str.split('\n'):
        if not line: continue
        if line[0] == 'L':
            pos -= int(line[1:])
        else:
            pos += int(line[1:])
        pos = pos % 100
        #print(f"({line}) - after: {pos}")
        if pos == 0:
            zeros += 1
    return zeros

def part2(in_str):
    zeros = 0
    pos = 50
    for line in in_str.split('\n'):
        if not line: continue

        print(f"starts at {pos}, moves {line}", end='')

        if line[0] == 'L':
            pos -= int(line[1:])
        else:
            pos += int(line[1:])

        print(f" to {pos}")

        if pos == 0:
            zeros += 1
            print(f"\tzero")
        else:
            while pos < 0:
                pos += 100
                zeros += 1
                print(f"\tpassed zero towards neg to {pos}")
            while pos >= 100:
                pos -= 100
                zeros += 1
                print(f"\tpassed zero towards pos to {pos}")

        print(f"after: {pos}, zeros: {zeros}\n")
    return zeros

def part2_goose(in_str):
    zeros = 0
    pos = 50
    for line in in_str.split('\n'):
        if not line: continue

        direction = line[0]
        distance = int(line[1:])

        # Count how many times we pass through 0 during this rotation
        if direction == 'L':
            # Moving left (toward lower numbers, wrapping at 0)
            for step in range(1, distance + 1):
                new_pos = (pos - step) % 100
                if new_pos == 0:
                    zeros += 1
        else:
            # Moving right (toward higher numbers, wrapping at 0)
            for step in range(1, distance + 1):
                new_pos = (pos + step) % 100
                if new_pos == 0:
                    zeros += 1

        # Update position to final position after rotation
        pos = (pos + distance if direction == 'R' else pos - distance) % 100

    return zeros


#FILE = f"{os.path.dirname(__file__)}/example1.txt"
#FILE = f"{os.path.dirname(__file__)}/example2.txt"
FILE = f"{os.path.dirname(__file__)}/in.txt"

with open(FILE, 'r') as f:
    in_str = f.read()

print("============================================================")
print("                        PART 1")
print("============================================================")
#print('Part 1: ', part1(in_str))
print("============================================================")
print("                        PART 2")
print("============================================================")
print('Part 2:', part2_goose(in_str))


"""
    50
L68 -18 - 88   = 1
L30 58
R48 100 - 0    = 2
L5
R260
L55
L1
L99
R14
L82
"""

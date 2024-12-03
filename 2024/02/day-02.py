import os

def safe_test(levels):
    asc = int(levels[1]) - int(levels[0])

    print(levels)
    for i, level in enumerate(levels):
        if i == 0: continue
        diff = int(levels[i]) - int(levels[i-1])
        if asc > 0 and (diff > 0):
            if abs(diff) > 3:
                print("much")
                return 0
            print("+yes", end=' ')
        elif asc < 0 and (diff < 0):
            if abs(diff) > 3:
                print("much")
                return 0
            print("-yes", end=' ')
        else:
            print("no")
            return 0
        if i == len(levels) - 1:
            print("DING")
            return 1
    print()

def part1(in_str):
    safe_count = 0
    for line in in_str.split('\n'):
        if not line: continue
        levels = line.split(' ')
        safe_count += safe_test(levels)
    return safe_count

def part2(in_str):
    safe_count = 0
    for line in in_str.split('\n'):
        if not line: continue
        levels = line.split(' ')

        if safe_test(levels) > 0:
            safe_count += 1
        else:
            levels_new = []
            # just brute force remove each element and try it
            for i in range(len(levels)):
                levels_new = levels.copy()
                print(i)
                del levels_new[i]
                # if we find ANY permutations that work, we win
                if safe_test(levels_new) > 0:
                    safe_count += 1
                    print("breaking")
                    break
        print()
    return safe_count


#FILE = "example1.txt"
#FILE = "example2.txt"
FILE = "in.txt"

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
import os
from pprint import pprint

# key must be before value
# '29': ['13'],
# '47': ['53', '13', '61', '29'],
# '53': ['29', '13'],
# '61': ['13', '53', '29'],
# '75': ['29', '53', '47', '61', '13'],
# '97': ['13', '61', '47', '29', '53', '75']
BEBUG = True
def isvalid(update, rules):
    # Y : 75,47,61,53,29
    # N : 75,97,47,61,53
    # There is a value in 97's list that CANT come before it
        # but does(75)
    # iterate backwards
        # if there is a value before current that exists in currents value
            # fail
    if BEBUG: print(f"CURRENT UPDATE: {update}")
    for i,val in enumerate(update):
        if BEBUG: print(val, end = ' ')
        if BEBUG: print('[',end='')
        # val = 97
        for check in update[:i]:
            # check = [75]
            # check if 'check' is in 97's list
            if (val in rules) and (check in rules[val]):
                if BEBUG: print("X]\n")
                return False
            if BEBUG: print(check, end = ',')
        if BEBUG: print(']')
    if BEBUG: print()

    return True

BUSTED = {}
def fix(update, rules, update_num):
    # Y : 75,47,61,53,29
    # N : 75,97,47,61,53

    # N : 97,13,75,29,47
    # N : 97,75,13,29,47
    # N : 97,75,29,13,47
    # N : 97,75,29,47,13
    # N : 97,75,47,29,13

    # There is a value in 97's list that CANT come before it
        # but does(75)
    # iterate backwards
        # if there is a value before current that exists in currents value
            # fail

    if BEBUG: print(f"CURRENT UPDATE: {update}")
    new_update = update.copy()
    if BEBUG: print(f"new_list: {new_update}")

    # iterate through the update
        # iterate backwards from each i, check = backwards iteration to look val's dict
        # if check is in val's dict, val needs to move in front of check
    for i,val in enumerate(update):
        if BEBUG: print(f"val={val}", end = ' [')
        for check in update[:i]:
            if BEBUG: print(check, end = ',')
            # if 'check' is in val's list, put check before val and run from check
            if (val in rules) and (check in rules[val]) and (i < len(update)):
                if BEBUG: print("X]")
                # remove check from newlist
                print(f"removing {val}")
                new_update.remove(val)

                # don't just swap the bad early and bad late, find the earliest place bad late can go
                # put val before the first element that exists in val's dict
                for j,jal in enumerate(update):
                    print(f"\tchecking {jal}")
                    if val in rules and jal in rules[val]:
                        print(f"found {jal} in {val}'s rules")
                        print(f"puting {val} in index {j}")
                        new_update[j:j] = [val]
                        break
                if BEBUG: print(f"new_list: {new_update}")
                # BUSTED keeps track of only those that needed fixed
                if update_num in BUSTED:
                    del BUSTED[update_num]

                print("fix on new list\n")
                BUSTED[update_num] = new_update
                # recurse and check the new list again
                fix(new_update, rules, update_num)
                return

        if BEBUG: print(']')
    if BEBUG: print("===== DONE NEXT!!!\n")

def part1(in_str):
    rules = {}
    updates = []
    rule_flag = True
    for line in in_str.split('\n'):
        if not line:
            rule_flag = False
            continue
        if rule_flag:
            rule = line.split('|')
            rule = list(map(int, rule))
            if rule[0] not in rules:
                rules[rule[0]] = [rule[1]]
            else:
                rules[rule[0]].append(rule[1])
        else:
            line_a = line.split(',')
            updates.append(list(map(int, line_a)))
    if BEBUG: print("rules:")
    if BEBUG: pprint(rules)

    mid_total = 0
    for update in updates:
        if isvalid(update, rules):
            mid_total += update[len(update)//2]
    return mid_total

def part2(in_str):
    rules = {}
    updates = []
    rule_flag = True
    for line in in_str.split('\n'):
        if not line:
            rule_flag = False
            continue
        if rule_flag:
            rule = line.split('|')
            rule = list(map(int, rule))
            if rule[0] not in rules:
                rules[rule[0]] = [rule[1]]
            else:
                rules[rule[0]].append(rule[1])
        else:
            line_a = line.split(',')
            updates.append(list(map(int, line_a)))
    if BEBUG: print("rules:")
    if BEBUG: pprint(rules)

    for i, update in enumerate(updates):
        fix(update, rules, i)
    print(BUSTED)
    mid_total = 0
    for update in BUSTED.values():
        mid_total += update[len(update)//2]
    return mid_total

#FILE = "example1.txt"
#FILE = "example2.txt"
FILE = "in.txt"

with open(FILE, 'r') as f:
    in_str = f.read()

print("============================================================")
print("                        PART 1")
print("============================================================")
#print('Part 1: ', part1(in_str))
print("============================================================")
print("                        PART 2")
print("============================================================")
print('Part 2:', part2(in_str))
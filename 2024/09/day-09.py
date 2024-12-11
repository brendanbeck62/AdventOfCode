import os
import copy

def checksum(str):
    sum = 0
    for i,c in enumerate(str):
        sum += int(c) * i
    return sum

#2333133121414135402
#2 3  3  3  13  3  12 14   14   13  14  02
#00...111...2...333.44.5555.6666.777.888899
def convert_to_dots(disk):
    dot_disk = []
    is_data = True
    id_count = 0
    id = 0
    for block in disk:
        char = '.'
        if is_data:
            char = id
            id += 1
            id_count += int(block)
        dot_disk.extend([f"{char}" for i in range(int(block))])
        is_data = not is_data
    return dot_disk, id_count

def convert_to_tuples(disk):
    dot_disk = []
    is_data = True
    id = 0
    starting_index = -1
    for count in disk:
        starting_index += 1
        char = -1
        if is_data:
            char = id
            id += 1
        if not is_data and count == '0':
            is_data = not is_data
            continue
        dot_disk.append((int(count), char, starting_index))
        is_data = not is_data
    return dot_disk

def part1(in_str):
    # in_str = 2333133121414131402
    dot_disk, ids = convert_to_dots(list(in_str))
    print("dot_disk")
    print(dot_disk)
    new_disk = []

    back_pointer = len(dot_disk)-1
    # 00...111...2...333.44.5555.6666.777.888899..1010
    for i,c in enumerate(dot_disk):
        if i >= ids:
            new_disk = new_disk[:i]
            break
        if c == '.':
            while dot_disk[back_pointer] == '.':
                back_pointer -= 1
            new_disk.append(dot_disk[back_pointer])
            back_pointer -= 1
        else:
            new_disk.append(c)

    print("new_disk")
    print(new_disk)
    return checksum(new_disk)

def part2(in_str):
    dot_disk = convert_to_tuples(list(in_str))
    print("dot_disk")
    print(dot_disk)
    new_disk = copy.deepcopy(dot_disk)

    # TODO will need to do while loop to update openings in place
    i = len(dot_disk)-1
    while i > 0:
        # (2,9)
        tup = dot_disk[i]
        # leave openings
        if tup[1] == -1:
            i -= 1
            continue
        print(f"trying to find a place for {tup}")
        # go forwards
        for j,opening in enumerate(new_disk):
            if j >= i:
                break
            # (2,0) , (3,-1)
            if opening[1] == -1 and opening[0] >= tup[0]:
                print(f"found an opening at index {j}: {opening}")
                # nuzzle him into the opening
                new_disk.remove(tup)
                # insert the moved file up
                new_disk.insert(j, tup)

                # TODO: there is a bug here when cleaning up the gaps.
                    # looks back and ahead for all adjecent gaps, and combines them
                    # there is an off by 1 that is putting the gap in the wrong place sometimes
                # insert the gap back in
                gap_index = i+2
                if gap_index >= len(dot_disk):
                    gap_index = i+1
                gap_size = tup[0]
                gap_count = gap_index - 1
                while gap_count < len(new_disk):
                    if new_disk[gap_count][1] > -1:
                        break
                    gap_size += new_disk[gap_count][0]
                    # deleteing it shifts everything after it left
                    # basically incrementing gap_count
                    del new_disk[gap_count]

                new_disk.insert(gap_count, (gap_size,-1,tup[2]))


                # subtract the disk size from the gap size
                new_disk[j+1] = (new_disk[j+1][0]-tup[0], -1, tup[2])
                # if the moved file files the entire gap, remove the gap node
                if new_disk[j+1][0]<=0:
                    del new_disk[j+1]

                break
        print(new_disk)
        i -= 1


    print(f"should be:\n00992111777.44.333....5555.6666.....8888..")

    sum = 0
    for tup in new_disk:
        sum += tup[0] * tup[1]
    return sum

FILE = f"{os.path.dirname(__file__)}/example1.txt"
#FILE = f"{os.path.dirname(__file__)}/example2.txt"
#FILE = f"{os.path.dirname(__file__)}/in.txt"

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



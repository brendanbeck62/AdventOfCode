import os

def check_surrounding(board, cords, next_char):
    #cords = (x,y)
    ret = []
    print(f"looking for {next_char}'s around {cords}")
    for loopy in range(-1, 2):
        for loopx in range(-1, 2):
            crdx = cords[0] + loopx
            crdy = cords[1] + loopy
            if crdy >= 0 and crdy < len(board) and crdx >= 0 and crdx < len(board[0]):
                print(f"\t({crdx},{crdy})={board[crdy][crdx]} [{loopx}, {loopy}]")
                if board[crdy][crdx] == next_char and (loopx != 0 or loopy != 0):
                    print("\tFOUND")
                    ret.append((crdx,crdy))
            else:
                print(f"\t({crdx},{crdy})=. [{loopx}, {loopy}]")
        print()
    return ret

# returns next_cord if char following prev, current, NEXT_CORD == next_char
    # else, returns None
def check_next(board, prev_cord, current_cord, current_char, next_char):
    print(f"found {current_char} at {current_cord}, looking for {next_char}")
    shift = (current_cord[0] - prev_cord[0], current_cord[1] - prev_cord[1])
    print(f"\tshift = {shift}")

    next_cord = (current_cord[0] + shift[0], current_cord[1] + shift[1])
    if next_cord[1] >= 0 and next_cord[1] < len(board) and next_cord[0] >= 0 and next_cord[0] < len(board[0]):
        print(f"\tnext = {next_cord} {board[next_cord[1]][next_cord[0]]}")
        if board[next_cord[1]][next_cord[0]] == next_char:
            return next_cord
    print("WRONG\n")
    return None

def inbounds(board, x, y):
    return y >= 0 and y < len(board) and x >= 0 and x < len(board[0])

# look around the given point, and return the offset of the 2 M's on the corners
    # something like [(-1, 1), (-1,-1)]
def check_surrounding_2(board, a_cord):
    possible_ms = {
        (1,1): [(1,-1),(-1,1)],
        (-1,1): [(-1,-1),(1,1)],
        (1,-1): [(-1,-1),(1,1)],
        (-1,-1): [(1,-1),(-1,1)]
    }
    for try_offset in possible_ms.keys():
        try_cord = (a_cord[0] + try_offset[0], a_cord[1] + try_offset[1])
        # if any of the corners have an M
        if inbounds(board, *try_cord) and board[try_cord[1]][try_cord[0]] == 'M':
            # if first value of key (1,-1)
            v1 = possible_ms[try_offset][0]
            v1_cord = (a_cord[0] + v1[0], a_cord[1] + v1[1])
            if inbounds(board, *v1_cord) and board[v1_cord[1]][v1_cord[0]] == 'M':
                return [try_offset, v1]

            # if first value of key (1,-1)
            v2 = possible_ms[try_offset][1]
            v2_cord = (a_cord[0] + v2[0], a_cord[1] + v2[1])
            if inbounds(board, *v2_cord) and board[v2_cord[1]][v2_cord[0]] == 'M':
                return [try_offset, v2]
    return None

def part1(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(line)

    xmas_count = 0
    for loopy in range(len(board)):
        for loopx in range(len(board[0])):
            if loopy >= 0 and loopy < len(board) and loopx >= 0 and loopx < len(board[0]):
                if board[loopy][loopx] == "X":
                    found_cords_m = check_surrounding(board, (loopx,loopy), 'M')
                    for m_cord in found_cords_m:
                        a_cord = check_next(board, (loopx,loopy), m_cord, 'M', 'A')
                        if a_cord:
                            s_cord = check_next(board, m_cord, a_cord, 'A', 'S')
                            if s_cord:
                                xmas_count += 1
    return xmas_count

def part2(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(line)
    """
    Same as part 1:
    - find an A
    - find each M Surrounding (only need to check 4 corners)
    - based on the direction traveled from the A to the M, go the other way and check for an S
    """

    xmas_count = 0
    for loopy in range(len(board)):
        for loopx in range(len(board[0])):
            if inbounds(board, loopx, loopy):
                if board[loopy][loopx] == "A":
                    print(f"found A at {(loopx,loopy)}")
                    # find 2 valid M offsets for an A cord (cant be kitty corner or else M A M)
                    # something like:
                        # A = (2,1)
                        # M = [(-1,-1), (-1,1)]
                    m_offsets = check_surrounding_2(board, (loopx,loopy))
                    if m_offsets:
                        # for each of the 2 valid m's offsets
                            # flip both the signs and check board. if both are S, profit
                        s1_offset = (m_offsets[0][0] * -1, m_offsets[0][1] * -1)
                        s2_offset = (m_offsets[1][0] * -1, m_offsets[1][1] * -1)
                        # need cords for s_1 and s_2
                        s1_cords = (loopx + s1_offset[0], loopy + s1_offset[1])
                        s2_cords = (loopx + s2_offset[0], loopy + s2_offset[1])
                        if inbounds(board, *s1_cords) and inbounds(board, *s2_cords) \
                            and board[s1_cords[1]][s1_cords[0]] == 'S' and board[s2_cords[1]][s2_cords[0]] == 'S':
                            print("xmas found")
                            xmas_count += 1
    return xmas_count

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
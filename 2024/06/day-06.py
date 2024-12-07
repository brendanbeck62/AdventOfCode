import os
import time
import sys
import json
import copy

directions = ['^','>','v','<']
moves = [(0,-1), (1,0), (0,1), (-1,0)]

VIS = True

def print_board(board):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))
    sys.stdout.write("\x1b[1A" * len(board))
    time.sleep(.25)

def get_start(board):
    for y in range(len(board)-1):
        for x in range(len(board[0])-1):
            if board[y][x] == "^":
                return (x,y)

def patrol(board, pos=None, curr_dir = None):
    if not pos:
        pos=get_start(board)
    if not curr_dir:
        curr_dir = 0

    rows, cols = len(board), len(board[0])

    visited = set()
    visited.add((pos[0], pos[1]))
    visited_entry = {}

    while True:
        d = moves[curr_dir]
        p = (pos[0] + d[0], pos[1] + d[1])

        if p[0] < 0 or p[0] >= rows or p[1] < 0 or p[1] >= cols:
            return True, visited, visited_entry

        if board[p[1]][p[0]] == "#":
            curr_dir = (curr_dir+1) % 4
            continue
        else:
            visited.add((p[0], p[1]))
            if p not in visited_entry:
                visited_entry[p] = (pos, curr_dir)
            elif visited_entry[p] == (pos, curr_dir):
                # we have already been on this square from this direction
                return False, None, None

            board[p[1]][p[0]] = directions[curr_dir]
            board[pos[1]][pos[0]] = "X"
            pos = p
            if VIS: print_board(board)

def part1(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(list(line))
    _, visited, _ = patrol(board)
    if VIS:print('\n'*len(board))
    return len(visited)

def part1_1(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(list(line))

    c_x = 0
    c_y = 0
    curr_dir = 0
    # find start
    for y in range(len(board)-1):
        for x in range(len(board[0])-1):
            if board[y][x] == "^":
                c_x = x
                c_y = y

    print_board(board)
    traveled_squares = 0
    while True:
        # move the guard in the direction hes facing

        if board[c_y + moves[curr_dir][1]][c_x + moves[curr_dir][0]] == '#':
            curr_dir = (curr_dir+1)%4

        next_square = board[c_y + moves[curr_dir][1]][c_x + moves[curr_dir][0]]

        if board[c_y + moves[curr_dir][1]][c_x + moves[curr_dir][0]] != 'X':
            traveled_squares += 1

        board[c_y][c_x] = 'X'

        c_x = c_x + moves[curr_dir][0]
        c_y = c_y + moves[curr_dir][1]

        board[c_y][c_x] = directions[curr_dir]

        print_board(board)
        if (c_y + moves[curr_dir][1] < 0) or (c_y + moves[curr_dir][1] >= len(board)) \
            or (c_x + moves[curr_dir][0] < 0) or (c_x + moves[curr_dir][0] >= len(board[0])):
            if board[c_y][c_x] != 'X':
                traveled_squares += 1
            print('\n'*len(board))
            break

    return traveled_squares

def part2(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(list(line))

    b_init = copy.deepcopy(board)
    _, visited, visited_entry = patrol(b_init)

    visited.remove(get_start(board)) # cant put it on guard
    loops = 0

    board_dump = json.dumps(board)
    # visited = [(x,y), (x,y)]
    # loop through all the squares that were visited
    for vx, vy in visited:
        b_copy = json.loads(board_dump)
        b_copy[vy][vx] = "#" # place a block

        pos = visited_entry[(vx, vy)][0]
        rot = visited_entry[(vx, vy)][1]

        # start at the square we visited in the same direction
        guard_gone_copy, _, _ = patrol(b_copy, pos, rot)
        if not guard_gone_copy:
            loops += 1

    if VIS:print('\n'*len(board))
    return loops

FILE = f"{os.path.dirname(__file__)}/example1.txt"
#FILE = f"{os.path.dirname(__file__)}/example2.txt"
#FILE = f"{os.path.dirname(__file__)}/in.txt"

with open(FILE, 'r') as f:
    in_str = f.read()

print("============================================================")
print("                        PART 1")
print("============================================================")
print('Part 1: ', part1(in_str))
print("============================================================")
print("                        PART 2")
print("============================================================")
#print('Part 2:', part2(in_str))
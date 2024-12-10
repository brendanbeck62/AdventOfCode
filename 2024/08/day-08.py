from pprint import pprint
import os

def inbounds(board, node):
    return node[0] >= 0 and node[0] < len(board[0]) and node[1] >= 0 and node[1] < len(board)

def part1(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(list(line))

    antennas = {}
    for y in range(len(board)):
        #ant = board[y][x]
        ants = [i for i, x in enumerate(board[y]) if x != "."]
        for x in ants:
            ant = board[y][x]
            if ant not in antennas:
                antennas[ant] = [(x,y)]
            else:
                antennas[ant].append((x,y))

    print(antennas)
    nodes = set()
    for char in antennas.keys():
        print(char)
        for curr in antennas[char]:
            print(f"{curr}")
            for partner in antennas[char]:
                if curr != partner:
                    print('\t',partner, end=' ')
                    d = (curr[0] - partner[0], curr[1] - partner[1])
                    print(d[0],d[1], end=' ')
                    new_node = (curr[0] + d[0], curr[1] + d[1])
                    print(new_node)
                    if inbounds(board, new_node):
                        nodes.add(new_node)
            print()
    print(nodes)
    return len(nodes)

def part2(in_str):
    board = []
    for line in in_str.split('\n'):
        if not line: continue
        board.append(list(line))

    antennas = {}
    for y in range(len(board)):
        #ant = board[y][x]
        ants = [i for i, x in enumerate(board[y]) if x != "."]
        for x in ants:
            ant = board[y][x]
            if ant not in antennas:
                antennas[ant] = [(x,y)]
            else:
                antennas[ant].append((x,y))

    print(antennas)
    nodes = set()
    # loop through each frequency (unique character)
    for char in antennas.keys():
        print(char)
        # loop through each antennea with the given character
        for curr in antennas[char]:
            print(f"{curr}")
            # loop through each adjcent antennea
            for partner in antennas[char]:
                if curr != partner:
                # calculate the 'slope' of the line
                    print('\t',partner, end=' ')
                    d = (curr[0] - partner[0], curr[1] - partner[1])
                    print(d[0],d[1], end=' ')

                    # do partner instead of curr so that curr gets counted as the
                        # first new_node
                    new_node = (partner[0] + d[0], partner[1] + d[1])
                    while inbounds(board, new_node):
                        print(new_node)
                        nodes.add(new_node)
                        new_node = (new_node[0] + d[0], new_node[1] + d[1])
        print()


                # add every square inbounds on the given slope, including those with the antennea
    print(nodes)
    return len(nodes)

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
print('Part 2:', part2(in_str))
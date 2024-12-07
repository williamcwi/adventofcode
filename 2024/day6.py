import os
from copy import copy, deepcopy

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'guard_gallivant.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

map = []
for line in lines:
    map.append(list(line))

y = len(map)
x = len(map[0])

for row in range(y):
    for col in range(x):
        # find initial position
        if map[row][col] == '^':
            coord = (row, col)
            direction = 'n'

def step(coord, direction, m):
    row, col = coord
    if direction == 'n':
        if row == 0:
            # exits m
            m[row][col] = 'X'
            return None, None
        elif m[row-1][col] == '#':
            # turn right
            return coord, 'e'
        else:
            # move forward
            m[row][col] = 'X'
            return (row-1, col), direction
        
    elif direction == 'e':
        if col == x-1:
            # exits m
            m[row][col] = 'X'
            return None, None
        elif m[row][col+1] == '#':
            # turn right
            return coord, 's'
        else:
            # move forward
            m[row][col] = 'X'
            return (row, col+1), direction
        
    elif direction == 's':
        if row == y-1:
            # exits m
            m[row][col] = 'X'
            return None, None
        elif m[row+1][col] == '#':
            # turn right
            return coord, 'w'
        else:
            # move forward
            m[row][col] = 'X'
            return (row+1, col), direction
        
    elif direction == 'w':
        if col == 0:
            # exits m
            m[row][col] = 'X'
            return None, None
        elif m[row][col-1] == '#':
            # turn right
            return coord, 'n'
        else:
            # move forward
            m[row][col] = 'X'
            return (row, col-1), direction

def traverse_map(c, d, m):
    exited = False
    i = 0
    while exited == False:
        i += 1
        c, d = step(c, d, m)
        if c == None:
            exited = True
        if i == 25000:
            return True
    return False

traverse_map(coord, direction, map)
# print('\n'.join(' '.join(str(x) for x in row) for row in map))

results1 = sum(x.count('X') for x in map)

results2 = 0

for row in range(y):
    for col in range(x):
        if map[row][col] == '#':
            continue
        else:
            temp_map = deepcopy(map)
            temp_map[row][col] = '#'
            if traverse_map(coord, direction, temp_map):
                results2 += 1

print(f'Part 1: {results1}')
print(f'Part 2: {results2}')

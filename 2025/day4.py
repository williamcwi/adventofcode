import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'printing_department.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    map = f.read().splitlines()

p1 = 0
p2 = 0

DELTAS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def count_surrounding(coord, map):
    i, j = coord
    count = 0
    for di, dj in DELTAS:
        ni = i + di
        nj = j + dj
        if 0 <= ni < len(map) and 0 <= nj < len(map[ni]):
            if map[ni][nj] == '@':
                count += 1
    return count

# Part 1
for i in range(len(map)):
    for j in range(len(map[i])):
        coord = (i,j)
        symbol = map[i][j]
        if symbol == '@' and count_surrounding(coord, map) < 4:
            p1 += 1

# Part 2
map_copy = [list(row) for row in map]
while True:
    to_remove = []

    for i in range(len(map_copy)):
        for j in range(len(map_copy[i])):
            coord = (i,j)
            symbol = map_copy[i][j]
            if symbol == '@' and count_surrounding(coord, map_copy) < 4:
                to_remove.append(coord)

    if not to_remove:
        break

    for i, j in to_remove:
        map_copy[i][j] = '.'

    p2 += len(to_remove)

print(f'Part 1: {p1}\nPart 2: {p2}')
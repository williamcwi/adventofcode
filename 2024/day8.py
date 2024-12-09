import os
from itertools import combinations

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'resonant_collinearity.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

antinodes = [['.']*len(lines[0]) for _ in range(len(lines))]
map = []
for line in lines:
    map.append(list(line))

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

all_chars = list(set(''.join(lines)))
for char in all_chars:
    if char not in characters:
        all_chars.remove(char)

for char in all_chars:
    occurances = []
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if map[row][col] == char:
                occurances.append((row, col))
    all_comb = combinations(occurances, 2)
    for comb in all_comb:
        coord1, coord2 = comb
        diff = (coord2[0]-coord1[0],coord2[1]-coord1[1])
        anti = [(coord2[0]+diff[0],coord2[1]+diff[1]),(coord1[0]-diff[0],coord1[1]-diff[1])]
        for a in anti:
            if a[0] < 0 or a[0] >= len(antinodes) or a[1] < 0 or a[1] >= len(antinodes):
                pass
            else:
                a[0], a[1]
                antinodes[a[0]][a[1]] = '#'

results1 = sum(x.count('#') for x in antinodes)
print(f'Part 1: {results1}')

antinodes2 = [['.']*len(lines[0]) for _ in range(len(lines))]

for char in all_chars:
    occurances = []
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if map[row][col] == char:
                occurances.append((row, col))
    all_comb = combinations(occurances, 2)
    for comb in all_comb:
        coord1, coord2 = comb
        diff = (coord2[0]-coord1[0],coord2[1]-coord1[1])
        anti = []
        c = True
        while c:
            if coord2[0] < 0 or coord2[0] >= len(antinodes2) or coord2[1] < 0 or coord2[1] >= len(antinodes2):
                c = False
            else:
                antinodes2[coord2[0]][coord2[1]] = '#'
                coord2 = (coord2[0]+diff[0],coord2[1]+diff[1])
        c = True
        while c:
            if coord1[0] < 0 or coord1[0] >= len(antinodes2) or coord1[1] < 0 or coord1[1] >= len(antinodes2):
                c = False
            else:
                antinodes2[coord1[0]][coord1[1]] = '#'
                coord1 = (coord1[0]-diff[0],coord1[1]-diff[1])

results2 = sum(x.count('#') for x in antinodes2)
print(f'Part 2: {results2}')
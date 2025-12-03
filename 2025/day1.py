import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'secret_entrance.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

p1 = 0
p2 = 0
dial = 50
for l in lines:
    direction, number = l[0], int(l[1:])
    for _ in range(number):
        if direction == 'L':
            dial = (dial - 1) % 100
        elif direction == 'R':
            dial = (dial + 1) % 100
        if dial == 0:
            p2 += 1
    if dial == 0:
        p1 += 1

print(f'Part 1: {p1}\nPart 2: {p2}')
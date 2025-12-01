import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'secret_entrance.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

results = 0
dial = 50
for l in lines:
    direction, number = l[0], int(l[1:])

    if direction == 'L':
        dial -= number
    elif direction == 'R':
        dial += number

    if dial % 100 == 0:
        results += 1

print(f'Results: {results}')
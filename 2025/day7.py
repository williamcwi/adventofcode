import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'laboratories.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

p1 = 0
start = lines[0].index("S")

beams = {start}

for row in lines[1:]:
    next_beams = set()

    for col in beams:
        if row[col] == "^":
            p1 += 1
            next_beams.add(col - 1)
            next_beams.add(col + 1)
        else:
            next_beams.add(col)

    beams = next_beams

beams = {start: 1}

for row in lines[1:]:
    next_beams = {}

    for col, count in beams.items():
        if row[col] == "^":
            next_beams[col - 1] = next_beams.get(col - 1, 0) + count
            next_beams[col + 1] = next_beams.get(col + 1, 0) + count
        else:
            next_beams[col] = next_beams.get(col, 0) + count

    beams = next_beams

p2 = sum(beams.values())

print(f'Part 1: {p1}\nPart 2: {p2}')
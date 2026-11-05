import os
from itertools import combinations
from math import prod

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'playground.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

p1=0
p2=0

boxes = [tuple(map(int, line.split(','))) for line in lines]

def distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

pairs = []
for i, j in combinations(range(len(boxes)), 2):
    a = boxes[i]
    b = boxes[j]
    pairs.append((distance(a,b), i, j))
pairs.sort()

circuits = [{i} for i in range(len(boxes))]

for dist, i, j in pairs[:1000]:
    circuit_a = None
    circuit_b = None

    for circuit in circuits:
        if i in circuit:
            circuit_a = circuit
        if j in circuit:
            circuit_b = circuit

    if circuit_a is not circuit_b:
        circuit_a.update(circuit_b)
        circuits.remove(circuit_b)

sizes = sorted([len(circuit) for circuit in circuits], reverse=True)

p1 = prod(sizes[:3])

for dist, i, j in pairs[1000:]:
    circuit_a = None
    circuit_b = None

    for circuit in circuits:
        if i in circuit:
            circuit_a = circuit
        if j in circuit:
            circuit_b = circuit

    if circuit_a is not circuit_b:
        circuit_a.update(circuit_b)
        circuits.remove(circuit_b)

        if len(circuits) == 1:
            p2 = boxes[i][0] * boxes[j][0]
            break

print(f'Part 1: {p1}\nPart 2: {p2}')
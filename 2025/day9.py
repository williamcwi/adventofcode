import os
from itertools import combinations
from math import prod

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'movie_theater.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

p1=0
p2=0

tiles = [tuple(map(int, line.split(','))) for line in lines]

def area(a, b):
    return prod((abs(x - y) + 1) for x, y in zip(a, b))

for i, j in combinations(tiles, 2):
    p1 = max(p1, area(i,j))

edges = []

for i in range(len(tiles)):
    a = tiles[i]
    b = tiles[(i + 1) % len(tiles)]
    edges.append((a, b))


def point_inside(x, y):
    inside = False

    for (ax, ay), (bx, by) in edges:

        if ax == bx and x == ax:
            if min(ay, by) <= y <= max(ay, by):
                return True

        if ay == by and y == ay:
            if min(ax, bx) <= x <= max(ax, bx):
                return True

        if (ay > y) != (by > y):
            intersection_x = ax + (y - ay) * (bx - ax) / (by - ay)

            if x < intersection_x:
                inside = not inside

    return inside


def valid_rectangle(a, b):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))

    if not point_inside((x1 + x2) / 2, (y1 + y2) / 2):
        return False

    for (ax, ay), (bx, by) in edges:

        if ax == bx: # Vertical edge
            edge_y1, edge_y2 = sorted((ay, by))

            if x1 < ax < x2 and max(y1, edge_y1) < min(y2, edge_y2):
                return False

        else: # Horizontal edge
            edge_x1, edge_x2 = sorted((ax, bx))

            if y1 < ay < y2 and max(x1, edge_x1) < min(x2, edge_x2):
                return False

    return True


for a, b in combinations(tiles, 2):
    current_area = area(a, b)

    if current_area > p2 and valid_rectangle(a, b):
        p2 = current_area

print(f'Part 1: {p1}\nPart 2: {p2}')
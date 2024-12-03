import os
import re

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'mull_it_over.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

results1 = 0
for line in lines:
    muls = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    for mul in muls:
        m = mul[4:-1].split(',')
        results1 += (int(m[0])*int(m[1]))

print(f'Part 1: {results1}')

results2 = 0
multiply = True
for line in lines:
    com = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",line)
    for c in com:
        if c == 'do()':
            multiply = True
        elif c == "don't()":
            multiply = False
        else:
            if multiply:
                m = c[4:-1].split(',')
                results2 += (int(m[0])*int(m[1]))

print(f'Part 2: {results2}')
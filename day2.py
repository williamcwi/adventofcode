import os
import re

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

with open(os.path.join(INPUT_DIR, 'cube_conundrum.txt'), 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

answer = 0

for i, line in enumerate(lines):
    flag = False
    for red in re.findall(r'\d+ red',line):
        r = int(re.sub(r'[a-zA-Z ]',"",red))
        if(r > RED_MAX):
            flag = True
    for green in re.findall(r'\d+ green',line):
        g = int(re.sub(r'[a-zA-Z ]',"",green))
        if(g > GREEN_MAX):
            flag = True
    for blue in re.findall(r'\d+ blue',line):
        b = int(re.sub(r'[a-zA-Z ]',"",blue))
        if(b > BLUE_MAX):
            flag = True
    if not flag:
        answer += i+1

print('Part 1 Answer: {}'.format(answer))

answer = 0

for line in lines:
    maxRed = 0
    for y in re.findall(r'\d+ red',line):
        temp = int(re.sub(r'[a-zA-Z ]',"",y))
        if(temp > maxRed):
            maxRed = temp
    maxGreen = 0
    for y in re.findall(r'\d+ green',line):
        temp = int(re.sub(r'[a-zA-Z ]',"",y))
        if(temp > maxGreen):
            maxGreen = temp
    maxBlue = 0
    for y in re.findall(r'\d+ blue',line):
        temp = int(re.sub(r'[a-zA-Z ]',"",y))
        if(temp > maxBlue):
            maxBlue = temp
    answer += maxRed*maxGreen*maxBlue

print('Part 2 Answer: {}'.format(answer))
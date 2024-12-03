import os
import re

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

with open(os.path.join(INPUT_DIR, 'trebuchet.txt'), 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

def first(s):
    for i, c in enumerate(s):
        if c.isdigit():
            return s[i]

def last(s):
    s = s[::-1]
    for i, c in enumerate(s):
        if c.isdigit():
            return s[i]

answer = 0
for line in lines:
    answer += int(str(first(line)) + str(last(line)))

print('Part 1 Answer: {}'.format(answer))

answer = 0
for line in lines:
    newStr = re.sub(r'one',"o1e",line)
    newStr = re.sub(r'two',"t2o",newStr)
    newStr = re.sub(r'three',"t3e",newStr)
    newStr = re.sub(r'four',"f4r",newStr)
    newStr = re.sub(r'five',"f5e",newStr)
    newStr = re.sub(r'six',"s6x",newStr)
    newStr = re.sub(r'seven',"s7n",newStr)
    newStr = re.sub(r'eight',"e8t",newStr)
    newStr = re.sub(r'nine',"n9e",newStr)
    answer += int(str(first(newStr)) + str(last(newStr)))

print('Part 2 Answer: {}'.format(answer))
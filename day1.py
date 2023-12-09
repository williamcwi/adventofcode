import os
import re

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

def first(s):
    for i, c in enumerate(s):
        if c.isdigit():
            return s[i]

def last(s):
    s = s[::-1]
    for i, c in enumerate(s):
        if c.isdigit():
            return s[i]

with open(os.path.join(INPUT_DIR, 'trebuchet.txt'), 'r', encoding='UTF-8') as f:
    answer = 0
    for row in f:
        answer += int(str(first(row)) + str(last(row)))

print('Part 1 Answer: {}'.format(answer))

with open(os.path.join(INPUT_DIR, 'trebuchet.txt'), 'r', encoding='UTF-8') as f:
    answer = 0
    for row in f:
        newStr = re.sub(r'one',"o1e",row)
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
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
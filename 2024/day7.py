import os
from itertools import product

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'bridge_repair.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

results1 = 0
results2 = 0

for line in lines: 
    temp = line.split(' ')
    target = temp[0][:-1]
    numbers = list(map(int, temp[1:]))
    operators_num = len(numbers) - 1
    all_operators = [p for p in product(['+','*'], repeat=operators_num)]
    for operators in all_operators:
        equation = ''
        answer = numbers[0]
        for i,operator in zip(range(1, operators_num+1),operators):
            if operator == '+':
                answer = answer + numbers[i]
            elif operator == '*':
                answer = answer * numbers[i]
        if answer == int(target):
            results1 += int(target)
            break

print(f'Part 1: {results1}')

for line in lines: 
    temp = line.split(' ')
    target = temp[0][:-1]
    numbers = list(map(int, temp[1:]))
    operators_num = len(numbers) - 1
    all_operators = [p for p in product(['+','*','||'], repeat=operators_num)]
    for operators in all_operators:
        equation = ''
        answer = numbers[0]
        for i,operator in zip(range(1, operators_num+1),operators):
            if operator == '+':
                answer = answer + numbers[i]
            elif operator == '*':
                answer = answer * numbers[i]
            elif operator == '||':
                answer = int(str(answer)+str(numbers[i]))
        if answer == int(target):
            results2 += int(target)
            break

print(f'Part 2: {results2}')
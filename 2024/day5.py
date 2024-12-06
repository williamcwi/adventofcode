import os
import itertools

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'print_queue.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

isRule = True
rules = []
updates = []
results1 = 0
results2 = 0
for line in lines:
    if line == '':
        isRule = False
        continue
    if isRule == True:
        temp = line.split('|')
        rules.append((temp[0],temp[1]))
    else: 
        updates.append(line.split(','))

incorrect = []

def get_median(list):
    median = int((len(list)-1)/2)
    return int(list[median])

for update in updates:
    correct_sequence = True
    combinations = list(itertools.combinations(update, 2))
    for combination in combinations:
        combination = (combination[1], combination[0])
        if combination in rules:
            correct_sequence = False
            incorrect.append(update)
            break

    if correct_sequence:
        results1 += get_median(update)

print(f'Part 1: {results1}')

for update in incorrect:
    correct_sequence = False
    while correct_sequence == False:
        temp = True
        combinations = list(itertools.combinations(update, 2))
        for combination in combinations:
            combination = (combination[1], combination[0])
            if combination in rules:
                temp = False
                a, b = update.index(combination[0]), update.index(combination[1])
                update[a], update[b] = update[b], update[a]
        if temp:
            correct_sequence = True
            results2 += get_median(update)

print(f'Part 2: {results2}')
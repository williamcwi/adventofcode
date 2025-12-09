import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'trash_compactor.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

p1 = 0
p2 = 0

# Part 1
array_2d = list(zip(*[list(map(int, line.split())) for line in lines[:-1]][::-1]))
operators = lines[-1].split()

for nums, oper in zip(array_2d, operators):
    if oper == '+':
        results = 0
        for n in nums:
            results += n
    elif oper == '*':
        results = 1
        for n in nums:
            results *= n
    p1 += results

# Part 2
width = max(len(line) for line in lines)
grid = [line.ljust(width) for line in lines]

rows = len(grid)
digit_rows = grid[:-1]
ops_row = grid[-1]

problems = []
current_problem = []

for c in range(width):
    col_digits = []
    for r in range(rows - 1):
        ch = digit_rows[r][c]
        if ch.isdigit():
            col_digits.append(ch)

    num_str = ''.join(col_digits)
    op_char = ops_row[c]

    is_separator = (num_str == '' and op_char == ' ')

    if is_separator:
        if current_problem:
            problems.append(current_problem[::-1])
            current_problem = []
    else:
        if num_str:
            current_problem.append(int(num_str))

if current_problem:
    problems.append(current_problem[::-1])

ops = ops_row.split()

for nums, oper in zip(problems, ops):
    if oper == '+':
        result = sum(nums)
    elif oper == '*':
        result = 1
        for n in nums:
            result *= n
    p2 += result

print(f'Part 1: {p1}\nPart 2: {p2}')
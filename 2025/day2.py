import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'gift_shop.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().split(',')

p1 = 0
p2 = 0
for l in lines:
    start_str, end_str = l.split('-')
    start = int(start_str)
    end = int(end_str)

    for value in range(start, end + 1):
        num = str(value)
        digits = len(num)

        # Part 1
        if digits % 2 == 0:
            half = digits // 2
            if num[:half] == num[half:]:
                p1 += value

        # Part 2
        for block_size in range(1, digits // 2 + 1):
            if digits % block_size != 0:
                continue
            block = num[:block_size]
            repeats = digits // block_size
            if block * repeats == num:
                p2 += value
                break

print(f'Part 1: {p1}\nPart 2: {p2}')
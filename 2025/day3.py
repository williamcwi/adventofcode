import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'lobby.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

p1 = 0
p2 = 0

def max_joltage(bank: str, k: int) -> int:
    digits = bank.strip()
    n = len(digits)
    result_digits = []
    start = 0

    for remaining in range(k, 0, -1):
        end = n - remaining
        best_pos = start
        for i in range(start, end + 1):
            if digits[i] > digits[best_pos]:
                best_pos = i
        result_digits.append(digits[best_pos])
        start = best_pos + 1

    return int("".join(result_digits))

for l in lines:
    p1 += max_joltage(l, 2)
    p2 += max_joltage(l, 12)

print(f'Part 1: {p1}\nPart 2: {p2}')
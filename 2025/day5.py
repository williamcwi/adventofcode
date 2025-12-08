import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'cafeteria.txt')
fresh_ranges = []
available_ids = []

with open(input_file, 'r', encoding='UTF-8') as f:
    reading_ranges = True
    for line in f:
        line = line.strip()
        if line == "":
            reading_ranges = False
            continue

        if reading_ranges:
            lo_str, hi_str = line.split("-")
            lo, hi = int(lo_str), int(hi_str)
            fresh_ranges.append((lo, hi))
        else:
            available_ids.append(int(line))

p1 = 0
p2 = 0

# Part 1
for x in available_ids:
    if any(lo <= x <= hi for lo, hi in fresh_ranges):
        p1 += 1

# Part 2
fresh_ranges.sort()
merged = []
cur_lo, cur_hi = fresh_ranges[0]

for lo, hi in fresh_ranges[1:]:
    if lo <= cur_hi + 1:
        cur_hi = max(cur_hi, hi)
    else:
        merged.append((cur_lo, cur_hi))
        cur_lo, cur_hi = lo, hi

merged.append((cur_lo, cur_hi))

p2 = sum(hi - lo + 1 for lo, hi in merged)

print(f'Part 1: {p1}\nPart 2: {p2}')
import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'red-nosed_reports.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

def is_safe(report, levels):
    diff = []
    for level in range(levels-1):
        diff.append(report[level+1] - report[level])
    
    if not min(diff) < 0 < max(diff):
        if all(1 <= abs(x) <= 3 for x in diff):
            return True
        
    return False

results1 = 0

for line in lines:
    report = [int(x) for x in line.split(' ')]
    levels = len(report)
    
    if is_safe(report, levels):
        results1 += 1

print(f'Part 1: {results1}')

results2 = 0

for line in lines:
    report = [int(x) for x in line.split(' ')]
    levels = len(report)
    
    if is_safe(report, levels):
        results2 += 1
    else: 
        for i in range(levels):
            temp_report = list(report)
            temp_report.pop(i)
            if is_safe(temp_report, levels-1):
                results2 += 1
                break

print(f'Part 2: {results2}')
import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'historian_hysteria.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

list1 = []
list2 = []

for line in lines:
    num1, num2 = line.split('   ')
    list1.append(int(num1))
    list2.append(int(num2))

list1, list2 = sorted(list1), sorted(list2)
sum1 = 0
for first, second in zip(list1, list2):
    diff = abs(first-second)
    sum1 += diff

print(f'Part 1: {sum1}')

sum2 = 0
for num in list1:
    score = list2.count(num) * num
    sum2 += score

print(f'Part 2: {sum2}')
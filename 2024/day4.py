import os

ROOT_DIR = os.path.abspath('./')
INPUT_DIR = os.path.join(ROOT_DIR, 'inputs')

input_file = os.path.join(INPUT_DIR,'ceres_search.txt')
with open(input_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()

matrix = []
for line in lines:
    matrix.append(line)
rows = len(matrix)
cols = len(matrix[0])

def get_word(row, col):
    directions = ['r', 'd', 'l', 'u', 'ur', 'ul', 'dr', 'dl']
    words = []
    if row < 3:
        if 'u' in directions: directions.remove('u')
        if 'ur' in directions: directions.remove('ur')
        if 'ul' in directions: directions.remove('ul')
    elif row > (rows - 4):
        if 'd' in directions: directions.remove('d')
        if 'dr' in directions: directions.remove('dr')
        if 'dl' in directions: directions.remove('dl')
    if col < 3:
        if 'l' in directions: directions.remove('l')
        if 'ul' in directions: directions.remove('ul')
        if 'dl' in directions: directions.remove('dl')
    elif col > (cols - 4):
        if 'r' in directions: directions.remove('r')
        if 'ur' in directions: directions.remove('ur')
        if 'dr' in directions: directions.remove('dr')

    for d in directions:
        word_list = []
        for i in range(4):
            if d == 'r':
                word_list.append(matrix[row][col+i])
            if d == 'd':
                word_list.append(matrix[row+i][col])
            if d == 'l':
                word_list.append(matrix[row][col-i])
            if d == 'u':
                word_list.append(matrix[row-i][col])
            if d == 'ur':
                word_list.append(matrix[row-i][col+i])
            if d == 'ul':
                word_list.append(matrix[row-i][col-i])
            if d == 'dr':
                word_list.append(matrix[row+i][col+i])
            if d == 'dl':
                word_list.append(matrix[row+i][col-i])
        words.append(''.join(word_list))
        
    return words.count('XMAS')

results1 = 0

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'X':
            results1 += get_word(row, col)

print(f'Part 1: {results1}')

def get_xmas(row, col):
    if row < 1 or row > rows - 2 or col < 1 or col > cols - 2:
        return 0
    
    word1 = ''.join([matrix[row-1][col-1],matrix[row][col],matrix[row+1][col+1]])
    word2 = ''.join([matrix[row-1][col+1],matrix[row][col],matrix[row+1][col-1]])
    if (word1 == 'MAS' or word1 == 'SAM') and (word2 == 'MAS' or word2 == 'SAM'):
        return 1
    else: 
        return 0

results2 = 0

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'A':
            results2 += get_xmas(row, col)

print(f'Part 2: {results2}')
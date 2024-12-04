import numpy as np

# Read the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()

count = 0
word = "XMAS"

# Create a NumPy array from the file contents
matrix = np.array([list(line.strip()) for line in lines])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def in_bounds(x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

count = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == word[0]:
            for direction in directions:
                found = True
                for i in range(1, len(word)):
                    new_x, new_y = x + i * direction[0], y + i * direction[1]
                    if not in_bounds(new_x, new_y) or matrix[new_x][new_y] != word[i]:
                        found = False
                        break
                if found:
                    count +=1

print(count)


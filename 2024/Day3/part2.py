import re

#Load the input file
file = open("input.txt", "r")
lines = file.read()

# Extract commands and process them one by one
commands = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', lines)
skip = False

results = 0

for command in commands:
    if "don't()" in command:
        skip = True
    elif 'do()' in command:
        skip = False
    elif 'mul(' in command and not skip:
        numbers = re.findall(r'\d+', command)
        if numbers and len(numbers) == 2:
            result = int(numbers[0]) * int(numbers[1])
            results += result

print(results)

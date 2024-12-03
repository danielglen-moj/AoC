#imports
import re

#Load the input file
file = open("input.txt", "r")
lines = file.read()

regex = r"mul\(\d+,\d+\)"

matches = re.findall(regex, lines)

total = 0

for match in matches:
    multiply = match.replace("mul(", "").replace(")", "")
    x, y = multiply.split(",")
    total += (int(x) * int(y))

print(total)


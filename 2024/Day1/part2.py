# Load the input file
file = open("input.txt", "r")
lines = file.readlines()

# Initialise the total
total = 0

# Initialise the arrays
leftside = []
rightside = []

for line in lines:
    leftside.append(int(line.split("   ")[0]))
    rightside.append(int(line.split("   ")[1]))

for i in range(0, len(leftside)):
    total += leftside[i] * rightside.count(leftside[i])

print(total)
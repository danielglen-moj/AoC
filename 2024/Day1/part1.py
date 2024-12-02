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

# Sort the arrays into numerical order
leftside = sorted(leftside)
rightside = sorted(rightside)

# Loop through the arrays and add the difference between the two values to the total
for i in range(0, len(leftside)):
    if leftside[i] > rightside[i]:
        total += leftside[i] - rightside[i]
    else:
        total += rightside[i] - leftside[i]

# Print the total
print(total)
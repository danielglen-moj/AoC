# Load the input file
file = open("input.txt", "r")
lines = file.readlines()

# Functions
def is_number_difference(array, max_diff): 
    for i in range(len(array) - 1): 
        if abs(array[i] - array[i + 1]) > max_diff: 
            print("Diff Not Safe") 
            return False 
    print("Diff Safe") 
    return True


def is_increase_or_decrease(array):
    status = None  # Initialize status as None
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            new_status = "Decrease"
        elif array[i] < array[i + 1]:
            new_status = "Increase"
        else:
            new_status = "Equal"
            print("Inc/Dec Not Safe")
            return False

        # Check if status has changed
        if status is not None and new_status != status:
            print("Inc/Dec Not Safe")
            return False

        status = new_status  # Update status
    print("Inc/Dec Safe")
    return True

def is_safe_with_dampener(array, max_diff): 
    if is_number_difference(array, max_diff) and is_increase_or_decrease(array): 
        return True 
    
    for i in range(len(array)):
        modified_array = array[:i] + array[i+1:] 
        if is_number_difference(modified_array, max_diff) and is_increase_or_decrease(modified_array):
            return True 
        
    return False

# Initialise the total
total = 0

for line in lines:
    array = (line.split(" "))
    int_array = [int(number) for number in array]
    if is_safe_with_dampener(int_array, 3): 
        total += 1 
        print("Overall Safe") 
    else: 
        print("Overall Not Safe") 
    print("--------------------")

print(total)

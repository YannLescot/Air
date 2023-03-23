import sys

# Function to move first argument in last index
def to_left(argument):
    new_string = []
    changed_word = []
    for index, word in enumerate(argument):
        if index != 0:
            new_string.append(word)
        else:
            changed_word = word
    new_string.append(changed_word)
    return new_string

def try_except():
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two arguments.")
        sys.exit()
    try:
        argument = sys.argv[1:]
    except ValueError:
        print("Invalid input. Please provide only string, no integers.")
        sys.exit()
    return argument

# Function to print out without bracket and ","
def without_bracket(new_string):
    for i in range(len(new_string)):
        print(new_string[i], end=" ")
    print()

# Convert globales variables
argument = try_except()
new_string = to_left(argument)

# Print out result
without_bracket(new_string)
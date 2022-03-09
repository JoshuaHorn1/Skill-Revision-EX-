"""Program for @home learning  - version 1
Created by Joshua Horn
10th March 2022
"""

# Ask user for name
name = input("What is your name? ").capitalize()  # capitalizes the first letter of the user's name

# Ask user for 2 numbers
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

# Add numbers together
answer = num_1 + num_2

# Multiply numbers together

# Greet user and display result
print("\nHello", name) # starts output on new line

print(f"{num_1} + {num_2} = {answer}".format(num_1, num_2, answer))  # prints the answer

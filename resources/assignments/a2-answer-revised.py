#        Name: Jordan Crouser
#    Filename: a2-answer.py
#        Date: 15 Sept 2018
# Description: Sample solution for A2: Clunky Calculator

# Get user-entered numbers
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

# Get operation
operation = input("Enter the operation (+, -, *, /, **, or //): ")

# Initialize variables to hold answer/remainder
answer = None
remainder = None

# Perform selected operation
if operation == "+":
    answer = num1 + num2
elif operation == "-":
    answer = num1 - num2
elif operation == "*":
    answer = num1 * num2
elif operation == "/":
    answer = num1 / num2
elif operation == "**":
    answer = num1 ** num2
elif operation == "//":
    answer = num1 // num2
    remainder = num1 % num2

# Print results    
print("The answer is:", str(answer))
if (remainder):
    print("The remainder is:", str(remainder))

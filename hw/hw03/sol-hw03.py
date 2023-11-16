#################################################
#
# Ab Mosca
#
# 09.20.2023
#
# Clunky calculator that takes in 2 numbers, an 
# operation, and returns the result with details. 
#################################################

# First, gather input
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /, **, or //): ")

# Next, determine the operation 
if (op == "+"):
  ans = num1 + num2
elif (op == "-"):
  ans = num1 - num2
elif (op == "*"):
  ans = num1 * num2
elif (op == "/"):
  ans = num1 / num2
elif (op == "//"):
  ans = num1 // num2
else: #op == "**"
  ans = num1 ** num2

# Determine message
if (abs(ans) < 100):
  if (ans < 0):
    txt = "The answer is small and negative! It is"
  elif (ans > 0):
    txt = "The answer is small and positive! It is"
  else: # zero 
    txt = "The answer is small! It is"
else: #big 
  if (ans < 0):
    txt = "The answer is big and negative! It is"
  elif (ans > 0):
    txt = "The answer is big and positive! It is"
  else: # zero 
    txt = "The answer is big! It is"   

# Print output 
print(txt, ans)
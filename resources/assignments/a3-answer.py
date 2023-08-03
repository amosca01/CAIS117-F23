#        Name: Jordan Crouser
#    Filename: a3-answer.py
#        Date: 23 Sept 2018
# Description: Sample solution for A3: Copycat

user_input = input("Enter a sentence: ")

# 0. Exact copy
print("0. " + user_input)

# 1. CAPITALS and lowercase
print("1a. " + user_input.upper())
print("1b. " + user_input.lower())

# 2. Double vowels
#    (since they haven't formally seen loops,
#     its also fine if they do one at a time)
doubled = user_input
for vowel in ["a", "e", "i", "o", "u"]:
    doubled = doubled.replace(vowel, vowel*2)
print("2. " + doubled)

# 3. Abbreviate:
#    (print just the first 5 letters,
#     followed by ...,
#     followed by the last 5 letters)
if (len(user_input) > 10):
    print("3. " + user_input[:5] + "..." + user_input[-5:])
else:
    print("3. " + user_input) # No abbreviation necessary
    
# 4. Capitalize each word
capitalized = ""
for word in user_input.split():
    capitalized += word.capitalize() + " "
print("4. " + capitalized)

# 5. Reverse
print("5. " + user_input[::-1]) # Could also be done with a loop

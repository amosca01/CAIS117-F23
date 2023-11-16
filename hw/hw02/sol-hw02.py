####################################################
## Ab Mosca
## 09.12.2023
## Mad Lib Game
####################################################

## Gather input
name = input("Welcome to Mad Libs! Enter your name: ")
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adj2 = input("Enter an adjective: ")
X = (" " + noun1)*3
month = input("Enter a month: ")
day = input("Enter a day: ")
year = input("Enter a year: ")
num = input("Enter a number: ")
Y = str(eval(num)*2)
food = input("Enter a food: ")
numPunc = eval(input("Enter a number: "))
punc = input("Enter a punctuation: ")*numPunc

## Print to the user
output = "Congrats " + name + "!\nYou’ve been invited to a " + adj1 + " party! The theme of the party is " + noun1 + ". Be sure to wear a " + adj2 + " costume that screams" + X + ". The party will be on " + month + " " + day + ", " + year + ". We expect " + num + " people, so please bring " + Y + " " + food + "s so that everyone can have some. We cannot wait to see you there" + punc 
  
print(output)




## 
## Ab Mosca
## 09.28.2023
##
## Copy Cat: This program takes a user string 
##            and modifies that string

import string

def main():

  # Get user sentence
  s = input("Enter a sentence: ")

  # print s
  print(s)

  # print all uppercase
  print(s.upper())

  # print all lowercase
  print(s.lower())

  # print doubled vowels
  s2 = s.replace("a", "aa")
  s2 = s2.replace("e", "ee")
  s2 = s2.replace("i", "ii")
  s2 = s2.replace("o", "oo")
  s2 = s2.replace("u", "uu")
  s2 = s2.replace("A", "AA")
  s2 = s2.replace("E", "EE")
  s2 = s2.replace("I", "II")
  s2 = s2.replace("O", "OO")
  s2 = s2.replace("U", "UU")
  print(s2)

  # print first and last 5 char
  first5 = s[0:6]
  last5 = s[-6:]
  s3 = first5 + "..." + last5
  print(s3)

  # print backwards
  print(s[::-1])

if __name__ == "__main__":
  main()
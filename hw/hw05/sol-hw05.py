## 
## Ab Mosca
## 10.03.2023
##
## Magic 8 Ball: This program simulates a magic
##                8 ball 

import random

def main():

  #Get user input
  q = input("Type a question: ")
  q = q.lower().strip()

  #Define possible answers
  answers = ["It is certain", 
            "It is decidedly so", 
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don’t count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"]

  # Play the game 
  while (q != "exit"):
    #answer randomly
    ans = random.choice(answers)
    print(ans)

    # check whether to continue 
    q = input("Type another question (EXIT to quit): ")
    q = q.lower().strip()

  # game is over 
  print("Thanks for playing!")

if __name__ == "__main__":
  main()
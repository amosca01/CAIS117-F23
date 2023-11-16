## 
## Ab Mosca
## 10.07.2023
##
## Sample solution for Encrypt-Decrypt, which takes
## a message and a cipher, and prints the encoding and
## decoding
 

def encode(m, c):
  '''
  parameters: string, string
  returns: string
  does: takes a message and cipher, returns message
        encoded according to cipher 
  '''
  
  m = m.lower()

  if c == "pig latin":
    encoded = ""
    
    # encode each word 
    words = m.split(" ")
    for word in words:
  
      # move first letter and add ay 
      new_word = word[1:] + word[0] + "ay"
  
      encoded += new_word + " "
  else:
    encoded = m[::-1]
    
  # capitalize and remove extra space 
  encoded = encoded.capitalize().strip()
  return encoded

def decode(m, c):
  '''
  parameters: string, string
  returns: string
  does: takes an encoded message and cipher, returns
        decoded message according to cipher 
  '''
  
  m = m.lower()

  if c == "pig latin": 
    decoded = ""
    
    # decipher  each word 
    words = m.split(" ")
    for word in words:
  
      # remove the "ay" and move last letter
      new_word = word[:-2]
      new_word = new_word[-1] + new_word[:-1]
  
      decoded+= new_word + " " 
  else:
    decoded = encoded = m[::-1]

  # capitalize and remove extra space 
  decoded = decoded.capitalize().strip()
  return decoded

def main():

  #get input 
  message = input("Enter a message: ").strip()
  cipher = input("Pig Latin or Reverse? ").lower().strip()

  #check input
  valid_inps = ["pig latin", "reverse"]
  if cipher not in valid_inps:
    print("Try again!")
    message = input("Enter a message: ")
    cipher = input("Pig Latin or Reverse? ").lower()
  
  #encode and decode 
  encoded = encode(message, cipher)
  print(encoded)
  decoded = decode(encoded, cipher)
  print(decoded)

if __name__ == "__main__":
  main()
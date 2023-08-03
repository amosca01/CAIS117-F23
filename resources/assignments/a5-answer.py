#        Name: Jordan Crouser
#    Filename: a5-answer.py
#        Date: 10 Oct 2018
# Description: Sample solution for A5: Encrypt/Decrypt

def encrypt(s):

    # Split sentence into words
    words = s.upper().split()

    # Create placeholder for encrypted sentence
    encrypted_s = ""

    # Loop over each word
    for word in words:

        # Figure out where to split
        split_position = 0
        for letter in range(len(word)):
            if word[letter] in "AEIOU":
                split_position = letter
                break

        # Swap beginning/end of word if appropriate, add suffix
        if split_position > 0:
            new_word = word[split_position:]+"*"+word[:split_position]+"AY"
        else:
            new_word = word + "*~WAY"

        # Append encrypted word to sentence
        encrypted_s += new_word + " "

    # Trim off trailing space and return
    return encrypted_s.strip()


def decrypt(s):

    # Split sentence into words
    words = s.upper().split()

    # Create placeholder for decrypted sentence
    decrypted_s = ""

    # Loop over each word
    for word in words:

        # Split on special character '*'
        pieces = word.split("*")

        # Replace suffixes as appropriate
        pieces[1] = pieces[1].replace("~WAY", "").replace("AY", "")

        # Flip and reassemble
        decrypted_s += pieces[1] + pieces[0] + " "

    # Trim off trailing space and return
    return decrypted_s.strip()    

def main():
    message = input("Enter a message: ")
    print(encrypt(message))
    print(decrypt(encrypt(message)))

if __name__ == "__main__":
    main()

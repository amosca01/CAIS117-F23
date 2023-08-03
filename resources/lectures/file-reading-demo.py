# -------------------------------------------------
#        Name: R. Jordan Crouser
#    Filename: file-reading-demo.py
#        Date: 5 July 2018
#
# Description: a simple demonstration of how to
#              read in a text file in Python
# -------------------------------------------------

def main():

    # Open file for reading
    infile = open("horizontal.txt", "r")

    # Open file for writing
    outfile = open("vertical.txt", "w")

    # Read the file and print its contents
    text = infile.read().split()

    for word in text:
        outfile.write(word + "\n")

    # Close the files
    infile.close()
    outfile.close()

main()

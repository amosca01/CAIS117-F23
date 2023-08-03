def main():

    # Open file
    file = open("test2.txt", "w")

    # Write to file
    for i in range(100):
        file.write("I want " + str(i) + " chicken nuggets" + "\n")

    # Close the cabinet
    file.close()

main()

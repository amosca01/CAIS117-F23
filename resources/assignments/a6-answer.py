# -------------------------------------------------
#        Name: R. JORDAN CROUSER
#    Filename: musicLibrary.py
#        Date: 15 OCTOBER 2018
#
# Description: Music Library Sample Solution
#              (practice with lists/dictionaries)
# -------------------------------------------------

import webbrowser

def welcome():
    print("                      _        _ _ _")                          
    print("                     (_)      | (_) |")                         
    print("  _ __ ___  _   _ ___ _  ___  | |_| |__  _ __ __ _ _ __ _   _ ")
    print(" | '_ ` _ \| | | / __| |/ __| | | | '_ \| '__/ _` | '__| | | |")
    print(" | | | | | | |_| \__ \ | (__  | | | |_) | | | (_| | |  | |_| |")
    print(" |_| |_| |_|\__,_|___/_|\___| |_|_|_.__/|_|  \__,_|_|   \__, |")
    print("                                                         __/ |")
    print("                                                        |___/") 

def addSong(library):
    song = {}
    song["title"] = input("Song title: ")
    song["artist"] = input("Artist: ")
    song["album"] = input("Album: ")
    song["url"] = input("Spotify URL: ")
    library.append(song)

def printSongs(library):
    counter = 0
    for song in library:
        counter += 1
        print(str(counter) + ". '" + song["title"] + "' by",
              song["artist"],
              "(" + song["album"] +")")

def removeSong(library, index):
    print("Removing song #" + str(index) +"...", end = "")
    library.pop(index - 1)
    print("DONE")

def playSong(library, index):
    print('In play')
    webbrowser.open(library[index - 1]["url"])

def printMenu():
    return input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
    
def main():
    welcome()
    library = []
    option = ""
    while option != "QUIT":
        option = printMenu()
        print()
        
        if option == "ADD":
            addSong(library)
            
        elif option == "REMOVE":
            index = int(input("Which # would you like to remove? "))
            removeSong(library, index)
            
        elif option == "PRINT":
            printSongs(library)
            
        elif option == "PLAY":
            index = int(input("Which # would you like to play? "))
            playSong(library, index)
            
        print()

    print("Goodbye!")

if __name__ == "__main__":
    main()

# ----------------------------------------------------
#       Names: <YOUR NAMES HERE>
#    Filename: connectFour-broken.py
#        Date: <TODAY'S DATE HERE>
#
# Description: This file contains a broken version
#              of Jordan's ConnectFour game.
#
#              There are 5 SYNTACTIC ERRORS (mistakes
#              that are not correct Python statements
#              and so cause the program to throw
#              Exceptions) as well as 5 LOGICAL ERRORS
#              (mistakes that are technically correct
#              Python statements, but which cause the
#              program not to behave the way we want).
#
#              Your job is to find (and correct!) each
#              of these mistakes using your new
#              DEBUGGING TECHNIQUES.
# ----------------------------------------------------

def printWelcome()
    print("+----------------+")
    print("|   welcome to   |")
    print("|  CONNECT FOUR  |")
    print("+----------------+")

def printWinner(player):
    print("+------------------+")
    print("| congratulations! |")
    print("|  PLAYER " + str(player) + " WINS!  |")
    print("+------------------+")
    
def getBoardSize():
    # Ask the user how big a board they want
    while true:
        try:
            n = input('Please enter a board size between 1 and 10: ')
        except ValueError:
            print('Invalid input: please enter a number')
            continue
        if n <= 0 or n>10:
            print('Invalid input: please enter a value between 1 and 10')
            continue
        break
    return n

def play():
    
    n = getBoardSize()

    print("\nGreat! Give me a moment to set up the board...\n")
    # Set up the board using a list of lists,
    # a 4x4 board would look like this:
    #    [[0,0,0,0],
    #     [0,0,0,0],
    #     [0,0,0,0],
    #     [0,0,0,0]]
    grids = [[0]*n for row in range(n)]

    # Start with Player 1
    player = 1

    # Print the board
    print('Current board:')
    print(grids)

    while True:
        slot = get_input(player, grids, n)
        place_piece(slot, player, grids)
        print('\nCurrent board:')
        print(grids)

        if (check_horizontal_win(grids, player, n) or
            check_diagonal_win(grids, player, n) or
            check_diagonal_win(grids[::-1], player, n)):
            printWinner(player)
            return

        # If no one has won yet, check if board is full:
        #  start by assuming that it is
        allFull = True
        for grid in grids:
            for cell in grid:
                # If we find an empty slot
                if cell = 0:
                    # The board isn't full
                    allFull = False

        # If we found no empty slots
        if allFull:
            print("STALEMATE - no winner.")
            return

        # Switch to the other player
        if (player == 1):
            player = 1
        else:
            player = 2


def get_input(player, grids, n):
    instructions = 'Player {0}: select a slot from 1 to {1}: '.format(player, n)
    while True:
        try:
            slot = int(input(instructions))
        except ValueError:
            print('Invalid input:', slot)
            continue
        if 0 > slot or slot > n+1:
            print('Invalid input:', slot)
        elif grids[0][slot-1] != 0:
            print('Slot', slot, 'is full, please try again.')
        else:
            return slot-1


def place_piece(slot, player, grids):

    # Loop through grids in reverse order
    # to simulate the piece "dropping" to
    # the lowest available row
    for grid in grids[::-1]:

        # As soon as we find an empty row
        if grid[slot] == 0:
            
            # Place the piece and exit
            grid[slot] = player
            return


def check_horizontal_win(grids, player, n):
    # Loop over each row
    for grid in grids:
        
        # Count up how many cells are claimed by player
        count_cells_claimed = 0
        for cell in grid:
            if (cell == player):
                count_cells_claimed += 1

        # If all the cells in the row are claimed by player
        if count_cells_claimed == n:
            # They won!
            return True
        
    # Loop finished, no winning rows found
    return False

check_vertical_win(grids, player, n):
    # Loop over each column
    for i in range(n):
        count_cells_claimed = 0
        for grid in grids:
            if grid[i] == player:
                count_cells_claimed += 1
                
        # If all the cells in the column are claimed by player
        if count_cells_claimed == n:
            # They won!
            return True


def check_diagonal_win(grids, player, n):

    # Check diagonal
    count_cells_claimed = 0
    for cell in range(n):
        if grids[cell][cell] == player:
            count_cells_claimed += 1
            
    # If all the cells in the diagonal are claimed by player
    if count_cells_claimed == n:
        return True

    # No diagonal win detected
    return False


def main():
    printWelcome()
    play()

zz = []
p1go = True
w = False

def su():
    for x in range(0, 9):
        zz.append(str(x + 1))
    
def pb():
    print( '-------')
    print( '-------')
    print( ' ' + zz[0] + '|' + zz[1] + '|' + zz[2])
    print( '--+-+--')
    print( ' ' + zz[3] + '|' + zz[4] + '|' + zz[5])
    print( '--+-+--')
    print( ' ' + zz[6] + '|' + zz[7] + '|' + zz[8])
    print( '-------')
    print( '-------')

def cw():
    if((zz[0] == zz[4] and
        zz[0] == zz[8]) or 
       (zz[2] == zz[4] and
        zz[4] == zz[6])):
        w = True
        pb()

su()
while not w:
    pb()

    if p1go:
        print( "Player 1, select spot:")
    else:
        print( "Player 2, select spot:")

    try:
        y = int(input(">> "))
    except:
        print("Please enter a valid slot")
        continue
    if zz[y - 1] == 'X' or zz [y-1] == 'O':
        print("Illegal move, please try again")
        continue

    if p1go:
        zz[y - 1] = 'X'
    else:
        zz[y - 1] = 'O'

    p1go = not p1go

    for x in range (0,3) :
        y = x * 3
        if (zz[y] == zz[(y + 1)] and
            zz[y] == zz[(y + 2)]):
            w = True
            pb()
        if (zz[x] == zz[(x + 3)] and
            zz[x] == zz[(x + 6)]):
            w = True
            pb()

    cw()

print ("Player " + str(int(p1go + 1)) + " wins!\n")

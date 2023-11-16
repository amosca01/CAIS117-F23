from graphics import *

def main():
    win = GraphWin("CSC111 Animated Ball", 600, 400)
    circ = Circle(Point(50,50), 10)
    circ.setFill( 'red' )
    circ.draw(win)
    
    # set initial direction of ball
    dx = 1.5
    dy = 0.25

    # move ball on screen
    while win.checkMouse() == None:
        circ.move( dx, dy )

        x = circ.getCenter().getX()
        y = circ.getCenter().getY()

        if x < 5:
            dx = -dx
        elif x > 595:
            dx = -dx
        if y < 5:
            dy = -dy
        elif y > 395:
            dy = -dy 

        
        
    win.close() # Close window when done

main()

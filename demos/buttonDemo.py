from graphics import *

class Button(Rectangle):

    def onClick(self):
        print("Button was clicked!")
        

def main():

    # Set up the window, draw a button
    win = GraphWin("Button Demo", 400, 400)
    btn = Button(Point(150,150), Point(250,250))
    btn.draw(win)

    # Continue to loop until the user presses q
    while win.checkKey() != "q":

        # Check to see if user clicked somewhere
        mousePt = win.checkMouse()
        if mousePt is not None:

            # Check if their click was within the x range of the button
            if btn.getP1().getX() < mousePt.getX() < btn.getP2().getX():

                # Check if their click was within the y range of the button
                if btn.getP1().getY() < mousePt.getY() < btn.getP2().getY():
                    print("Button clicked at", mousePt)


if __name__ == "__main__":
    main()

    

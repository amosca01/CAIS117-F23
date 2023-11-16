# aquarium.py
# Your name here
#
# A module containing the definition for a graphic fish with
# an oval body, tail, and circle eye.

from graphics import *
from random import randint

WIDTH = 800
HEIGHT = 450

class Fish:
    """Definition for a fish with a body, eye, and tail"""
    def __init__(self, win, position):
        """constructs a fish made of 1 oval centered at `position`,
           a second oval for the tail, and a circle for the eye"""
        
        self.position = position

        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)

        # body is an oval
        p1 = Point(position.getX()-40, position.getY()-20)
        p2 = Point(position.getX()+40, position.getY()+20)
        self.body = Oval( p1, p2 )
        self.body.setFill(color_rgb(red, green, blue))

        # tail is another oval
        p1 = Point(position.getX()+30, position.getY()-30)
        p2 = Point(position.getX()+50, position.getY()+30)
        self.tail = Oval( p1, p2 )
        self.tail.setFill( "black" )

        # eye
        center2 = Point( position.getX()-15, position.getY()-5 )
        self.eye = Circle( center2, 5 )
        self.eye.setFill( "black" )

        # Initially facing left, moving slowly
        self.dx = -3
        self.dy = -1

    def draw( self, win ):
        """draw the fish to the window"""
        self.body.draw( win )
        self.tail.draw( win )
        self.eye.draw( win )

    def move( self ):
        """move the fish by dx"""
        self.body.move( self.dx, self.dy )
        self.tail.move( self.dx, self.dy )
        self.eye.move( self.dx, self.dy )

        # If fish swims off the screen to the left or right
        if self.body.getP2().getX() < -50 or self.body.getP1().getX() > WIDTH + 50:
            self.flip()
            # Reverse direction, keep same speed
            self.dx = -self.dx

        # If the fish hits the top or bottom
        if self.body.getP1().getY() < 0 or self.body.getP2().getY() > HEIGHT:
            self.dy = -self.dy

        # 5% chance: randomly switch going up/down
        switch = randint(1, 20)
        if (switch == 1):
            self.dy = -self.dy

    def flip( self ):
        # If facing left, turn right
        if (self.dx < 0):
            self.eye.move(30, 0)
            self.tail.move(-80, 0)

        # If facing right, turn left
        else:
            self.eye.move(-30, 0)
            self.tail.move(80, 0)

def main():

    # open a graphic window
    win = GraphWin( "Fish", WIDTH, HEIGHT )

    # draw the background
    bg = Image(Point(WIDTH/2, HEIGHT/2), "aquarium_bg.gif")
    bg.draw(win)
    
    # empty list to hold fish
    fishies = []
    clickedPt = None

    # keep going until the user clicks
    while True:

        clickedPt = win.checkMouse()
        if clickedPt != None:
            newFish = Fish( win, clickedPt)
            fishies.append(newFish)
            newFish.draw(win)
            clickedPt = None
            
        for fish in fishies:
            fish.move()

    win.close()
main()

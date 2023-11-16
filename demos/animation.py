from graphics import *
def main():
  win = GraphWin("My Circle", 600, 400)
  c = Circle(Point(50,50), 10)
  c.draw(win)
  for i in range(150):
    c.move(3,2) # The move function takes two values, dx and dy
  win.getMouse() # Pause to view result
  win.close() # Close window when done
main()

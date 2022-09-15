#USE THIS IN FULL SCREEN
import sys, os
import curses
from curses import wrapper
from curses.textpad import rectangle

#initiate curses function wrapper
def main(screen):

    # initite colors with limited color attributes
    # with id, color 1, color 2
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)

    ymax, xmax = screen.getmaxyx() # get the max y and x value of the terminal window

    # messages printed to the curses screen 
    # using addstr(y_cord, x_cord, string)
    screen.addstr(int(ymax / 2) - 10, int(xmax / 4), "---- this is an example of text on a screen ----\n\n")
    screen.addstr(int(ymax / 2) + -9, int(xmax / 4),"---- blue text on yellow backgound! ----\n\n", curses.color_pair(1))
    screen.addstr(int(ymax / 2) + -8, int(xmax / 4),"I'm a char:\n\n")
    screen.addch( int(ymax / 2) + -7, int(xmax / 4),'z')
    screen.addstr(int(ymax / 2) + -6, int(xmax / 4),"---- rectangle: ----\n")

    # rectangle with upper left hand corner coordinates and lower right hand corner coordinites
    # as parameters
    rectangle(screen, int(ymax / 2) - 5, int(xmax / 4), int(ymax / 2) - 2, int(xmax / 2))

    # obtaining user input using function getkey()
    screen.addstr(int(ymax / 2) -  1, int(xmax / 4),"---- user input/output: ----\n")
    k = screen.getkey()
    screen.addstr(int(ymax / 2), int(xmax / 4),f"---- your key: {k} ----\n")
    
    # refresh screen to show data drawn on it
    screen.refresh()

    #get a key to exit the screen
    screen.getch()

  

wrapper(main) 

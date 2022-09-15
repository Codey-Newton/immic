import curses
from curses import wrapper
import time
import random

def main(stdscr):
    # Get screen size
    height, width = stdscr.getmaxyx()

    # Declare colors
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    WHITE = curses.color_pair(1)
    BLUE = curses.color_pair(2)
    GREEN = curses.color_pair(3)

    # Some initilizations
    color = WHITE
    cont = False

    # While input is incorrect, ask again
    while(cont == False):
        stdscr.addstr("Please choose a color\nb = blue, g = green, w = white\n")
        char = stdscr.getkey()
        stdscr.clear()
        if char == 'b':
            color = BLUE
            cont = True
        elif char == 'g':
            color = GREEN
            cont = True
        elif char == 'w':
            color = WHITE
            cont = True
        else:
            stdscr.addstr("You entered an improper key, try again.\n")
    stdscr.clear()

    # Print random squares of chosen color on the screen.
    for i in range(150):
        screenclr = random.randint(0,15)
        # Clear screen randomly
        if screenclr == 5:
            stdscr.clear()
        rand = random.randint(0, height-2)
        rand2 = random.randint(0, width-1)
        stdscr.addstr(rand, rand2, "  ", color)
        stdscr.refresh()
        time.sleep(0.1)
    # Exit program condition
    stdscr.addstr(height-2, 0, "Press any key to exit. ")
    stdscr.getch()


wrapper(main)

import sys,os
import curses


def print_pause_menu(stdscr):

    #array with
    menu = ['Resume', 'Save', 'Home', 'Settings', 'Exit']

    #clear and refresh screen
    stdscr.clear()
    stdscr.refresh()

    #sets the cursor to be at the top left of the screen
    curses.curs_set(0)

    current_row = 0;

    # set the attibute.
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    while 1:

        # get condinates for center of screen
        h, w = stdscr.getmaxyx()
        # get y based on # of items in array and x based on
        # letters in each item in array.
        for i, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + i
            if i == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        #gets key from user
        k = stdscr.getch()
        if k == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif k == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif k == k in [10, 13]:
            if current_row == len(menu)-1:
                break
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row]))
            stdscr.refresh()
            stdscr.getch()

        stdscr.clear()

def main():
    curses.wrapper(print_pause_menu)

if __name__ == "__main__":
    main()

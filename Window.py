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
            if current_row == len(menu)-5:
                curses.wrapper(divide_screen)
                break
            #elif current_row == len(menu)-4:
                #curses.wrapper(save_data)
                #break
            #elif current_row == len(menu)-3:
                #curses.wrapper(start_menu)
                #break
            #elif current_row == len(menu)-2:
                #curses.wrapper(settings_menu)
                #break
            elif current_row == len(menu)-1:
                break
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row]))
            stdscr.refresh()
            stdscr.getch()

            stdscr.clear()



def divide_screen(stdscr):

    stdscr.clear()
    stdscr.refresh()
    end = 0
    h, w = stdscr.getmaxyx()

    character_win = curses.newwin(h, w//4, 0, 0)
    story_win = curses.newwin(h//2, w//2+27, 0, w//4+3)
    choices_win = curses.newwin(h//2, w//2+27, h//2, w//4+3)
    while 1:

        character_win.clear()
        story_win.clear()
        choices_win.clear()
        character_win.addstr("Hello World!000000000000000000000000000000000000000000000000000000000")
        story_win.addstr("Hello World!0000000000000000000000000000000000000000000000000000000000000000000000000000000")
        choices_win.addstr("Hello World!0000000000000000000000000000000000000000000000000000000000000000000000000000000")
        story_win.refresh()
        choices_win.refresh()
        character_win.refresh()
        k = stdscr.getch()
        if k == 27:
            curses.wrapper(print_pause_menu)
            break
        if k == curses.KEY_UP:
            break



def main():
    curses.wrapper(divide_screen)


if __name__ == "__main__":
    main()


# height = 30
# width = 120

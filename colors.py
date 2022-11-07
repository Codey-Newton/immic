import curses
dialog  = 0
options = 0
boarder = 0
picture = 0
def terminal_colors():
    def main(stdscr):
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)
        stdscr.addstr(0, 0, '{0} colors available'.format(curses.COLORS))
        maxy, maxx = stdscr.getmaxyx()
        maxx = maxx - maxx % 5
        x = 0
        y = 1
        try:
            for i in range(0, curses.COLORS):
                stdscr.addstr(y, x, '{0:5}'.format(i), curses.color_pair(i))
                x = (x + 5) % maxx
                if x == 0:
                    y += 1
        except curses.ERR:
            pass
        stdscr.getch()
        exit(0) 
    curses.wrapper(main)
    
# gives the game color
def scene_colors(story: dict, curr_scene: int):
    if 'color_dialog' in story['adventure']['scene'][curr_scene]:
        color_list[0] = int(story['adventure']['scene'][curr_scene]['color_dialog'])
    elif 'color_options' in story['adventure']['scene'][curr_scene]:
        color_list[1] = int(story['adventure']['scene'][curr_scene]['color_options'])
    elif 'color_boarder' in story['adventure']['scene'][curr_scene]:
        color_list[2] = int(story['adventure']['scene'][curr_scene]['color_boarder'])
    elif 'color_boarder' in story['adventure']['scene'][curr_scene]:
        color_list[3] = int(story['adventure']['scene'][curr_scene]['color_boarder'])    
    else:
        return

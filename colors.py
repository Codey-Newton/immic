import curses
import ascii_magic

# print available terminal colors
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
    
# returns a color list holding all available colors
# in a scene.
def scene_colors(story: dict, curr_scene: int):
    dialog = 0
    options = 0
    boarder = 0
    picColor = 0
    color_list = [ ]
    if 'color_dialog' in story['adventure']['scene'][curr_scene]:
        #print("you have dialog color: ", int(story['adventure']['scene'][curr_scene]['color_dialog']))
        dialog = int(story['adventure']['scene'][curr_scene]['color_dialog'])
    if 'color_options' in story['adventure']['scene'][curr_scene]:
        options = int(story['adventure']['scene'][curr_scene]['color_options'])
    if 'color_boarder' in story['adventure']['scene'][curr_scene]:
        boarder = int(story['adventure']['scene'][curr_scene]['color_boarder'])
    if 'picColor' in story['adventure']['scene'][curr_scene]:
        picColor = int(story['adventure']['scene'][curr_scene]['picColor'])    
    
    color_list = [dialog, options, boarder, picColor]
   
    return color_list

 # takes a image and converts it to ascii art 80 characters wide       
def a_picture(picture: str, col=55):
    tmp_pic = ascii_magic.from_image_file(
        picture, mode = ascii_magic.Modes.ASCII, columns=col)
    return tmp_pic

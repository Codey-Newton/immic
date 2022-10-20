import sys,os
import curses
import xmltodict
import re
import time,random

Line= "HELOOOO"
Options = []
Input = 999

def print_pause_menu(stdscr):

    #array with
    menu = ['Resume', 'Save', 'Load', 'Home', 'Exit']

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
                #curses.wrapper(load_menu)
                #break
            #elif current_row == len(menu)-2:
                #curses.wrapper(start_menu)
                #break
            elif current_row == len(menu)-1:
                exit()
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row]))
            stdscr.refresh()
            stdscr.getch()

            stdscr.clear()



def divide_screen(stdscr):

    global Input
    stdscr.clear()
    stdscr.refresh()
    end = 0
    h, w = stdscr.getmaxyx()

    character_win = curses.newwin(h, w//4, 0, 0)
    story_win = curses.newwin(h//2-1, w//2+27, 0, w//4+3)
    choices_win = curses.newwin(h//2-1, w//2+27, h//2+1, w//4+3)
    border_win = curses.newwin(h, 3, 0, w//4)
    border2_win = curses.newwin(3, w//2+27, h//2-1, w//4+2)
    while 1:

        border_win.clear()
        border2_win.clear()
        character_win.clear()
        story_win.clear()
        #choices_win.clear()
        for i in range(h):
            border_win.addstr(i, 0,"||")
        for i in range(87):
            border2_win.addstr(0, i,"_")
        character_win.addstr("HELOOOOOOOOOOOOOOOOOOOO")
        story_win.addstr(3, 8, Line)
        if len(Options) == 1:
            choices_win.addstr(2, 8, Options[0])
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            stdscr.move(26, 40)
            k = stdscr.getch()

            if k == 27:
                print_pause_menu(stdscr)
                break
            if k == 48:
                choices_win.addstr(10, 8, chr(k))
                choices_win.refresh()
                time.sleep(1)
                Input = k - 48
                break
            else:
                choices_win.addstr(10, 8, chr(k))
                choices_win.addstr(10, 12, "Invalid input. Only 0 is valid")
        if len(Options) == 2:
            choices_win.addstr(2, 8, Options[0])
            choices_win.addstr("\n")
            choices_win.addstr(4, 8, Options[1])
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            stdscr.move(26, 40)
            k = stdscr.getch()
            if k == 27:
                print_pause_menu(stdscr)
                break
            if k == 48 or k == 49:
                choices_win.addstr(10, 8, chr(k))
                choices_win.refresh()
                time.sleep(1)
                if k == 48:
                    Input = k - 48
                elif k == 49:
                    Input = k - 49
                break
            else:
                choices_win.addstr(10, 8, chr(k))
                choices_win.addstr(10, 12, "Invalid input. Only numbers [0, 1] are valid")
        if len(Options) == 3:
            choices_win.addstr(2, 8, Options[0])
            choices_win.addstr("\n")
            choices_win.addstr(4, 8, Options[1])
            choices_win.addstr("\n")
            choices_win.addstr(6, 8, Options[2])
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            stdscr.move(26, 40)
            k = stdscr.getch()
            if k == 27:
                print_pause_menu(stdscr)
                break
            if k == 48 or k == 49 or k == 50:
                choices_win.addstr(10, 8, chr(k))
                choices_win.refresh()
                time.sleep(1)
                if k == 48:
                    Input = k - 48
                elif k == 49:
                    Input = k - 48
                elif k == 50:
                    Input = k - 48
                break
            else:
                choices_win.addstr(10, 8, chr(k))
                choices_win.addstr(10, 12, "Invalid input. Only numbers [0, 1, 2] are valid ")
        if len(Options) == 4:
            choices_win.addstr(2, 8, Options[0])
            choices_win.addstr("\n")
            choices_win.addstr(4, 8, Options[1])
            choices_win.addstr("\n")
            choices_win.addstr(6, 8, Options[2])
            choices_win.addstr("\n")
            choices_win.addstr(8, 8, Options[3])
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            stdscr.move(26, 40)
            k = stdscr.getch()

            if k == 27:
                print_pause_menu(stdscr)
                break
            if k == 48 or k == 49 or k == 50 or k == 51:
                choices_win.addstr(10, 8, chr(k))
                choices_win.refresh()
                time.sleep(1)
                if k == 48:
                    Input = k - 48
                elif k == 49:
                    Input = k - 48
                elif k == 50:
                    Input = k - 48
                elif k == 51:
                    Input = k - 48
                break
            else:
                choices_win.addstr(10, 8, chr(k))
                choices_win.addstr(10, 12, "Invalid input. Only numbers [0, 1, 2, 3] are valid")



#######################################################################################

def display_scene_text(dialog: str):
  global Line
  Line = dialog
  #print("\n")

#checks to see if your input is in the valid_inputs list
def get_input(valid_input: list):

  while True:
    curses.wrapper(divide_screen)
    user_entered = str(Input)
    if user_entered not in valid_input:
      #print("Invalid input. Please use one of the following inputs:\n")
      #print(valid_input)
      user_entered = None
    else:
      return user_entered

def get_response(story: dict, curr_scene: int):

    global Options
    Options.clear()
    # if there are more than 4 options, its actually a single option,
    # but it counts the individual characters.
    # Or in another way, there are 4 options max
    if(len(story['adventure']['scene'][curr_scene]['options']) > 4):

        Options.append((str(0) + ". " + story['adventure']['scene'][curr_scene]['options']))
        #curses.wrapper(divide_screen, options)
        valid_inputs = [str(num) for num in range(1)]
        option_index = int(get_input(valid_inputs))

        # parse the option string using re's to find integers contained
        # in [ ], (must be integers in [ ]).
        # and save the value in a variable.
        # N: use re library thats built in to python
        scene_jump_match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", string = story['adventure']['scene'][curr_scene]['options'])
        #print(scene_jump_match.group())

    # do everything above exept with more than one option
    else:
      for i in range(len(story['adventure']['scene'][curr_scene]['options'])):
        Options.append((str(i) + ". " + story['adventure']['scene'][curr_scene]['options'][i]))
      valid_inputs = [str(num) for num in range(len(story['adventure']['scene'][curr_scene]['options']))]
      #print(valid_inputs)
      option_index = int(get_input(valid_inputs))
      #print(option_index)
      scene_jump_match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", string = story['adventure']['scene'][curr_scene]['options'][option_index])
      #print(scene_jump_match.group())


    return int(scene_jump_match.group())



def story_flow(story: dict):
  curr_scene = 0

  while curr_scene != None:
    scene = story['adventure']['scene'][curr_scene]

    if scene == None:
      curr_scene = None
      break

    display_scene_text(story['adventure']['scene'][curr_scene]['dialog'])

    # if a option contains nothing, or returns None, break form the loop.
    if story['adventure']['scene'][curr_scene]['options'] == None:
      curr_scene = None
      break

    curr_scene = get_response(story, curr_scene)






def main():
      # Open the file and read the contents into my_xml
      # arg1: file name, arg2: r(read), arg3: encoding type
    with open('debugAdventure.xml', 'r', encoding='utf-8') as file:
        my_xml = file.read()

      # Use xmltodict to parse and convert
      # the XML document
    story = xmltodict.parse(my_xml, namespace_separator=True)
    story_flow(story)
    #strings = "HELOO!"
    #curses.wrapper(divide_screen, strings)


if __name__ == "__main__":
    main()


# height = 30
# width = 120

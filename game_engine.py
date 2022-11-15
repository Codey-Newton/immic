import sys,os
from pathlib import Path
import curses
import xmltodict
import re
import time
import character as ch
import colors
import story_scheme
import pickle
#--------------------------------------------------------
# global variables
#--------------------------------------------------------
title_pic = ""
save_name = "immic"
title_pic_color = 0
menu_color = 80
Picture = ""
Line= "HELOOOO"
Options = []
Input = 999
Player = ch.Character()
color_listG = [0,0,0,0]
##########################################################

#----------------------------------------------------------
# pause screen + screen boxes                             |
#----------------------------------------------------------,
def title_screen(stdscr):

        global Player
        menu = ['Start Game', 'Load Game', 'Exit']

        #clear and refresh screen
        stdscr.clear()
        stdscr.refresh()

        #sets the cursor to be at the top left of the screen
        curses.curs_set(0)

        current_row = 0

        # get condinates for center of screen
        h, w = stdscr.getmaxyx()

        # set the attibute.
         # initiate colors
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)
        title_win = curses.newwin(100 , 180, h//2 - 21, w//2 - 35)

        title = colors.a_picture(title_pic, 155)

        while 1:

            title_win.clear()

            title_win.addstr(title, curses.color_pair(title_pic_color))

            title_win.refresh()
            # get y based on # of items in array and x based on
            # letters in each item in array.
            for i, row in enumerate(menu):
                x = w//2 - len(row)//2
                y = h//2 - len(menu)//2 + i
                if i == current_row:
                    stdscr.attron(curses.color_pair(menu_color))
                    stdscr.addstr(y, x, row)
                    stdscr.attroff(curses.color_pair(menu_color))
                else:
                    stdscr.addstr(y, x, row)
            #gets key from user
            k = stdscr.getch()
            if k == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif k == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif k == k in [10, 13]:
                if current_row == len(menu)-3:
                    curses.wrapper(main)
                    break
                elif current_row == len(menu)-2:
                    Player = load_story(Player)
                    curses.wrapper(main)
                    break
                elif current_row == len(menu)-1:
                    exit()
                stdscr.clear()
                stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row]))
                stdscr.refresh()
                stdscr.getch()

                stdscr.clear()

def print_pause_menu(stdscr):
    global Player
    #array with
    menu = ['Resume', 'Save', 'Exit']

    #clear and refresh screen
    stdscr.clear()
    stdscr.refresh()

    #sets the cursor to be at the top left of the screen
    curses.curs_set(0)

    current_row = 0

    # set the attibute.
    # initiate colors
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    while 1:

        # get condinates for center of screen
        h, w = stdscr.getmaxyx()
        # get y based on # of items in array and x based on
        # letters in each item in array.
        for i, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + i
            if i == current_row:
                stdscr.attron(curses.color_pair(menu_color))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(menu_color))
            else:
                stdscr.addstr(y, x, row)
        #gets key from user
        k = stdscr.getch()
        if k == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif k == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif k == k in [10, 13]:
            if current_row == len(menu)-3:
                curses.wrapper(divide_screen)
                break
            elif current_row == len(menu)-2:
                save_story(Player)
                curses.wrapper(divide_screen)
                break
            elif current_row == len(menu)-1:
                exit()
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row]))
            stdscr.refresh()
            stdscr.getch()

            stdscr.clear()

def divide_screen(stdscr):
    global Input, color_listG, Picture
    characterpic = """\
            /////\\
            |O O ||
            |/   @|
             \-_//
            __| |__
          .'       `.
          |         |
          | |     | |
          | |     | |
          | |     | |
          |_|     |_|
          \/|_____|\/
            |  |  |
            |  |  |
            |  |  |
            |  |  |
            |  |  |
            |  |  |
           _|__|__|
          (__(____] """
    stdscr.clear()
    stdscr.refresh()
    end = 0
    h, w = stdscr.getmaxyx()

    picture_win = curses.newwin(h//2-3, w//4-4, 2, 4)
    character_win = curses.newwin(h//2-1, w//4-8, h//2+1, 8)
    story_win = curses.newwin(h//2-1, w//2+20, 0, w//4+3)
    choices_win = curses.newwin(h//2-1, w//2+47, h//2+1, w//4+3)
    border_win = curses.newwin(h, 3, 0, w//4)
    border2_win = curses.newwin(1, w, h//2-1, 0)
    while 1:

        border_win.clear()
        border2_win.clear()
        character_win.clear()
        story_win.clear()
        picture_win.clear()
        picture_win.addstr(Picture, curses.color_pair(color_listG[3])) 
        for i in range(h):
            border_win.addstr(i, 0,"||", curses.color_pair(color_listG[2]))
        for i in range(w-1):
            border2_win.addstr(0, i,"_", curses.color_pair(color_listG[2]))
        character_win.addstr(characterpic)
        character_win.addstr("\n")
        character_win.addstr("\n")
        character_win.addstr("Character Name = ")
        character_win.addstr(Player.name)
        character_win.addstr("\n")
        character_win.addstr("Agile = ")
        character_win.addstr(str(Player.Agile[1]))
        character_win.addstr("\n")
        character_win.addstr("Brain = ")
        character_win.addstr(str(Player.Brain[1]))
        character_win.addstr("\n")
        character_win.addstr("Charm = ")
        character_win.addstr(str(Player.Charm[1]))
        character_win.addstr("\n")
        character_win.addstr("Detect = ")
        character_win.addstr(str(Player.Detect[1]))
        character_win.addstr("\n")
        character_win.addstr("Endure = ")
        character_win.addstr(str(Player.Endure[1]))
        character_win.addstr("\n")
        story_win.addstr(3, 8, Line, curses.color_pair(color_listG[0]))
        if len(Options) == 1:
            choices_win.addstr(2, 8, Options[0], curses.color_pair(color_listG[1]))
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            picture_win.refresh()
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
            choices_win.addstr(2, 8, Options[0], curses.color_pair(color_listG[1]))
            choices_win.addstr("\n")
            choices_win.addstr(4, 8, Options[1], curses.color_pair(color_listG[1]))
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            picture_win.refresh()
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
                    Input = k - 48
                break
            else:
                choices_win.addstr(10, 8, chr(k))
                choices_win.addstr(10, 12, "Invalid input. Only numbers [0, 1] are valid")
        if len(Options) == 3:
            choices_win.addstr(2, 8, Options[0], curses.color_pair(color_listG[1]))
            choices_win.addstr("\n")
            choices_win.addstr(4, 8, Options[1], curses.color_pair(color_listG[1]))
            choices_win.addstr("\n")
            choices_win.addstr(6, 8, Options[2], curses.color_pair(color_listG[1]))
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            picture_win.refresh()
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
            choices_win.addstr(2, 8, Options[0], curses.color_pair(color_listG[1]))
            choices_win.addstr("\n")
            choices_win.addstr(4, 8, Options[1], curses.color_pair(color_listG[1]))
            choices_win.addstr("\n")
            choices_win.addstr(6, 8, Options[2], curses.color_pair(color_listG[1]))
            choices_win.addstr("\n")
            choices_win.addstr(8, 8, Options[3], curses.color_pair(color_listG[1]))
            border_win.refresh()
            border2_win.refresh()
            story_win.refresh()
            choices_win.refresh()
            character_win.refresh()
            picture_win.refresh()
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

#-----------------------------------------------------
# main story functions                               |
#-----------------------------------------------------

'''def display_scene_text(dialog: str):
  global Line
  Line = dialog'''
  
def save_story(Player:ch.Character):
    path = Path(f"./saves_immic/{save_name}")
    if path.is_file():
        os.remove(f"./saves_immic/{save_name}")
        
    with open(f"./saves_immic/{save_name}", 'wb') as f:
        pickle.dump(Player, f)

def load_story(Player:ch.Character):
    try:
        with open(f"./saves_immic/{save_name}", 'rb') as f:
            Player = pickle.load(f)

    except FileNotFoundError:
        exit("save file not found!!!")
        
    else:
        return Player
    
# checks to see if your input is in the valid_inputs list
def get_input(valid_input: list):

  while True:
    curses.wrapper(divide_screen)
    user_entered = str(Input)
    if user_entered not in valid_input:
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
        scene_jump_match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", \
        string = story['adventure']['scene'][curr_scene]['options'])

        parse_check = re.search(pattern = "(?<=\{)[A-E] [0-9] [0-9]+(?=\})", \
        string = story['adventure']['scene'][curr_scene]['options'])
        
        if parse_check != None:

            skill_list = parse_check[0].split()
            skill_check = Player.skill_check(skill_list)
        
            if skill_check == 'F':
                return int(scene_jump_match.group())
            else:
                return int(skill_check)

    # do everything above exept with more than one option
    else:
        for i in range(len(story['adventure']['scene'][curr_scene]['options'])):
          Options.append((str(i) + ". " + story['adventure']['scene'][curr_scene]['options'][i]))

        valid_inputs = [str(num) for num in range(len(story['adventure']['scene'][curr_scene]['options']))]
        option_index = int(get_input(valid_inputs))

        scene_jump_match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", \
        string = story['adventure']['scene'][curr_scene]['options'][option_index])

        parse_check = re.search(pattern = "(?<=\{)[A-E] [0-9] [0-9]+(?=\})", \
        string = story['adventure']['scene'][curr_scene]['options'][option_index])
        #print(parse_check)
        if parse_check != None:

          skill_list = parse_check[0].split()
          #print(skill_list)
          skill_check = Player.skill_check(skill_list)

          if skill_check == 'F':
              return int(scene_jump_match.group())
          else:
              #print(skill_check)
              return int(skill_check)

    return int(scene_jump_match.group())



def story_flow(story: dict):

    global color_listG, Line, Picture

    curr_scene = Player.scene

    while curr_scene != None:
      Picture = ""
      Player.scene = curr_scene

      color_listG = colors.scene_colors(story, curr_scene)
      
      #print(color_listG)

      if story['adventure']['scene'][curr_scene] == None:
        curr_scene = None
        return 1

      Line = story['adventure']['scene'][curr_scene]['dialog']
      if 'picture' in story['adventure']['scene'][curr_scene]:
        Picture = colors.a_picture(story['adventure']['scene'][curr_scene]['picture'])
      # if a option contains nothing, or returns None, break form the loop.
      if story['adventure']['scene'][curr_scene]['options'] == None:
        global Options
        Options.clear()
        Line = story['adventure']['scene'][curr_scene]['dialog']
        Options.append("End Of The Story, To exit press 0")
        curr_scene = None
        curses.wrapper(divide_screen)
        return 1

      curr_scene = get_response(story, curr_scene)

################################################################################




def main(stdscr):
    
    # initiate colors
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    flag = 0
    stdscr.border()
    stdscr.refresh()

    while flag != 1:

        stdscr.clear()

        stdscr.refresh()
        curses.curs_set(0)

        flag = story_flow(story)


if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        input_arg  = sys.argv[1]
        input_arg2 = sys.argv[2]
        if input_arg2 == '-cc':
            Player = ch.createCharacter()
    else:
        input_arg = sys.argv[1]

    if input_arg == '-c':
        colors.terminal_colors()

    # Open the file and read the contents into my_xml
    # arg1: file name, arg2: r(read), arg3: encoding type
    with open(input_arg, 'r', encoding='utf-8') as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert
    # the XML document
    story = xmltodict.parse(my_xml, namespace_separator=True)
    
    # run story_file checks and initalize title variables 
    list_title = story_scheme.check(story)
    title_pic = list_title[0]
    save_name = list_title[1]
    title_pic_color = int(list_title[2])
    menu_color = int(list_title[3])
    path = Path(f"./saves_immic/{save_name}")
    if path.is_file() != True:
       Player = ch.createCharacter()
    curses.wrapper(title_screen)
    

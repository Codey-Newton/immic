import random
import time
import curses

Player = 0

# prompts player with points left in attribute and how many
# they want to take out to put into another stat.
def redistribute(A_stat, screen, tmp_points=0):
    #valid_point_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    stat = A_stat
    tmp_stat = stat
    flag = 0

    if (tmp_points == 0):
        screen.addstr("Points to redistribute: ")
        screen.addstr(str(A_stat))
        screen.addstr("\n")
        while flag != 1:
            screen.addstr("Please Enter ['1', '2', '3', '4', '5', '6', '7', '8', '9']: \n")
            tmp_points = screen.getch()
            screen.addstr("\n")
            if tmp_points == 49:
                tmp_points = 1
                flag = 1
            elif tmp_points == 50:
                tmp_points = 2
                flag = 1
            elif tmp_points == 51:
                tmp_points = 3
                flag = 1
            elif tmp_points == 52:
                tmp_points = 4
                flag = 1
            elif tmp_points == 53:
                tmp_points = 5
                flag = 1
            elif tmp_points == 54:
                tmp_points = 6
                flag = 1
            elif tmp_points == 55:
                tmp_points = 7
                flag = 1
            elif tmp_points == 56:
                tmp_points = 8
                flag = 1
            elif tmp_points == 57:
                tmp_points = 9
                flag = 1
            else:
                screen.addstr("\nInvalid input. ")

        stat -= tmp_points
        if (stat < 1):
            stat = tmp_stat
            tmp_points = 0
            screen.addstr("point limit reached!")

    elif (stat < 1):
        stat = tmp_stat
        tmp_points = 0
        screen.addstr("point limit reached!")

    else:
        flag = 0
        while flag != 1:
            screen.addstr("Do you want to add points or nothing: [+, n] \n")
            oper_choice = screen.getch()
            screen.addstr("\n")
            if (oper_choice == 43):
                flag = 1
                stat += tmp_points
                if (stat > 10):
                    stat = tmp_stat
                    screen.addstr("point limit reached!")
                else:
                    tmp_points = 0
                screen.clear()
            elif (oper_choice == 110):
                flag = 1
                screen.clear()
            else:
                screen.addstr("\nInvalid input. ")
    result = [tmp_points, stat]
    return (result)

def redistributep(A_stat, screen, tmp_points=0):
    #valid_point_input = ['1', '2', '3', '4', '5']
    stat = A_stat
    tmp_stat = stat
    flag = 0
    if (tmp_points == 0):
        screen.addstr("Points to redistribute: ")
        while flag != 1:
            screen.addstr("Please Enter ['1', '2', '3', '4', '5']: \n")
            tmp_points = screen.getch()
            screen.addstr("\n")
            if tmp_points == 49:
                tmp_points = 1
                flag = 1
            elif tmp_points == 50:
                tmp_points = 2
                flag = 1
            elif tmp_points == 51:
                tmp_points = 3
                flag = 1
            elif tmp_points == 52:
                tmp_points = 4
                flag = 1
            elif tmp_points == 53:
                tmp_points = 5
                flag = 1
            else:
                screen.clear()
                screen.addstr("\nInvalid input. ")

        stat -= tmp_points
        if (stat < 0):
            stat = tmp_stat
            tmp_points = 0
            screen.addstr("point limit reached!")

    elif (stat < 0):
        stat = tmp_stat
        tmp_points = 0
        screen.addstr("point limit reached!")

    else:
        flag = 0
        while flag != 1:
            screen.addstr("Do you want to add points or nothing: [+, n] \n")
            oper_choice = screen.getch()
            screen.addstr("\n")
            if (oper_choice == 43):
                flag = 1
                stat += tmp_points
                tmp_points = 0
                screen.clear()
            elif (oper_choice == 110):
                flag = 1
                screen.clear()
            else:
                screen.addstr("\nInvalid input. ")


    result = [tmp_points, stat]
    return (result)


#def skill_check(A_stat, A_check, A_scene):
 #   stat = A_stat
  #  check = A_check
   # scene_jump = A_scene


# -----------------------------------------------------------------------------
class Character(object):

    def __init__(self):
        self.name = ""
        self.Agile = ["A", 5]
        self.Brain = ["B", 5]
        self.Charm = ["C", 5]
        self.Detect = ["D", 5]
        self.Endure = ["E", 5]
        self.Points = ["P", 5]
        self.scene = 0

    # -------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------
    ''' check to see if player atrribute is higher than check
    if not, return F. if so, do a dice roll and take the difference 
    b/w the player stat and roll and see if it is higher than check
    return scene_jump if diff is higher than skill_check else return F '''
    def skill_check(self, str):
        #print("in skill_check")
        tmpstat = 0
        diceroll = random.randint(1, 9)
        stat = str[0]
        check = int(str[1])
        scene_jump = int(str[2])
        if(stat == self.Agile[0]):
            if (self.Agile[1] > check):
                tmpstat += self.Agile[1] - diceroll
                if(tmpstat > check):
                    return scene_jump
                else:
                    return 'F'
            else:
                return 'F'
        elif(stat == self.Brain[0]):
            if (self.Brain[1] > check):
                    tmpstat += self.Brain[1] - diceroll
                    if (tmpstat > check):
                        return scene_jump
                    else:
                        return 'F'
            else:
                return 'F'
        elif(stat == self.Charm[0]):
            if(self.Charm[1] > check):
                tmpstat += self.Charm[1] - diceroll
                if (tmpstat > check):
                    return scene_jump
                else:
                    return 'F'
            else:
                return 'F'
        elif (stat == self.Detect[0]):
            if (self.Detect[1] > check):
                tmpstat += self.Detect[1] - diceroll
                if (tmpstat > check):
                    return scene_jump
                else:
                    return 'F'
            else:
                return 'F'
        elif (stat == self.Endure[0]):
            if (self.Endure[1] > check):
                tmpstat += self.Endure[1] - diceroll
                if (tmpstat > check):
                    return scene_jump
                else:
                    return 'F'
            else:
                return 'F'

    ''' take input and run a case based on A-E
    run redistribute finction and take the returned list
    and initialize a stats newly allocated points'''
    def setupPoints(self):
        screen = curses.initscr()
        screen.clear()
        char_done = 0
        while char_done != 1:
            screen.addstr("Please enter a name for your Character: ")
            self.name = screen.getstr()
            screen.clear()

            flag = 0
            flag2 = 0
            #valid_stat_input = ['A', 'B', 'C', 'D', 'E', 'P']
            stat_list = [self.Agile[1], self.Brain[1], self.Charm[1], self.Detect[1], self.Endure[1], self.Points[1]]
            stat_results = []
            tmp_points = 0
            AreUdone = ""

            while AreUdone != "y":

            # check input
                #screen.clear()
                while flag != 1:
                    screen.addstr("Please Enter ['A', 'B', 'C', 'D', 'E', 'P']: \n")
                    stat = screen.getch()
                    screen.addstr("\n")
                    if stat == 65:
                        stat = "A"
                        flag = 1
                    elif stat == 66:
                        stat = "B"
                        flag = 1
                    elif stat == 67:
                        stat = "C"
                        flag = 1
                    elif stat == 68:
                        stat = "D"
                        flag = 1
                    elif stat == 69:
                        stat = "E"
                        flag = 1
                    elif stat == 80:
                        stat = "P"
                        flag = 1
                    else:
                        screen.clear()
                        screen.addstr("Invalid input. ")

                flag = 0
                match stat:
                    case 'A':
                        stat_results = redistribute(stat_list[0], screen, tmp_points)
                        tmp_points = stat_results[0]
                        stat_list[0] = stat_results[1]
                        self.Agile[1] = stat_list[0]

                    case 'B':
                        stat_results = redistribute(stat_list[1], screen, tmp_points)
                        tmp_points = stat_results[0]
                        stat_list[1] = stat_results[1]
                        self.Brain[1] = stat_list[1]

                    case 'C':
                        stat_results = redistribute(stat_list[2], screen, tmp_points)
                        tmp_points = stat_results[0]
                        stat_list[2] = stat_results[1]
                        self.Charm[1] = stat_list[2]

                    case 'D':
                        stat_results = redistribute(stat_list[3], screen, tmp_points)
                        tmp_points = stat_results[0]
                        stat_list[3] = stat_results[1]
                        self.Detect[1] = stat_list[3]

                    case 'E':
                        stat_results = redistribute(stat_list[4], screen, tmp_points)
                        tmp_points = stat_results[0]
                        stat_list[4] = stat_results[1]
                        self.Endure[1] = stat_list[4]

                    case 'P':
                        stat_results = redistributep(stat_list[5], screen, tmp_points)
                        tmp_points = stat_results[0]
                        stat_list[5] = stat_results[1]
                        self.Points[1] = stat_list[5]

                if (tmp_points > 0):
                    continue

                else:
                    if (self.Points[1] != 0):
                        screen.addstr("Still have points in Point attribute: ")
                        screen.addstr(str(self.Points[1]))
                        screen.addstr("\n")

                    else:
                        while flag2 != 1:
                            screen.addstr("Are done with character setup?: [y, n]: ")
                            AreUdone = screen.getch()
                            screen.addstr("\n")
                            if AreUdone == 121:
                                AreUdone = "y"
                                flag2 = 1
                                char_done = 1
                            elif AreUdone == 110:
                                AreUdone = "n"
                                flag2 = 1
                                screen.clear()
                            else:
                                screen.addstr("\nInvalid input. ")

                flag2 = 0

def createCharacter():
    global Player
    Player = Character()
    Player.setupPoints()
    return Player


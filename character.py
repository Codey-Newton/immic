import random
import time


def get_input(valid_input: list):
    while True:
        print("Enter ", valid_input)
        Input = input()
        if Input not in valid_input:
            print("\nInvalid input. Please use one of the following inputs:")
            print(valid_input)
            Input = None
        else:
            return Input


def redistribute(A_stat, tmp_points=0):
    valid_point_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    stat = A_stat
    tmp_stat = stat

    if (tmp_points == 0):
        print("\nPoints to redistribute: ")
        tmp_points = int(get_input(valid_point_input))
        stat -= tmp_points
        if (stat < 1):
            stat = tmp_stat
            tmp_points = 0
            print("point limit reached!")

    elif (stat < 1):
        stat = tmp_stat
        tmp_points = 0
        print("point limit reached!")

    else:
        oper_choice = input("Do you want to add points or nothing: [+, n] ")
        if (oper_choice == "+"):
            stat += tmp_points
            if (stat > 10):
                stat = tmp_stat
                print("point limit reached!")

            else:
                tmp_points = 0
        elif (oper_choice == "n"):
            print()

    result = [tmp_points, stat]
    return (result)

def redistributep(A_stat, tmp_points=0):
    valid_point_input = ['1', '2', '3', '4', '5']
    stat = A_stat
    tmp_stat = stat
    if (tmp_points == 0):
        print("\nPoints to redistribute: ")
        tmp_points = int(get_input(valid_point_input))
        stat -= tmp_points
        if (stat < 0):
            stat = tmp_stat
            tmp_points = 0
            print("point limit reached!")

    elif (stat < 0):
        stat = tmp_stat
        tmp_points = 0
        print("point limit reached!")

    else:
        oper_choice = input("Do you want to add points or nothing: [+, n] ")
        if (oper_choice == "+"):
            stat += tmp_points
            tmp_points = 0
        elif (oper_choice == "n"):
            print()

    result = [tmp_points, stat]
    return (result)


#def skill_check(A_stat, A_check, A_scene):
 #   stat = A_stat
  #  check = A_check
   # scene_jump = A_scene


# -----------------------------------------------------------------------------
class Character(object):

    def __init__(self, name):
        self.name = name
        self.Agile = ["A", 5]
        self.Brain = ["B", 5]
        self.Charm = ["C", 5]
        self.Detect = ["D", 5]
        self.Endure = ["E", 5]
        self.Points = ["P", 5]

    # -------------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------------
    def skill_check(self, str):

        print("in skill_check")
        tmpstat = 0
        diceroll = random.randint(1, 9)
        stat = str[0]
        check = int(str[1])
        scene_jump = int(str[2])
        print(" Dice roll number: ", diceroll)
        if(stat == self.Agile[0]):
            print("Agility check! ")
            if (self.Agile[1] > check):
                tmpstat += self.Agile[1] - diceroll
                if(tmpstat > check):
                    print("You have passed the skill check!")
                    return scene_jump
                else:
                    print( "You have failed the skill check!")
                    return 'F'
            else:
                print("You have failed the skill check!")
                return 'F'
        elif(stat == self.Brain[0]):
            print("Brain Check! ")
            if (self.Brain[1] > check):
                    tmpstat += self.Brain[1] - diceroll
                    if (tmpstat > check):
                        print("You have passed the skill check!")
                        return scene_jump
                    else:
                        print("You have failed the skill check!")
                        return 'F'
            else:
                print("You have failed the skill check!")
                return 'F'
        elif(stat == self.Charm[0]):
            print("Charm Check!")
            if(self.Charm[1] > check):
                tmpstat += self.Charm[1] - diceroll
                if (tmpstat > check):
                    print("You have passed the skill check!")
                    return scene_jump
                else:
                    print("You have failed the skill check!")
                    return 'F'
        elif (stat == self.Detect[0]):
            print("Detect Check!")
            if (self.Detect[1] > check):
                tmpstat += self.Detect[1] - diceroll
                if (tmpstat > check):
                    print("You have passed the skill check!")
                    return scene_jump
                else:
                    print("You have failed the skill check!")
                    return 'F'
        elif (stat == self.Endure[0]):
            print("Endure Check!")
            if (self.Endure[1] > check):
                tmpstat += self.Endure[1] - diceroll
                if (tmpstat > check):
                    print("You have passed the skill check!")
                    return scene_jump
                else:
                    print("You have failed the skill check!")
                    return 'F'
        else:
            print("Not an Attribute!")

    def setupPoints(self):
        print("in setup\n")
        valid_stat_input = ['A', 'B', 'C', 'D', 'E', 'P']
        stat_list = [self.Agile[1], self.Brain[1], self.Charm[1], self.Detect[1], self.Endure[1], self.Points[1]]
        stat_results = []
        tmp_points = 0
        AreUdone = ""

        while AreUdone != 'y':

            # check input
            stat = get_input(valid_stat_input)

            match stat:
                case 'A':
                    stat_results = redistribute(stat_list[0], tmp_points)
                    tmp_points = stat_results[0]
                    stat_list[0] = stat_results[1]
                    self.Agile[1] = stat_list[0]

                case 'B':
                    stat_results = redistribute(stat_list[1], tmp_points)
                    tmp_points = stat_results[0]
                    stat_list[1] = stat_results[1]
                    self.Brain[1] = stat_list[1]

                case 'C':
                    stat_results = redistribute(stat_list[2], tmp_points)
                    tmp_points = stat_results[0]
                    stat_list[2] = stat_results[1]
                    self.Charm[1] = stat_list[2]

                case 'D':
                    stat_results = redistribute(stat_list[3], tmp_points)
                    tmp_points = stat_results[0]
                    stat_list[3] = stat_results[1]
                    self.Detect[1] = stat_list[3]

                case 'E':
                    stat_results = redistribute(stat_list[4], tmp_points)
                    tmp_points = stat_results[0]
                    stat_list[4] = stat_results[1]
                    self.Endure[1] = stat_list[4]

                case 'P':
                    stat_results = redistributep(stat_list[5], tmp_points)
                    tmp_points = stat_results[0]
                    stat_list[5] = stat_results[1]
                    self.Points[1] = stat_list[5]

            if (tmp_points > 0):
                print()

            else:
                if (self.Points[1] != 0):
                    print("Still have points in Point attribute: ", self.Points[1])
                else:
                    AreUdone = input("Are done with character setup?: [y, n]: ")

# -------------------------------------------------------------------------------
if __name__ == '__main__':
    name1 = input("Please enter your character's name:")
    Player = Character(name1)
    print(Player.name)
    skillz = "A75"
    skills = "B56"
    Skill = "C34"
    SKILL = "D45"
    Spill = "E21"
    Player.setupPoints()
    print(Player.Agile, Player.Brain,
          Player.Charm, Player.Detect, Player.Endure, Player.Points)
    Player.skill_check(skillz)
    Player.skill_check(skills)
    Player.skill_check(Skill)
    Player.skill_check(SKILL)
    Player.skill_check(Spill)
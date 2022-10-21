from secrets import choice


class Character(object):


    def __init__(self, name):
        name = name
        self.Agile  = ["A", 5]
        self.Brain  = ["B", 5]
        self.Charm  = ["C", 5]
        self.Detect = ["D", 5]
        self.Endure = ["E", 5]
        self.Points = ["P", 5]

    def skill_check(self, str):
        print("in skill_check")
        stat = str[0]
        print(stat)
        check = int(str[1])
        print(check)
        scene_jump = int(str[2])
        print(scene_jump)

        if (self.Agile[0] == stat):
            print("yes")
            self.Agile[1] = check
            print(self.Agile[1])
        

    def setupPoints(self):
        print("in setup")
        valid_stat_input = ['A','B','C','D','E', 'P']
        tmp_stat = 0 
        tmp_points = 0
        oper_choice = ""
        AreUdone = ""
        while AreUdone != 'y':

            #check input
            stat = input("Enter stat: [A,B,C,D,E]: " )
            while stat not in valid_stat_input:
                print("Invalid input. Please use one of the following inputs:\n")
                print(valid_stat_input)
            
            match stat:
                case 'A':
                    tmp_stat = self.Agile[1]
                    if (tmp_points == 0):
                        tmp_points = int(input("Points to redistribute: "))
                        if(self.Agile[1] <= 1):
                            self.Agile[1] = tmp_stat
                            tmp_points = 0
                            print("point limit reached!")
                        else:
                            self.Agile[1] -= tmp_points

                    elif(self.Agile[1] < 1):
                        self.Agile[1] = tmp_stat
                        tmp_points = 0
                        print("point limit reached!")

                    else:
                        oper_choice = input("Do you want to add points or nothing: [+, n]")

                        if(oper_choice == "+"):
                            self.Agile[1] += tmp_points
                            if (self.Agile[1] > 10):
                                self.Agile[1] = tmp_stat
                                print("point limit reached!")
                                
                            else:
                                tmp_points = 0
                                print(self.Agile[1])

                        elif(oper_choice == "n"):
                            print() 
                case 'B':
                    tmp_stat = self.Brain[1]
                    if (tmp_points == 0):
                        tmp_points = int(input("Points to redistribute: "))
                        self.Brain[1] -= tmp_points

                    elif(self.Brain[1] < 1):
                        self.Brain[1] = tmp_stat
                        tmp_points = 0
                        print("point limit reached!")

                    else:
                        oper_choice = input("Do you want to add points or nothing: [+, n]")

                        if(oper_choice == "+"):
                            self.Brain[1] += tmp_points
                            if (self.Brain[1] > 10):
                                self.Brain[1] = tmp_stat
                                print("point limit reached!")
                                
                            else:
                                tmp_points = 0
                                print(self.Brain[1])


                        elif(oper_choice == "n"):
                            print() 

            AreUdone = input("Are done with character setup?: [y, n]: ")
    
        
        


if __name__=='__main__': 
    name1 = input("Please enter your character's name:")
    Player = Character(name1)
    skillz = "A75"
    Player.setupPoints()
    Player.skill_check(skillz)
    print(Player.Agile)
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
    
        
        


if __name__=='__main__': 
    name1 = input("Please enter your character's name:")
    Player = Character(name1)
    skillz = "A75"
    Player.setupPoints()
    Player.skill_check(skillz)
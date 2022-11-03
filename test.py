import character as ch
import pickle, sys, ascii_magic

def a_picture(picture):
    ascii_magic.Modes.TERMINAL
    ascii_magic.Back.GREEN
    tmp_pic = ascii_magic.from_image_file(
        picture, char = 'g', columns=50)
    return tmp_pic

def save_story(Player:ch.Character):
    with open('Player.pickle', 'wb') as f:
        pickle.dump(Player, f)

def load_story(Player:ch.Character):
    with open('Player.pickle', 'rb') as f:
        Player = pickle.load(f)
    return Player
if __name__ == "__main__":
    Player = ch.Character()
    print("before pickle:\n")
    Player.name = "Tim"
    print(Player.name)
    save_story(Player)
    print("name change: ")
    Player.name = "john"
    print(Player.name)
    Player = load_story(Player)
    print("after pickle load:\n")
    print(Player.name)
    pic = 'cskull.jpeg'
    pic = a_picture(pic)
    print(pic)
import xmltodict
import re
import sys,time,random

def display_scene_text(dialog: str):
  print(dialog)
  print("\n")

#checks to see if your input is in the valid_inputs list
def get_input(valid_input: list):
  while True:
    user_entered = input()
    if user_entered not in valid_input:
      print("Invalid input. Please use one of the following inputs:\n")
      print(valid_input)
      user_entered = None
    else:
      return user_entered

def get_response(story: dict, curr_scene: int):

    # if there are more than 4 options, its actually a single option,
    # but it counts the individual characters. 
    # Or in another way, there are 4 options max
    if(len(story['adventure']['scene'][curr_scene]['options']) > 4):
        print(str(0) + ". " + story['adventure']['scene'][curr_scene]['options'])
        valid_inputs = [str(num) for num in range(1)]
        option_index = int(get_input(valid_inputs))

        # parse the option string using re's to find integers contained
        # in [ ], (must be integers in [ ]).
        # and save the value in a variable.
        # N: use re library thats built in to python
        scene_jump_match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", string = story['adventure']['scene'][curr_scene]['options'])
        print(scene_jump_match.group())

    # do everything above exept with more than one option
    else:
      for i in range(len(story['adventure']['scene'][curr_scene]['options'])):
        print(str(i) + ". " + story['adventure']['scene'][curr_scene]['options'][i]) 
      valid_inputs = [str(num) for num in range(len(story['adventure']['scene'][curr_scene]['options']))]
      print(valid_inputs)
      option_index = int(get_input(valid_inputs))
      print(option_index)
      scene_jump_match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", string = story['adventure']['scene'][curr_scene]['options'][option_index])
      print(scene_jump_match.group())
  

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



if __name__=='__main__':

  # Open the file and read the contents into my_xml
  # arg1: file name, arg2: r(read), arg3: encoding type
  with open('debugAdventure.xml', 'r', encoding='utf-8') as file:
        my_xml = file.read()

  # Use xmltodict to parse and convert 
  # the XML document
  story = xmltodict.parse(my_xml, namespace_separator=True)
  story_flow(story)
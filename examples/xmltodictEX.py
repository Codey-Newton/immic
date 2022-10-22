import xmltodict
import pprint
import re
# Open the file and read the contents into my_xml
# arg1: file name, arg2: r(read), arg3: encoding type
with open('debugAdventure.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()
  
# Use xmltodict to parse and convert 
# the XML document
my_dict = xmltodict.parse(my_xml, namespace_separator=True)
  
# Print the dictionary
pprint.pprint(my_dict, indent=2)
print("\n")

#concatenate 1st option strings from the dictionary
option = ""
for i in range(len(my_dict['adventure']['scene'])):
    if(my_dict['adventure']['scene'][i]['options'] == None):
        print("endscene\n")
        break
    for j in range(len(my_dict['adventure']['scene'][i]['options'])):
        if(len(my_dict['adventure']['scene'][i]['options']) > 4):
            match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", string = my_dict['adventure']['scene'][i]['options'])
            print(match.group())
            break
        else: 
            match = re.search(pattern = "(?<=\[)[0-9]+(?=\])", string = my_dict['adventure']['scene'][i]['options'][j])
        print(match.group())



#print dialog
print(my_dict['adventure']['scene'][0]['dialog'])

#check length 
print(len(my_dict['adventure']['scene'][2]['options']))

#using re library to match bracket pattern
match = re.search(pattern = "\[[0-9]+\]", string = my_dict['adventure']['scene'][0]['options'][2])
print(match.group())

#find a key in dicitonary
if 'color_dialog' in my_dict['adventure']['scene'][0]:
    print("found colors")
else:
    print("no colors")
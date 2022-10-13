import xmltodict
import pprint

# Open the file and read the contents
with open('example.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()
  
# Use xmltodict to parse and convert 
# the XML document
my_dict = xmltodict.parse(my_xml)
  
# Print the dictionary
pprint.pprint(my_dict, indent=2)
print("\n")

#concatenate 1st option strings from the dictionary
option = ""
for i in range(4):
    option += my_dict['adventure']['arc']['scene'][i]['options'][0]
print(option)
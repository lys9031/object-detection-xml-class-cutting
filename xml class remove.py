import os
import xml.etree.ElementTree as ET

Dir = r"C:\Users\a\Desktop\b"

file_list = os.listdir(Dir)
xml_list = []
for file in file_list:
    if '.xml' in file:
        xml_list.append(file)

for xml_file in xml_list:
    target_path = Dir + "\\" + xml_file
    targetXML = open(target_path, 'rt', encoding='UTF8')
    
    tree = ET.parse(targetXML)
    root = tree.getroot()
    
    for object in root.findall('object'):
        name = str(object.find('name').text)
        if name == 'cat':
            root.remove(object)
        if name == 'sun':
            root.remove(object)
        if name == 'moon':
            root.remove(object)
        if name == 'cloud':
            root.remove(object)
        if name == 'flower':
            root.remove(object)
        if name == 'butterfly':
            root.remove(object)
        if name == 'snowman':
            root.remove(object)
        if name == 'car':
            root.remove(object)
        if name == 'train':
            root.remove(object)
        if name == 'ship':
            root.remove(object)
        if name == 'plane':
            root.remove(object)
        if name == 'bicycle':
            root.remove(object)
        if name == 'animal':
            root.remove(object)
        if name == 'rabbit':
            root.remove(object)
        if name == 'bird':
            root.remove(object)
        if name == 'whale':
            root.remove(object)
        if name == 'fish':
            root.remove(object)
        if name == 'window':
            root.remove(object)
        if name == 'door':
            root.remove(object)
        if name == 'star':
            root.remove(object)
        if name == 'rainbow':
            root.remove(object)
        if name == 'baseline':
            root.remove(object)
        if name == 'rain':
            root.remove(object)
        if name == 'electriclight':
            root.remove(object)
        if name == 'ladder':
            root.remove(object)
        if name == 'stair':
            root.remove(object)
        if name == 'fence':
            root.remove(object)
        if name == 'person':
            root.remove(object)
        if name == 'person1':
            root.remove(object)
        if name == 'person2':
            root.remove(object)
        if name == 'person3':
            root.remove(object)
        if name == 'person4':
            root.remove(object)
        if name == 'person5':
            root.remove(object)
        if name == 'house':
            root.remove(object)
        if name == 'house1':
            root.remove(object)
        if name == 'house2':
            root.remove(object)
        if name == 'tree':
            root.remove(object)
        if name == 'tree1':
            root.remove(object)
        if name == 'tree2':
            root.remove(object)
        if name == 'tree3':
            root.remove(object)
        if name == 'tree4':
            root.remove(object)
        if name == 'fruittree':
            root.remove(object)

            
    tree.write(xml_file)
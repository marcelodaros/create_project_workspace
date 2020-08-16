import os
import sys
from datetime import date, datetime

# Check if usage is correct
if len(sys.argv) != 2:
    print("Usage: python folders.py /destination")
    exit(1)

# set destination path
destination = sys.argv[1]

# create list for folder template for project
folderStructure = ['00_PROJETO', '01_DOCS', '02_BINS_EDITORES',
                    '03_ARTES', '04_SETTINGS', '05_EXPORT', '06_CREDITOS',
                    '07_VFX', '08_COLOR_GRADE', '09_SOUND_DESIGN', '10_OFFS',
                    '11_TRILHAS', '98_ACESSIBILIDADE', '99_MASTERS']

# create list for folders inside each project
epsStructure = ['__ASSIST', '__EDIT', '__FINALIZACAO', '_WORK']

# create all folder in the destination path
for folder in folderStructure:
    try:
        os.mkdir(destination + folder)
    except FileExistsError:
        print("Folder ", destination, " already exists")

# ask for number of episodes
num_eps = int(input("Qual o número de EPs? "))

# ask for project ID
id_prj = input("Qual o ID do projeto? ")

# determine the framerate of the project
print("23,98 [1] | 29,97 [2]")
framerate = int(input("Qual framerate, 1 ou 2? "))

# copy the correct template for the framerate
if framerate == 1:
    file_template = open("AvidTemplate/Template23/Template23.avp", "rb")
    file2_template = open("AvidTemplate/Template23/Template23 Settings.xml", "rb")
    prj_template = file_template.read()
    set_template = file2_template.read()
elif framerate == 2:
    file_template = open("AvidTemplate/Template29/Template29.avp", "rb")
    file2_template = open("AvidTemplate/Template29/Template29 Settings.xml", "rb")
    prj_template = file_template.read()
    set_template = file2_template.read()
else:
    print("Input errado do framerate!")
    exit(1)

# creating episodes projects and folders
i = 1
while i <= num_eps:
    # create folder for the episode
    folder_name = (destination + folderStructure[0] + "/{}_EP{:02d}").format(id_prj.upper(), i)
    os.mkdir(folder_name)

    # create all epsStructure folders inside episode's folder
    for folder in epsStructure:
        try:
            os.mkdir(folder_name + '/' + folder)
        except FileExistsError:
            print("Folder ", (folder_name + '/' + folder), " already exists")

    # generate episode project
    prj_name = (destination + folderStructure[0] + "/{}_EP{:02d}/{}_EP{:02d}.avp").format(id_prj.upper(), i, id_prj.upper(), i)
    newprj = open(prj_name, "wb")
    newprj.write(prj_template)

    # generate episode Settings file
    set_name = (destination + folderStructure[0] + "/{}_EP{:02d}/{}_EP{:02d} Settings.xml").format(id_prj.upper(), i, id_prj.upper(), i)
    newset = open(set_name, "wb")
    newset.write(set_template)

    # close current files
    newprj.close()
    newset.close()
    i += 1

# close template files
file_template.close()
file2_template.close()


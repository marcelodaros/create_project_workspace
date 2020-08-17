# create_project_workspace
A Python script for creating template folders and Avid Projects.

You can set number of episodes, the ID of the project and two framerates (23,98 and 29,97).
All Avid projects are 1080p.

Download folders.py and AvidTemplate folder.

Put both in same folder and run the script in a terminal.

Usage: pyhton folders.py /destination

Ex:
python folders.py c:/test/

Template (PT-BR):

00_PROJETO

01_DOCS

02_BINS_EDITORES

03_ARTES

04_SETTINGS

05_EXPORT

06_CREDITOS

07_VFX

08_COLOR_GRADE

09_SOUND_DESIGN

10_OFFS

11_TRILHAS

98_ACESSIBILIDADE

99_MASTERS

Episode template:
ID_EP##:
  - __ASSIST
  - __EDIT
  - __FINALIZACAO
  - WORK


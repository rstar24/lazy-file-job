# THis file will work only in wsl
import os
import pandas as pd
import numpy as np
import shutil
import subprocess

students = pd.read_csv("/mnt/e/python_file_creation_automation/students.csv")
build_dir = '/mnt/e/python_file_creation_automation/build/'
front_page_dir = '/mnt/e/python_file_creation_automation/src/front-page'


students['Student_Name'] = students['Student Name'].str.replace(' ','_')

names = []

for x in students['Student_Name']:
    names.append(x)

copy_path_f1 = [ build_dir + x + '/' for x in names ]
copy_command_array = ['cp -r ' + front_page_dir +' ' + build_dir + x for x in students['Student_Name'] ]

#print(copy_commad_array[0])
#print(copy_path_f1)

for x in copy_command_array:
    subprocess.run(x,shell=True)

"""
for x in copy_path_f1:
    shutil.copytree(front_page_dir,x)
    
front_page_files = []
for x in copy_path_f1:
    front_page_files.append(x + '/front-page/template.tex')
"""
#print(front_page_files)

# Now build the sed command for changing the 
# words I should make a sed command array 
# this will be simple as shit
#print(students.head())

sed_command_array = []

for index, row in students.iterrows():
    s = "sed -i 's/Rishabh\ Rathore/{}/g; s/0827CI211155/{}/g' /mnt/e/python_file_creation_automation/build/{}/front-page/front-page.tex".format(row['Student Name'].replace(" ","\ "),row['Enrollment no'],row['Student_Name'])
    sed_command_array.append(s)

print(sed_command_array[0])

for x in sed_command_array:
    subprocess.run(x, shell=True)

print('Done-Beautifuly')

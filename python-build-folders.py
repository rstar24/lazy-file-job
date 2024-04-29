import os
import pandas as pd
import numpy as np

students = pd.read_csv("/mnt/e/python_file_creation_automation/students.csv")
build_dir = '/mnt/e/python_file_creation_automation/build/'

students['Student Name'] = students['Student Name'].str.replace(' ','_')

names = []

for x in students['Student Name']:
    names.append(x)

# print(names)
os.chdir(build_dir)

for x in names:
    os.mkdir(x)





# folder_name = []

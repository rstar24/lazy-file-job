import os
import pandas as pd
import numpy as np

students_csv_path = os.path.abspath('students.csv')

students = pd.read_csv(students_csv_path)
build_dir = os.path.dirname(students_csv_path)

students['Student Name'] = students['Student Name'].str.replace(' ','_')

names = []

for x in students['Student Name']:
    names.append(x)

# print(names)
os.chdir(build_dir)

for x in names:
    os.mkdir(x)





# folder_name = []

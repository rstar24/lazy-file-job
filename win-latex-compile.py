# THis file will work only in windows 
import os
import pandas as pd
import numpy as np
import shutil
import subprocess

students_csv_path = os.path.abspath('students.csv')

students = pd.read_csv(students_csv_path)
build_dir = os.path.dirname(students_csv_path)
front_mklatex_base_dir = os.path.join(build_dir,'build')


students['Student_Name'] = students['Student Name'].str.replace(' ','_')
front_page_latex_files = []

for x in students['Student_Name']:
    temp = front_mklatex_base_dir
    x = temp + x + '\\front-page\\front-page.tex'
    front_page_latex_files.append(x)





print('Done-Beautifuly')

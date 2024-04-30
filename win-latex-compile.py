# THis file will work only in windows 
import os
import pandas as pd
import numpy as np
import shutil
import subprocess

students = pd.read_csv("E:\\python_file_creation_automation\\students.csv")
build_dir = 'E:\\python_file_creation_automation\\'
front_mklatex_base_dir = 'E:\\python_file_creation_automation\\build\\'


students['Student_Name'] = students['Student Name'].str.replace(' ','_')

front_page_latex_files = []

for x in students['Student_Name']:
    temp = front_mklatex_base_dir
    x = temp + x + '\\front-page\\front-page.tex'
    front_page_latex_files.append(x)





print('Done-Beautifuly')

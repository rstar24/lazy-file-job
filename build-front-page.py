
import os
import pandas as pd
import numpy as np
import shutil
import subprocess

students = pd.read_csv("/mnt/e/python_file_creation_automation/students.csv")
build_dir = '/mnt/e/python_file_creation_automation/build/'
front_page_dir = '/mnt/e/python_file_creation_automation/src/front-page'


students['Student Name'] = students['Student Name'].str.replace(' ','_')

names = []

for x in students['Student Name']:
    names.append(x)

copy_path_f1 = [ build_dir + x for x in names ]

for x in copy_path_f1:
    shutil.copy(front_page_dir,x)

front_page_files = []

for x in copy_path_f1:
    front_page_files.append(x + '/front-page/template.tex')



sed_commad_0 = "sed -i 's/Rishabh Rathore/'



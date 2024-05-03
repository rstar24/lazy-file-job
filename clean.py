# This script is for cleaning the build directory
# it will delete the contents of the students and final folder in 
# build dir 
import os 
import shutil
# import pandas as pd
# import numpy as np

def delete_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
        
current_dir = os.getcwd()
build_dir = os.path.join(current_dir,'build')
build_dir_students = os.path.join(build_dir,'students')
build_dir_final = os.path.join(build_dir,'final')

delete_folder_contents(build_dir_students)
delete_folder_contents(build_dir_final)
print("Cleared the contents of build/students and build/final")
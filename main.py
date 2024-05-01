import os
import shutil
import subprocess
import re
import time
import pandas as pd
import numpy as np
from PyPDF2 import PdfFileMerger

start_time = time.time()


# THis is a utility function for copying the contents of a folder to another 
# folder
def copy_directory_contents(source_dir, destination_dir):
    try:
        # Ensure source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

        # Ensure destination directory exists or create it
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Copy the contents of the source directory to the destination directory
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)
            destination_item_path = os.path.join(destination_dir, item)
            if os.path.isdir(source_item_path):
                shutil.copytree(source_item_path, destination_item_path)
            else:
                shutil.copy2(source_item_path, destination_item_path)

        # print("Directory contents copied successfully!")
    except Exception as e:
        print("An error occurred:", e)

# This is a utility function for replacing the text in the
# tex file 
def replace_text_in_file(file_path, search_pattern, replace_text):
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # Use regular expressions to perform the search and replace
        new_contents = re.sub(search_pattern, replace_text, file_contents)

        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.write(new_contents)

        # print("Text replaced successfully!")
    except Exception as e:
        print("An error occurred:", e)    

# Declaring the important paths
proj_root_dir = os.getcwd()
build_dir = os.path.join(proj_root_dir,'build')
build_dir_final = os.path.join(build_dir,'final')
build_dir_students = os.path.join(build_dir,'students')

src_dir = os.path.join(proj_root_dir,'src')
file_tex_template_path = os.path.join(src_dir,'file')
front_tex_path = os.path.join(src_dir,'front-page')

# Making directory for each student
students = pd.read_csv('students.csv')
students['Student_Name'] = students['Student Name'].str.replace(' ','_')

students_build_dirs_paths = []
# Will create named folder for each student in build_dir
def create_folder_in_students():
    for x in students['Student_Name']:
        temp = os.path.join(build_dir_students,x)
        students_build_dirs_paths.append(temp)
        os.mkdir(temp)
        
    for x in students_build_dirs_paths:
        file = os.path.join(x,'file')
        front_page = os.path.join(x,'front-page')
        os.mkdir(file)
        os.mkdir(front_page)
        
    print('Empty Student Name Folders Created')
    print("made file and front page dir in students")

create_folder_in_students()

def copy_tex_dirs():
    print("Starting the copying of template tex")
    
    for x in students_build_dirs_paths:
        file_path = os.path.join(x,'file')
        front_page_path = os.path.join(x,'front-page')
        copy_directory_contents(file_tex_template_path,file_path)
        copy_directory_contents(front_tex_path,front_page_path)
    print('file-tex and front-page-tex file copied')
        
copy_tex_dirs()    
print("Working fine till the copying part")    

# Now I need to change the name and enrollment number
# for all the students 

def change_it():
    my_name = r'Rishabh Rathore'
    my_enn = r'0827CI211155'
    file_paths = []
    front_paths = []
    names = students['Student Name'].tolist()
    enn = students['Enrollment no'].tolist()
    
    for x in students_build_dirs_paths:
        t0 = os.path.join(x,'file')
        t1 = os.path.join(t0,'template.tex')
        t2 = os.path.join(x,'front-page')
        t3 = os.path.join(t2,'front-page.tex')
        # file_paths.append(os.path.join(x,'file\\template.tex'))
        # front_paths.append(os.path.join(x,'front-page\\front-page.tex'))
        file_paths.append(t1)
        front_paths.append(t3)
    
    # if(len(file_paths) == len(front_paths)):
    #     print('file_paths len {}'.format(len(file_paths)))
    #     print('front_paths len {}'.format(len(front_paths)))
    #     print("works")
    
    # Replace names and enn
    for i in range(len(names)):
        replace_text_in_file(file_paths[i],my_name,names[i])
        replace_text_in_file(file_paths[i],my_enn,enn[i])
        replace_text_in_file(front_paths[i],my_name,names[i])
        replace_text_in_file(front_paths[i],my_enn,enn[i])
    
    print('Replacement successful')        

change_it()

def compile_tex():
    file_paths = []
    front_paths = []
    for x in students_build_dirs_paths:
        t1 = os.path.join(x,'file')
        t2 = os.path.join(t1,'template.tex')
        file_paths.append(t2)
        t3 = os.path.join(x,'front-page')
        t4 = os.path.join(t1,'front-page.tex')
        front_paths.append(t4)
        # file_paths.append(os.path.join(x,'file\\template.tex'))
        # front_paths.append(os.path.join(x,'front-page\\front-page.tex'))
    
    # print("len(student_build_paths) = {}".format(len(students_build_dirs_paths)))
    # print("len(file_paths) = {}".format(len(file_paths)))
    # print("len(front_paths) = {}".format(len(front_paths)))
    
    
    
    command_compile_file_tex = []
    command_compile_front_tex = []
    
    # for i in range(len(students_build_dirs_paths)):
    for x in students_build_dirs_paths:
        for i in range(5):
            t1 = os.path.join(x,'file')
            t2 = os.path.join(t1,'template.tex')
            t3 = os.path.join(x,'front-page')
            t4 = os.path.join(t1,'front-page.tex')
            temp = "pdflatex --include-directory={} --output-directory={} {}".format(t1,t2,file_paths[i])
            temp2= "pdflatex --output-directory={} {}".format(t3,t4)
            subprocess.run(temp)
            subprocess.run(temp2)
        # print(temp)
        
        # subprocess.run(temp,shell=True)
        # result = subprocess.run(temp,shell=True,capture_output=True,text=True)
        # if(result.returncode == 0):
        #     print("compiled It")
        # else:
        #     print("try again Rishabh")
        
    # for i in range(len(front_paths)):
    #     temp = "pdflatex -output-directory={} {}".fromat(os.path.curdir(file_paths[i]),file_paths[i])
    #     result = subprocess.run(temp,shell=True,capture_output=True,text=True)
    #     if(result.returncode == 0):
    #         print("compiled It")
    #     else:
    #         print("try again Rishabh")

compile_tex()

end_time = time.time()
temp_0 = end_time-start_time
print("Time taken by the script {}".format(temp_0))
# print(proj_root_dir)
# print(build_dir_final)
# print(build_dir_students)
# students = pd.read_csv('studetns.csv')


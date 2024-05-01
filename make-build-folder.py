import os
import shutil

curr_dir = os.getcwd()
print(curr_dir)
os.mkdir('build')
build_dir = os.path.join(curr_dir,'build')
os.chdir('build')
os.mkdir('final')
os.mkdir('students')


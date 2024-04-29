#!/bin/usr/bash
# First make some The student named folders in thebuild 
# directory 
proj_dir="/mnt/e/python_file_creation_automation/"
build_dir="/mnt/e/python_file_creation_automation/build/"
csv_file="/mnt/e/python_file_creation_automation/students.csv"

students=$(awk -F ',' '{print $2}' "$csv_file")

for((i=0; i<${#students[@]}; i++)); do
    students[$i]=${students[$i]// /_}
done

cd "/mnt/e/python_file_creation_automation/build/"

# Use xargs to create folders from the array
for item in "${students[@]}"; do
    echo "$item"
done


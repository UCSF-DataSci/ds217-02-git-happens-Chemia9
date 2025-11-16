#!/bin/bash

echo "setting up project..."

# create directory structure
mkdir -p src data output

echo "created direcotries"

#create .gitignore
touch .gitignore

echo "created .gitignore"

#create sample data files
cat > data/students.csv << 'EOF'
name, age, grade, subject
Bob, 23, 91, Math
Sara, 21, 94, Chemistry
Anna, 21, 88, Chemistry
Daniel, 20, 82, Biology
Kevin, 22, 98, Biology
Tina, 20, 80, Math
Hannah, 22, 95, Math
Justin, 20, 78, Chemistry
EOF
echo "created sample data in data/students.csv"

#set up python template files
#set up data_analysis.py
cat > src/data_analysis.py << 'EOF'
#!/usr/bin/env python3
""" student grade analysis """

def load_students(filename):
    """ load the csv file as a list

    Args:
    filename: csv file of data

    Returns: list of dictionaries with each element of list 
    corresponding to a student
    """

    #TODO: read csv file by line
    #TODO: create a dictionary for each line with variables as keys
    #TODO: append each dictionary to a list

def calculate_average_grade (students):
    """ calculate average of all students grades

    Args:
    filename: the list of students data

    Returns: float for average grade across students
    """

    #TODO: Make list of grades only
    #TODO: calculate average

def count_math_students (students):
    """ count number of students in Math

    Args:
    students: the list of students data

    Returns: integer number of students in math
    """

    #TODO: make list of subjects
    #TODO: count number of maths in subjects

def generate_report():

def save_report(report, filename):

def main():

EOF
#set up data_analysis_functions.py

#make script executable
chmod +x setup_project.sh
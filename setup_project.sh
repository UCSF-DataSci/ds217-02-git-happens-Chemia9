#!/bin/bash

echo "setting up project..."

# create directory structure
mkdir -p src data output

echo "created direcotries"

#create .gitignore
touch .gitignore

echo "created .gitignore"

#create analysis_report.txt
touch output/analysis_report.txt

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

echo "setting up python templates"
cat > src/data_analysis.py << 'EOF'
#!/usr/bin/env python3
""" basic analysis script """

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

echo "set up python template 1"

#set up data_analysis_functions.py

cat > src/data_analysis_functions.py << 'EOF'
#!/usr/bin/env python3
"""Advanced analysis script"""

def load_data(filename):
    """ Generic loader that checks file extension

    Args:
    filename: any file type

    Returns: string 'csv' or error if not csv
    """

    #TODO: check if file type is csv

def load_csv (filename):

def analyze_data (students):
    """ return dictionary wit multiple statistics

    Args:
    students: list of student data

    Returns: dictionary with average, min, max
    """
    #TODO: create a list of grades
    #TODO: calculate average
    #TODO: get min and max

def analyze_grade_distribution (grades):
    """ count grades by letter grade ranges

    Args:
    grades: list of grades

    Returns: dictionary of counts and percentages
    """

    #TODO: define grade categories in dictionary
    #TODO: count through grades
    #TODO: add percentages to dictionary

def save_results (results, filename):

def main():

EOF

echo "set up python template 2"

#make script executable
chmod +x setup_project.sh
echo "script is executable"
echo "setup is complete"
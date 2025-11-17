#!/usr/bin/env python3
""" basic analysis script """

def load_students(filename):
    """ load the csv file as a list

    Args:
    filename: csv file of data

    Returns: list of dictionaries with each element of list 
    corresponding to a student
    """

    with open(filename, 'r') as file:
        lines = file.readlines()[1:] # read lines as list and exclude first line
        
    student_data = [] # create empty list
    for line in lines: # create a dictionary of datapoints for each line
        data = line.strip().split (',')
        student = {
            'name' : data[0],
            'age' : data[1],
            'grade' : data[2],
            'subject' : data[3]
        }
        student_data.append(student) # append to list

    return student_data # display final output


def calculate_average_grade (students):
    """ calculate average of all students grades

    Args:
    filename: the list of students data

    Returns: float for average grade across students
    """
    grades = list() # empty list for grades
    for student in students: # extract the grade from each student
        grade = student['grade']
        grades.append(int(grade)) # and append
    
    return sum(grades) / len(grades) # calculate average
        


def count_math_students (students):
    """ count number of students in Math

    Args:
    students: the list of students data

    Returns: integer number of students in math
    """

    subjects = list() # empty list for subjects
    for student in students: # extract subject from each student
        subject = student['subject'].title() # capitalize all
        subjects.append(subject) # and append

    return subjects.count('Math') # count Math

def generate_report(file):
    """generate report"""

    students = load_students(file)
    report = f"Basic Analysis:\n Data:\n {"\n".join(str(student) for student in students)}\n Average Grade = {calculate_average_grade(students):.1f}\n Number of Math Students: {count_math_students(students)}\n"

    return report

def save_report(report, filename):
    """save report to file"""
    with open(filename, 'w') as file:
        file.write(str(report)) # write report to file

def main():
    # Load data
    student_data = load_students("data/students.csv")

    if not student_data:
        print("No data loaded. Please check data/students.csv")
        return
    
    print(f"Loaded {len(student_data)} students")

    # using the generate report since it contains everything
    report = generate_report("data/students.csv")

    print(f"{report}")

    save_report(report, "output/analysis_report.txt")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Advanced analysis script"""

def load_data(filename):
    """ Generic loader that checks file extension

    Args:
    filename: any file type

    Returns: string 'csv' or error if not csv
    """
    if filename.endswith('.csv'):
        return "csv"
    else:
        raise ValueError("Unsupported file type. Only CSV files are supported.")   

def load_csv (filename):
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

def analyze_data (students):
    """ return dictionary wit multiple statistics

    Args:
    students: list of student data

    Returns: dictionary with average, min, max
    """

    grades = list() # empty list for grades
    for student in students: # extract the grade from each student
        grade = student['grade']
        grades.append(int(grade)) # and append
    average_grade = sum(grades) / len(grades) # calculate average
    min_grade = min(grades)
    max_grade = max(grades)
    return {
        'average_grade': average_grade,
        'min_grade': min_grade,
        'max_grade': max_grade
    }

def analyze_grade_distribution (students):
    """ count grades by letter grade ranges

    Args:
    grades: list of grades

    Returns: dictionary of counts and percentages
    """
    grades = list() # empty list for grades
    for student in students: # extract the grade from each student
        grade = student['grade']
        grades.append(int(grade)) # and append

    distribution = {
        'A': {'count': 0, 'percentage': 0.0},
        'B': {'count': 0, 'percentage': 0.0},
        'C': {'count': 0, 'percentage': 0.0},
        'D': {'count': 0, 'percentage': 0.0},
        'F': {'count': 0, 'percentage': 0.0}
    }
    for grade in grades:
        if grade >= 90:
            distribution['A']['count'] += 1
            distribution['A']['percentage'] += 1/len(grades) * 100
        elif grade >= 80:
            distribution['B']['count'] += 1
            distribution['B']['percentage'] += 1/len(grades) * 100
        elif grade >= 70:
            distribution['C']['count'] += 1
            distribution['C']['percentage'] += 1/len(grades) * 100
        elif grade >= 60:
            distribution['D']['count'] += 1
            distribution['D']['percentage'] += 1/len(grades) * 100
        else:
            distribution['F']['count'] += 1
            distribution['F']['percentage'] += 1/len(grades) * 100
    
    
    return distribution
    

def save_results (results, filename):

    """ save results to a text file

    Args:
    results: string of results
    filename: output text file

    Returns: None
    """
    with open (filename, 'w') as file:
        file.write(results)


def main():
    # Load data
    if load_data("data/students.csv") == "csv":
        student_data = load_csv("data/students.csv")
    else:
        raise ValueError("Unsupported file type. Only CSV files are supported.")   

    # Analyze data
    analysis = analyze_data(student_data)
    distribution = analyze_grade_distribution(student_data)

    # Prepare results
    results = f"Advanced Analysis Results:\n Average Grade: {analysis['average_grade']:.1f}\n Min Grade: {analysis['min_grade']}\n Max Grade: {analysis['max_grade']}\n\nGrade Distribution:\n"
    for grade, stats in distribution.items():
        results += f" {grade}: Count = {stats['count']}, Percentage = {stats['percentage']:.1f}%\n"

    # Save results
    save_results(results, "output/analysis_report.txt")

if __name__ == "__main__":
    main()
# ECOR 1042 Lab 5 - Individual submission for sort_students_age_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jacob Aydin"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101264856"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(student_info: list, order: str) -> list:
    """Takes a list of dictionaries and arranges the list with buble sorting technique depending on the age value and wheter the user wants ascending/descending order.
    returns the arranged list
    
    Preconditions: all the dictionaries either must contain or exclude age
    Examples:
    >>>sort_students_age_bubble([{"Age":25,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    [{'Age': 25, 'School': 'GP'}, {'Age': 19, 'School': 'MS'}]
    >>>sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Age" key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    >>>sort_students_age_bubble([{"Age":25,"School":"GP"},{"Age":19,"School":"MS"},{"Age":5,"School":"CF"},{"Age":4,"School":"BS"}], "A")
    [{'Age': 4, 'School': 'BS'}, {'Age': 5, 'School': 'CF'}, {'Age': 19, 'School': 'MS'}, {'Age': 25, 'School': 'GP'}]
    """
    a = 0
    swap = True
    while swap:
        swap = False
        for i in range(len(student_info) - 1):
            if "Age" not in student_info[i]:
                if a == 0:
                    print('"Age" key is not present')
                    a += 1
            else:
                for j in range(len(student_info) - i - 1):
                    if order == "A":
                        if student_info[j]["Age"] > student_info[j + 1]["Age"]:
                            student_info[j], student_info[j + 1] = student_info[j + 1], student_info[j]
                            swap = True
                    elif order == "D":
                        if student_info[j + 1]["Age"] > student_info[j]["Age"]:
                            student_info[j], student_info[j + 1] = student_info[j + 1], student_info[j]
                            swap = True
        return student_info

# Do NOT include a main script in your submission

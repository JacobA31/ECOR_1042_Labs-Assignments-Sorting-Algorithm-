# ECOR 1042 Lab 3 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jacob Aydin"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101264856"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#
# Place your student_school_list function after this line


def student_school_list(name_of_file: str, school: str) -> list[dict]:
    """The function takes the name of the file and school then returns a list that has all the informations for every student (except school) which are stored as dictionary
    
    Preconditions: The name_of_file must be 'student-mat.csv' in order to recieve data
    
    Example:
    >>>student_school_list('student-mat.csv', 'GP')
    [{'Age': '18', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another elemet}...]  
    >>>student_school_list('student-mat.csv', 'gp')
    []
    >>>student_school_list('student-mat.csv', 'MB')
    [{'Age': '16', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {another element} ...]
    """
    open_data = open(name_of_file)  #opens the data file
    data_dict1 = []     #Empty list to add the student info
    for line in open_data:  #Goes through every line in the data file
        data = line.strip('\n').split(',')  #Removes unnecessary things and makes a "list" of values
        if school == data[0]:   #Checks if the given school name is in the data
            student_info = {'Age': data[1], 'StudyTime': float(data[2]), 'Failures': int(data[3]), 'Health': int(data[4]),
                            'Absences': int(data[5]), 'G1': int(data[6]), 'G2': int(data[7]), 'G3': int(data[8])}   #Creates a dictionary for every student in the specific school and stores their data
            data_dict1.append(student_info) #Adds the dictionary to the empty list
    open_data.close()   #closes the file
    return data_dict1

# Do NOT include a main script in your submission

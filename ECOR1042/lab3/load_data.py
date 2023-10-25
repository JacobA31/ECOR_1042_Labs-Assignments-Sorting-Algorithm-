# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Jacob Aydin - Spencer Edmonds - Anneli Sheridan - Pagalavan Sivakumar"

# Update "" with your team (e.g. T102)
__team__ = "T111"

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
            student_info = {'Age': int(data[1]), 'StudyTime': float(data[2]), 'Failures': int(data[3]), 'Health': int(data[4]),
                            'Absences': int(data[5]), 'G1': int(data[6]), 'G2': int(data[7]), 'G3': int(data[8])}   #Creates a dictionary for every student in the specific school and stores their data
            data_dict1.append(student_info) #Adds the dictionary to the empty list
    open_data.close()   #closes the file
    return data_dict1

#==========================================#
# Place your student_health_list function after this line


def student_health_list(file_name: str, health_value: int) -> list[dict]:
    """
    Given a CSV file name and a health value, returns a list of dictionaries
    containing the information of all students whose health value matches the given value.
    Examples: 
    student_health_list(a, 0)
    >>>>[]
    student_health_list(a,1)
    """
    i = 0
    open_data = open(file_name)  #opens the data file
    data_dict1 = []     #Empty list to add the student info
    for line in open_data:  #Goes through every line in the data file
        data = line.strip('\n').split(',')  #Removes unnecessary things and makes a "list" of values

        if i > 0:
            if health_value == int(data[4]):   #Checks if the given school name is in the data
                student_info = {'School': data[0], 'Age': int(data[1]), 'StudyTime': float(data[2]), 'Failures': int(data[3]),
                                'Absences': int(data[5]), 'G1': int(data[6]), 'G2': int(data[7]), 'G3': int(data[8])}   #Creates a dictionary for every student in the specific school and stores their data
                data_dict1.append(student_info) #Adds the dictionary to the empty list
        i += 1
    open_data.close()   #closes the file
    return data_dict1
#==========================================#
# Place your student_age_list function after this line


def student_age_list(filename: str, age: int) -> list[dict]:
    """
    this code recieves a csv file input and and age input the csv file is opened and a dictionary is created of the information is created,
    the age is the age of the students and will return a dictionary of all the students with the same age
    
    Preconditions:
    file must and can only be a csv file, can only be 'student-mat.csv' 
    age must be postive integer
    
    Examples:
    >>>student_age_list("student-mat.csv", 15)
       [{'School': 'GP', 'StudyTime': '2', 'Failures': '3', 'Health': '3', 'Absences': '10', 'G1': '7', 'G2': '8', 'G3': '10'}, {another element}]
    >>>student_age_list("student-mat.csv", 0)
       []
    >>>student_age_list("student-mat.csv", 18)
       [{'School': 'GP', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another element}]
    """
    open_data = open(filename)  #opens the data file
    data_dict1 = []     #Empty list to add the student info
    i = 0
    for line in open_data:  #Goes through every line in the data file
        data = line.strip('\n').split(',')  #Removes unnecessary things and makes a "list" of values
        if i > 0:
            if age == int(data[1]):   #Checks if the given school name is in the data
                student_info = {'School': data[0], 'StudyTime': float(data[2]), 'Failures': int(data[3]), 'Health': int(data[4]),
                                'Absences': int(data[5]), 'G1': int(data[6]), 'G2': int(data[7]), 'G3': int(data[8])}   #Creates a dictionary for every student in the specific school and stores their data
                data_dict1.append(student_info) #Adds the dictionary to the empty list
        i += 1
    open_data.close()   #closes the file
    return data_dict1

#==========================================#
# Place your student_failures_list function after this line


def student_failures_list(list_students_file: str, num_fail: int) -> list[dict]:
    """Returns a list containing dictionaries of all the students who have
    the same number of failures as input by the user. Dictionaries should
    exclude the failures category. 

    Preconditions: num_fail >= 0.

    Ensure string entered for list_students_file makes the file accessible. 



    Examples:
    >>>student_failures_list('student-mat.csv', 16)
    []

    >>>student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another element}]

    >>>student_failures_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': '16', 'StudyTime': '1', 'Health': '5', 
    'Absences': '14', 'G1': '6', 'G2': '9', 'G3': '8'}, {another element}]
    """
    i = 0
    open_data = open(list_students_file)  #opens the data file
    data_dict1 = []     #Empty list to add the student info
    for line in open_data:  #Goes through every line in the data file
        data = line.strip('\n').split(',')  #Removes unnecessary things and makes a "list" of values
        if i > 0:
            if num_fail == int(data[3]):   #Checks if the given school name is in the data
                student_info = {'School': data[0], 'Age': int(data[1]), 'StudyTime': float(data[2]), 'Health': int(data[4]),
                                'Absences': int(data[5]), 'G1': int(data[6]), 'G2': int(data[7]), 'G3': int(data[8])}   #Creates a dictionary for every student in the specific school and stores their data
                data_dict1.append(student_info) #Adds the dictionary to the empty list
        i += 1
    open_data.close()   #closes the file
    return data_dict1

#==========================================#
# Place your load_data function after this line


def load_data(name_of_file: str, dict_key: tuple) -> list[dict]:
    """
    This function accepts two inputs, the first being a csv file ('student-mat.csv')
    the second being a tuple with 2 values, the first being the key of the data wanted (ex. 'Age')
    and the second being the input parameter for the data wanted, the function calls the function specified
    and returns a list containing a dictionary of the data specified
    
    Preconditions: 
    name_of_file must be 'student-mat.csv'
    1st value in tuble must and can only be one of 'School', 'Health', 'Age', 'Failures', or 'All'
    2nd value in tuple must be positive integer except in case of 'School' values must be one of 'GP', 'MB', 'CF', 'BD', or 'MS'
    
    Examples
    >>>load_data("student-mat.csv", ('Age', 15))
    [{'School': 'GP', 'StudyTime': '2', 'Failures': '3', 'Health': '3', 'Absences': '10', 'G1': '7', 'G2': '8', 'G3': '10'}, {Another Element}]
    >>>load_data("student-mat.csv", ('Failures', 1))
    [{'School': 'GP', 'Age': '16', 'StudyTime': '2', 'Health': '3', 'Absences': '25', 'G1': '7', 'G2': '10', 'G3': '11'}, {Another Element}]
    >>>load_data("student-mat.csv", ('School', 'BD'))
    [{'Age': '18', 'StudyTime': 2.0, 'Failures': 1, 'Health': 2, 'Absences': 0, 'G1': 7, 'G2': 7, 'G3': 0}, {Another Element}]
    """
    dict1 = []
    if dict_key[0] == 'School':
        return student_school_list(name_of_file, dict_key[1])

    elif dict_key[0] == 'Health':
        return student_health_list(name_of_file, dict_key[1])

    elif dict_key[0] == 'Age':
        return student_age_list(name_of_file, dict_key[1])

    elif dict_key[0] == 'Failures':
        return student_failures_list(name_of_file, dict_key[1])

    elif dict_key[0] == 'All':
        i = 0
        open_data = open(name_of_file)  #opens the data file
        data_dict1 = []     #Empty list to add the student info
        for line in open_data:  #Goes through every line in the data file
            data = line.strip('\n').split(',')  #Removes unnecessary things and makes a "list" of values
            if i > 0: #Helps to get rid of first line
                student_info = {'School': (data[0]), 'Age': int(data[1]), 'StudyTime': float(data[2]), 'Failures': int(data[3]), 'Health': int(data[4]),
                                'Absences': int(data[5]), 'G1': int(data[6]), 'G2': int(data[7]), 'G3': int(data[8])}   #Creates a dictionary for every student and stores their data
                data_dict1.append(student_info) #Adds the dictionary to the empty list
            i += 1
        open_data.close()   #closes the file
        return data_dict1
    else:
        print("Invalid Value")
        return dict1
#==========================================#
# Place your add_average function after this line


def add_average(students: list[dict]) -> list[dict]:
    """
    Given a list of dictionaries of student's grades the function calculates the average grade for each student and adds it to the dictionary as 'G_AVG'.
    Precondtion: none
    
    
    Examples:
    student1 = [
    {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
     'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6},
    {'School': 'MS', 'Age': 17, 'StudyTime': 5.2, 'Failures': 0,
     'Health': 5, 'Absences': 3, 'G1': 8, 'G2': 9, 'G3': 9},
    {'School': 'GP', 'Age': 16, 'StudyTime': 7.5, 'Failures': 2,
     'Health': 2, 'Absences': 10, 'G1': 3, 'G2': 4, 'G3': 5},
    ]
    student2 = [
    {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
     'Health': 3, 'Absences': 7, 'G1': 2, 'G2': 3, 'G3': 3},
    {'School': 'MS', 'Age': 17, 'StudyTime': 5.2, 'Failures': 0,
     'Health': 5, 'Absences': 3, 'G1': 1, 'G2': 1, 'G3': 1},
    {'School': 'GP', 'Age': 16, 'StudyTime': 7.5, 'Failures': 2,
     'Health': 2, 'Absences': 10, 'G1': 3, 'G2': 4, 'G3': 5},
    ]
    student3 = [
    {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
     'Health': 3, 'Absences': 7, 'G1': 2, 'G2': 8, 'G3': 4},
    {'School': 'MS', 'Age': 17, 'StudyTime': 5.2, 'Failures': 0,
     'Health': 5, 'Absences': 3, 'G1': 8, 'G2': 5, 'G3': 3},
    {'School': 'GP', 'Age': 16, 'StudyTime': 7.5, 'Failures': 2,
     'Health': 2, 'Absences': 10, 'G1': 9, 'G2': 3, 'G3': 1},
    ]

    add_average(student1)
    >>>[{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'School': 'MS', 'Age': 17, 'StudyTime': 5.2, 'Failures': 0, 'Health': 5, 'Absences': 3, 'G1': 8, 'G2': 9, 'G3': 9, 'G_Avg': 8.67}, {'School': 'GP', 'Age': 16, 'StudyTime': 7.5, 'Failures': 2, 'Health': 2, 'Absences': 10, 'G1': 3, 'G2': 4, 'G3': 5, 'G_Avg': 4.0}]
    add_average(student2)
    >>>[{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 2, 'G2': 3, 'G3': 3, 'G_Avg': 2.67}, {'School': 'MS', 'Age': 17, 'StudyTime': 5.2, 'Failures': 0, 'Health': 5, 'Absences': 3, 'G1': 1, 'G2': 1, 'G3': 1, 'G_Avg': 1.0}, {'School': 'GP', 'Age': 16, 'StudyTime': 7.5, 'Failures': 2, 'Health': 2, 'Absences': 10, 'G1': 3, 'G2': 4, 'G3': 5, 'G_Avg': 4.0}]
    add_average(student3)
    >>>[{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 2, 'G2': 8, 'G3': 4, 'G_Avg': 4.67}, {'School': 'MS', 'Age': 17, 'StudyTime': 5.2, 'Failures': 0, 'Health': 5, 'Absences': 3, 'G1': 8, 'G2': 5, 'G3': 3, 'G_Avg': 5.33}, {'School': 'GP', 'Age': 16, 'StudyTime': 7.5, 'Failures': 2, 'Health': 2, 'Absences': 10, 'G1': 9, 'G2': 3, 'G3': 1, 'G_Avg': 4.33}]
    """

    for student in students:
        # Calculate the average grade
        avg_grade = (student['G1'] + student['G2'] + student['G3']) / 3
        # Add the average grade to the dictionary
        student['G_Avg'] = round(avg_grade, 2)
    return students

# Do NOT include a main script in your submission

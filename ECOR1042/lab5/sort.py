# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Jacob Aydin - Spencer Edmonds - Anneli Sheridan - Pagalavan Sivakumar"

# Update "" with your team (e.g. T102)
__team__ = "T111"

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
#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(students_list: list, order: str) -> list:
    '''
    Sorts the given list of dictionaries by the "StudyTime" attribute
    using the selection sort algorithm. Based on user input the returned list needs to be ascending or descending
    based on if A or D is entered. It hsoyuld only sort if "StudyTIme is in the dictonary
    
    Examples:
    sort_students_by_studytime( [{"StudyTime":10.2,"School":"GP"},{"StudyTime":19.1,"School":"MS"},{"StudyTime":12.2,"School":"GP"},{"StudyTime":14.2,"School":"GP"}], "A")
    >>>[{'StudyTime': 10.2, 'School': 'GP'}, {'StudyTime': 12.2, 'School': 'GP'}, {'StudyTime': 14.2, 'School': 'GP'}, {'StudyTime': 19.1, 'School': 'MS'}]
    sort_students_by_studytime( [{"StudyTime":10.2,"School":"GP"},{"StudyTime":19.1,"School":"MS"},{"StudyTime":12.2,"School":"GP"},{"StudyTime":14.2,"School":"GP"}], "D")) 
    >>>[{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 14.2, 'School': 'GP'}, {'StudyTime': 12.2, 'School': 'GP'}, {'StudyTime': 10.2, 'School': 'GP'}]
    '''
    # check if "StudyTime" is a key in each dictionary
    if not all('StudyTime' in student for student in students_list):
        print('"StudyTime" key is not present')
        return students_list
    #Sorting Algorithms
    n = len(students_list)
    for i in range(n - 1):
        min_max_index = i
        for j in range(i + 1, n):
            if order == 'A':
                if students_list[j]['StudyTime'] < students_list[min_max_index]['StudyTime']:

                    min_max_index = j
            else:
                if students_list[j]['StudyTime'] > students_list[min_max_index]['StudyTime']:

                    min_max_index = j
        if min_max_index != i:
            students_list[i], students_list[min_max_index] = students_list[min_max_index], students_list[i]

    return students_list
#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(student_list: list, order: str) -> list:
        """
        this code accepts two parameters the 1st being a list of dictionaries and the second beign either A or D (ascending and descending respectively)
        the function then returns the average of the students grades and prints it in either ascending or descending order
        
        Parameter:
        input 1 must be a list of dictionaries 
        input 2 can only be 'A' or 'D'
        
        Examples:
        >>>sort_students_g_avg_insertion( [{"G_Avg":12.4,"School":"GP"}, {"G_Avg":11.3,"School":"MS"}], "A")
        [{'G_Avg': 11.3, 'School': 'GP'}, {'G_Avg': 12.4, 'School': 'MS'}]
        >>>sort_students_g_avg_insertion( [{"G_Avg":5.6,"School":"GP"}, {"G_Avg":12.4,"School":"MS"}, {"G_Avg":2.4,"School":"MS"}], "D")
        [{'G_Avg': 12.4, 'School': 'GP'}, {'G_Avg': 5.6, 'School': 'MS'}, {'G_Avg': 2.4, 'School': 'MS'}]
        >>>sort_students_g_avg_insertion( [{"G_Avg":19.2,"School":"GP"}, {"G_Avg":7.8,"School":"MS"}, {"G_Avg":2.4,"School":"MS"}, {"G_Avg":3.6,"School":"GP"}], "D")
        [{'G_Avg': 19.2, 'School': 'GP'}, {'G_Avg': 7.8, 'School': 'MS'}, {'G_Avg': 3.6, 'School': 'MS'}, {'G_Avg': 2.4, 'School': 'GP'}]
        """
        for i in range(1, len(student_list)):
                if 'G_Avg' in student_list[i]:
                        key = student_list[i].get('G_Avg')
                else:
                        print('"G_Avg" key is not present')
                        return student_list
                j = i - 1

                if order == "A":
                        while j >= 0 and key < student_list[j].get('G_Avg'):
                                student_list[j + 1]['G_Avg'] = student_list[j].get('G_Avg')
                                student_list[j + 1]['G_Avg'] = student_list[j].get('G_Avg')
                                j -= 1
                        student_list[j + 1]['G_Avg'] = key

                elif order == "D":
                        while j >= 0 and key > student_list[j].get('G_Avg'):
                                student_list[j + 1]['G_Avg'] = student_list[j].get('G_Avg')
                                student_list[j + 1]['G_Avg'] = student_list[j].get('G_Avg')
                                j -= 1
                        student_list[j + 1]['G_Avg'] = key

        return student_list

#==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(lst_students: list, direction_order: str) -> list:
    """Uses the bubble sort algorithm to sort the dictionaries in either an ascending or descending order as selected by the user. Sorting is designated by the Failures category - if failures is a key in the dictionary, the function returns the sorted list, if not, the function prints '"Failures key is not present.' and returns the original list.

    Preconditions: direction_order = "A" or "D"

    Precondition: do not enter duplicated entries


    print('"Failures" key is not present.')
                lst_students = lst_students


    Examples:
    >>>sort_students_failures_bubble([{"Failures":10, "School":"GP"}, {"Failures":19, "School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]

    >>>sort_students_failures_bubble([{"Failures":2, "School":"GP"}, {"Failures":9, "School":"GP"}, {"Failures":21, "School":"GP"}, {"Failures":7, "School":"GP"}], "A")
    [{'Failures': 2, 'School': 'GP'}, {'Failures': 7, 'School': 'GP'}, {'Failures': 9, 'School': 'GP'}, {'Failures': 21, 'School': 'GP'}]

    >>>sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Failures" key is not present. 
    [{'School':'GP'}, {'School':'MS'}]
    """

    swap = True
    while swap:
        swap = False
        for i in range(len(lst_students) - 1):
            if "Failures" not in lst_students[i]:
                print('"Failures" key is not present.')
                lst_students = lst_students
            elif direction_order == 'A':
                if lst_students[i]['Failures'] > lst_students[i + 1]['Failures']:
                    # swap the places of the dictionary
                    posit = lst_students[i]
                    lst_students[i] = lst_students[i + 1]
                    lst_students[i + 1] = posit
                    swap = True
            elif direction_order == 'D':
                if lst_students[i]['Failures'] < lst_students[i + 1]['Failures']:
                    # swap the places of the dictionary
                    posit = lst_students[i]
                    lst_students[i] = lst_students[i + 1]
                    lst_students[i + 1] = posit
                    swap = True
    return lst_students
#==========================================#
# Place your sort function after this line


def sort(student_info: list, order: str, attribute: str) -> list:
    """Sorts the given list by the chosen order(Ascending/Descending) and by the chosen attribute(Age, StudyTime, G_Avg, Failures) with bubble sorting technique
    if attribute is not valid prints cannot be sorted by "attribute" and returns the list
    
    Examples:
    >>>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]
    >>>sort( [{"StudyTime":10.2,"School":"GP"},{"StudyTime":19.1,"School":"MS"}], "A","StudyTime")
    [{'StudyTime': 10.2, 'School': 'GP'}, {'StudyTime': 19.1, 'School': 'MS'}]
    """
    if attribute == "Age":
        return sort_students_age_bubble(student_info, order)
    elif attribute == "StudyTime":
        return sort_students_time_selection(student_info, order)
    elif attribute == "G_Avg":
        return sort_students_g_avg_insertion(student_info, order)
    elif attribute == "Failures":
        return sort_students_failures_bubble(student_info, order)
    else:
        print("Cannot be sorted by", '"', attribute, '"')
        return student_info
# Do NOT include a main script in your submission

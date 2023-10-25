# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Anneli Sheridan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101269116"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#
# Place your script for your batch_UI after this line


def batch_UI():
    """
    Takes user input as a text file, which contains information called as well as 4 commands. 

    Preconditions: we assume the text file called is properly formatted.

    Example text file:
    L;student-mat.csv;School;GP
    S;Age;D;N
    H;StudyTime

    Corresponser interface:
    Please enter the name of the file where your commands are stored: 
    batch_file.txt
    Data loaded.
    Data sorted. <<<You selected not to display>>>
    <<<Histograms with Study Time will be shown.>>>
    """
    import load_data
    import sort
    import histogram
    import matplotlib
    import numpy
    import scipy

    userinput = input(
        "Please enter the name of the file where your commands are stored: \n")

    file = open(userinput, "r")

    b_list = []
    for line in file:
        lst = line.strip("\n").split(";")
        b_list += lst

    for item in range(len(b_list)):
        if b_list[item] == "L":
            data_1 = open(b_list[item + 1], "r")
            data_2 = str(b_list[item + 1])

    val1 = (b_list[2])
    val2 = (b_list[3])
    list_used = load_data.load_data(data_2, (val1, val2))
    print("Data loaded.")

    if b_list[4] == "S":
        if b_list[5] == "G_Avg":
            sorted_list = sort.sort_students_g_avg_insertion(
                list_used, b_list[6])
        elif b_list[5] == "Failures":
            sorted_list = sort.sort_students_failures_bubble(
                list_used, b_list[6])
        elif b_list[5] == "StudyTime":
            sorted_list = sort.sort_students_time_selection(
                list_used, b_list[6])
        elif b_list[5] == "Age":
            sorted_list = sort.sort_students_age_bubble(
                list_used, b_list[6])
    if b_list[7] == "Y":
        print("Data sorted.", sorted_list)
    elif b_list[7] == "N":
        print("Data sorted. <<<You selected not to display>>>")

    for i in range(len(b_list)):
        if b_list[i] == "H":
            histo = histogram.histogram(list_used, b_list[i + 1])

    for i in range(len(b_list)):
        if b_list[i] == "C":
            graph = curve_fit.curve_fit(list_used, b_list[i + 1])


batch_UI()

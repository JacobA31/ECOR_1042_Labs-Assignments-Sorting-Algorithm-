# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Spencer Edmonds"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259835"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "111"

#==========================================#
# Place your script for your text_UI after this line
"""
This module allows users to select from 5 options, L loads data by file name and by filter, S sorts data by filter in either ascending or descending order,
C makes a curve of best fit for the loaded data, H makes a histogram from the loaded data and finally E exits the program

Preconditions: 
follow printed instructions, none

Examples
>>>Please enter command : L
Please enter file name : student-mat.csv
Please enter filter attribute : School
Enter attribute value : MB
[{'Age': '16', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {another element}]
>>>Please enter command : S
Sorting attributes : 
Age, StudyTime, Failures, G_Avg
Enter Sorting Attribute : Age
Enter order (Ascending : A) or (Descending : D) : A
Data Sorted, Do you want to display the data Y / N : Y
[{'Age': '15', 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {Another element}]
>>>Please enter command : S
Sorting attributes : 
Age, StudyTime, Failures, G_Avg
Enter Sorting Attribute : Age
Enter order (Ascending : A) or (Descending : D) : D
Data Sorted, Do you want to display the data Y / N : Y
[{'Age': '19', 'StudyTime': 2.0, 'Failures': 3, 'Health': 5, 'Absences': 2, 'G1': 7, 'G2': 8, 'G3': 9}, {another element}]
"""

import sort
import load_data
import histogram
import curve_fit

print("Available commands:")
print("L : Load Data")
print("S : Sort Data")
print("C : Curve Fit")
print("H : Histogram")
print("E : Exit")

n = True
file = ""
loaded = []

while n == True:
    command = input("Please enter command : ").upper()
    
    if command == "L":
        file = input("Please enter file name : ")
        att = input("Please enter filter attribute : ")
        
        if att.upper() == "ALL":
            print("Data Successfully loaded")
            
            loaded = load_data.load_data(file, ("ALL", -1))
            
            print(loaded)
        
        else:
            val = input("Enter attribute value : ")
            valid = True
            
            while valid:
                loaded = load_data.load_data(file, (att, val))
                
                if len(loaded) == 0:
                    att = input("Please enter valid key attribute : ")
                
                else:
                    valid = False
                    print(loaded)
        
    elif command == "S":
        if file == "":
            print("Load file before running S command")
        
        else:
            print("Sorting attributes : ")
            print("Age, StudyTime, Failures, G_Avg")
            
            att_sort = input("Enter Sorting Attribute : ")
            order = input("Enter order (Ascending : A) or (Descending : D) : ")
            
            if att_sort == "G_Avg":
                g_avg = load_data.add_average(file)
                att_sorted = sort.sort(g_avg, order, att_sort)
            
            else:
                att_sorted = sort.sort(loaded, order, att_sort)
            
            data = input("Data Sorted, Do you want to display the data Y / N : ")
            
            if data == "Y":
                print(att_sorted)
    
    elif command == "C":
        att_fit = input("Enter attribute for desired best fit : ")
        poly = input("Enter Order of polynomial : ")
        
        equation = curve_fit.curve_fit(att_fit, poly)
        
        print(equation)
        
    elif command == "H":
        plot = input("Enter attribute for desired plotting : ")
        
        histo = histogram.histogram(plot)
        
        print(histo)
        
    elif command == "E":
        n = False
    
    else:
        print("Command Invalid")
        
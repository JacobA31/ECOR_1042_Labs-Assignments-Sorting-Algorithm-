# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jacob Aydin"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101264856"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#
# Place your curve_fit function after this line
import numpy as np


def curve_fit(data: list, attribute: str, deg: int) -> str:
    """the function takes in a list of dictionaries containing data about student grades, a string indicating the attribute to compare averages to, and an integer representing the degree of the polynomial to fit to the data. It calculates the average grade for each level of the specified attribute, fits a polynomial to the averages, and returns a string representation of the equation of the best fit
    
    Examples:
    >>>curve_fit([{'School': 'A', 'G_Avg': 85, 'Health': 1},{'School': 'B', 'G_Avg': 70, 'Health': 2},{'School': 'C', 'G_Avg': 90, 'Health': 1},{'School': 'A', 'G_Avg': 75, 'Health': 3},{'School': 'B', 'G_Avg': 80, 'Health': 2},{'School': 'C', 'G_Avg': 95, 'Health': 3},],'Health',5)
    'y = 11.25x^2-46.25x+122.5'
    >>>curve_fit([{'School': 'A', 'G_Avg': 2, 'Health': 0},{'School': 'B', 'G_Avg': 3, 'Health': 1},{'School': 'C', 'G_Avg': 2, 'Health': 2}],'Health',2)
    'y = -1.0x^2+2.0x+2.0'
    >>>curve_fit([{'G_Avg':-481, 'G1':4},{'G_Avg':-1, 'G1':1},{'G_Avg':-25, 'G1':2}],"G1",5)
    'y = -68.0x^2+180.0x-113.0'
    """
    G_Avg = {}
    for i in data:
        G_Avg[i[attribute]] = []
    for i in data:
        G_Avg[i[attribute]] += [i['G_Avg']]
    for key in G_Avg:
        if len(G_Avg[key]) != 0:
            G_Avg[key] = round(sum(G_Avg[key]) / len(G_Avg[key]), 2)
        else:
            del G_Avg[i[attribute]]

    x = list(G_Avg.keys())
    y = list(G_Avg.values())

    if deg < len(x) - 1:
        a = np.polyfit(x, y, deg)
    else:
        a = np.polyfit(x, y, len(x) - 1)
    k = a
    a = []
    for i in range(len(k)):
        a.append(round(k[i], 2))

    st = []

    for i in range(len(a)):
        if i == 0:
            st.append(str(a[i]) + "x^" + str(len(a) - 1 - i))

        elif i < len(a) - 2 and i > 0:
            if a[i] != 1 and a[i] != 0 and a[i] < 0:
                st.append(str(a[i]) + "x^" + str(len(a) - 1 - i))
            elif a[i] != 1 and a[i] != 0 and a[i] > 1:
                st.append("+" + str(a[i]) + "x^" + str(len(a) - 1 - i))
            elif a[i] == 1:
                st.append("x^" + str(len(a) - i - 1))

        elif i < len(a) - 1 and i > 0:
            if a[len(a) - 2] != 1 and a[len(a) - 2] != 0 and a[len(a) - 2] < 0:
                st.append(str(a[len(a) - 2]) + "x")
            elif a[len(a) - 2] != 1 and a[len(a) - 2] != 0 and a[len(a) - 2] > 1:
                st.append("+" + str(a[len(a) - 2]) + "x")
            elif a[len(a) - 2] == 1:
                st.append("x")

        elif i < len(a) and i > 0:
            if a[len(a) - 1] != 1 and a[len(a) - 1] != 0 and a[len(a) - 1] < 0:
                st.append(str(a[len(a) - 1]))
            elif a[len(a) - 1] != 1 and a[len(a) - 1] != 0 and a[len(a) - 1] > 1:
                st.append("+" + str(a[len(a) - 1]))

        eq = ''.join(st)
    return "y = " + eq
# Do NOT include a main script in your submission

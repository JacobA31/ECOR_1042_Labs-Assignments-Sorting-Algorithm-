# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Pagalavan Sivakumar"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101262555"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#
import matplotlib.pyplot as plt

def histogram(data:list, attribute:str):
    """Generates a histogram of the given attribute from a list of dictionaries.
    precondition:
    data has to be a list of dictonaries
    attribute is a quality  
      """
    counts = {}
    for item in data:
        value = item[attribute]
        if isinstance(value, float):
            key = round(value)
        else:
            key = value
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    
    labels = sorted(counts.keys())
    values = [counts[label] for label in labels]
    
    plt.bar(labels, values)
    plt.xlabel(attribute)
    plt.ylabel('Frequency')
    plt.title('Histogram of ' + attribute)
    plt.show()


    return None

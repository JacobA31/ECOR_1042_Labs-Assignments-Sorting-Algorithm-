# ECOR 1042 Lab 4 - Individual submission for test1 function

#import check module here
import check
#import load_data module here
import load_data
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jacob Aydin"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101264856"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#
#Do not modify the code alreayd provided.


def test_return_list():
    #Complete the function with your test cases

    #test that student_school_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'GP'), list), True)
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'CF'), list), True)
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'MB'), list), True)

    #test that student_age_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_age_list('student-test.csv', 15), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 17), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 18), list), True)

    #test that student_health_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_health_list('student-test.csv', 4), list), True)
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 3), list), True)
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 5), list), True)

    #test that student_failures_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 0), list), True)
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 1), list), True)
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 2), list), True)

    #test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('School', 'GP')), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('School', 'MB')), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Health', 3)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Age', 16)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Failures', 3)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('All', -1)), list), True)

    #test that add_average returns a list (3 different test cases required)"""

    check.equal(isinstance(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]), list), True)
    check.equal(isinstance(load_data.add_average([{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}]), list), True)
    check.equal(isinstance(load_data.add_average([{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]), list), True)

    check.summary()

# Do NOT include a main script in your submission

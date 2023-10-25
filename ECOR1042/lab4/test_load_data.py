# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
import load_data
# Update "" with your the name of the active members of the team
__author__ = "Jacob Aydin - Spencer Edmonds - Anneli Sheridan - Pagalavan Sivakumar"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#

# Place test_return_list function here


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

    check.equal(isinstance(load_data.add_average(load_data.student_age_list('student-test.csv', 15)), list), True)
    check.equal(isinstance(load_data.add_average(load_data.student_failures_list('student-test.csv', 2)), list), True)
    check.equal(isinstance(load_data.add_average(load_data.student_health_list('student-test.csv', 5)), list), True)

    check.summary()

# Place test_return_list_correct_lenght function here


def test_return_list_correct_lenght():
    #Complete the function with your test cases

    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_school_list('student-test.csv', 'GP')), 3)
    check.equal(len(load_data.student_school_list('student-test.csv', 'MB')), 2)
    check.equal(len(load_data.student_school_list('student-test.csv', 'MS')), 4)

    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_age_list('student-test.csv', 15)), 3)
    check.equal(len(load_data.student_age_list('student-test.csv', 18)), 4)
    check.equal(len(load_data.student_age_list('student-test.csv', 21)), 0)

    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_health_list('student-test.csv', 1)), 1)
    check.equal(len(load_data.student_health_list('student-test.csv', 5)), 3)
    check.equal(len(load_data.student_health_list('student-test.csv', 3)), 8)

    #test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(load_data.student_failures_list('student-test.csv', 2)), 2)
    check.equal(len(load_data.student_failures_list('student-test.csv', 0)), 11)
    check.equal(len(load_data.student_failures_list('student-test.csv', 1)), 1)

    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data('student-test.csv', ('Age', 15))), 3)
    check.equal(len(load_data.load_data('student-test.csv', ('Health', 2))), 0)
    check.equal(len(load_data.load_data('student-test.csv', ('School', 'BD'))), 3)
    check.equal(len(load_data.load_data('student-test.csv', ('Failures', 2))), 2)
    check.equal(len(load_data.load_data('student-test.csv', ('Age', 40))), 0)
    check.equal(len(load_data.load_data('student-test.csv', ('All', 5))), 15)

    #test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average(load_data.student_failures_list('student-test.csv', 2))), 2)
    check.equal(len(load_data.add_average(load_data.student_health_list('student-test.csv', 5))), 3)
    check.equal(len(load_data.add_average(load_data.student_age_list('student-test.csv', 15))), 3)

    check.summary()

#Place test_return_correct_dict_inside_list function here


testfile = "student-test.csv"


def test_return_correct_dict_inside_list():
    #Complete the function with your test cases

    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_school_list(testfile, "GP")[0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_school_list(testfile, "GP")[-1], {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.student_school_list(testfile, "GP")[1], {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})

    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal(load_data.student_age_list(testfile, 15)[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.student_age_list(testfile, 15)[-1], {'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})
    check.equal(load_data.student_age_list(testfile, 15)[1], {'School': 'MB', 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12})

    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.student_health_list(testfile, 3)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_health_list(testfile, 3)[-1], {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12})
    check.equal(load_data.student_health_list(testfile, 3)[1], {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_failures_list(testfile, 0)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_failures_list(testfile, 0)[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.student_failures_list(testfile, 0)[1], {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(load_data.load_data(testfile, ('Age', 18))[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data(testfile, ('Age', 18))[-1], {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.load_data(testfile, ('Health', 3))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data(testfile, ('Health', 5))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.load_data(testfile, ('School', 'GP'))[0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data(testfile, ('School', 'MS'))[-1], {'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})

     #test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.add_average(load_data.load_data(testfile, ("All", 1)))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67})
    check.equal(load_data.add_average(load_data.load_data(testfile, ("All", 0)))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33})
    check.equal(load_data.add_average(load_data.load_data(testfile, ("All", 6)))[1], {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33})

    check.summary()
#Place test_add_average function here


def test_add_average():
    # Complete the function with your test cases

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)

    # test that the function returns an empty list when it is called whith an empty list

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)

    # test that the G_Avg value is properly calculated  (5 different test cases required)

    import string
    import load_data
    import check
    from load_data import student_school_list
    from load_data import student_age_list
    from load_data import student_health_list
    from load_data import student_failures_list
    from load_data import add_average
    from load_data import load_data

    # The following checks ensure that add_average does not change the size of the list

    check.equal(len(add_average(student_school_list("student-test.csv", "MB"))),
                len(student_school_list("student-test.csv", "MB")))  # Case 1: 'School' is not a key of the dictionary

    check.equal(len(add_average(student_health_list("student-test.csv", 3))),
                len(student_health_list("student-test.csv", 3)))  # Case 2: 'Health' is not a key of the dictionary

    check.equal(len(add_average(student_age_list("student-test.csv", 18))),
                len(student_age_list("student-test.csv", 18)))  # Case 3: 'Age' is not a key of the dictionary

    check.equal(len(add_average(student_failures_list('student-test.csv', 0))),
                len(student_failures_list('student-test.csv', 0)))  # Case 4: 'Failures' is not a key of the dictionary

    check.equal(len(add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
                                  'Health': 3, 'Absences': 7, 'G1': 2, 'G2': 8, 'G3': 4}])), 1)  # Case 5: All keys present

    check.equal(len(add_average([])), 0)  # Case 6: Empty list

    # Some lists to make the following code easier to read

    list_school = student_school_list("student-test.csv", "MB")
    list_aa_school = add_average(
        student_school_list("student-test.csv", "MB"))

    list_health = student_health_list("student-test.csv", 3)
    list_aa_health = add_average(student_health_list("student-test.csv", 3))

    list_age = student_age_list("student-test.csv", 18)
    list_aa_age = add_average(student_age_list("student-test.csv", 18))

    list_failures = student_failures_list('student-test.csv', 0)
    list_aa_failures = add_average(
        student_failures_list('student-test.csv', 0))

    list_case5 = [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3,
                                   'Absences': 6, 'G1': 6, 'G2': 6, 'G3': 6}]
    list_aa_case5 = add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3,
                                  'Absences': 6, 'G1': 6, 'G2': 6, 'G3': 6}])

    # The following checks ensure that the number of keys has increased by one

    # Case 1: 'School' is not a key of the dictionary
    check.equal(len(list_aa_school[0]), len(list_school[0]) + 1)

    # Case 2: 'Health' is not a key of the dictionary
    check.equal(len(list_aa_health[0]), len(list_health[0]) + 1)

    # Case 3: 'Age' is not a key of the dictionary
    check.equal(len(list_aa_age[0]), len(list_age[0]) + 1)

    # Case 4: 'Failures' is not a key of the dictionary
    check.equal(len(list_aa_failures[0]), len(list_failures[0]) + 1)

    # Case 5: All keys present
    check.equal(len(list_aa_case5[0]), len(list_case5[0]) + 1)

    # The following checks ensure the output value is accurate
    check.equal(int(list_aa_school[0]['G_Avg']), int((int(list_school[0]['G1']) +
                int(list_school[0]['G2']) + int(list_school[0]['G3'])) // 3))  # Case 1: 'School' is not a key of the dictionary

    check.equal(int(list_aa_health[-1]['G_Avg']), int(((int(list_health[-1]['G1'])) +
                                                      (int(list_health[-1]['G2'])) + (int(list_health[-1]['G3']))) // 3))  # Case 2: 'Health' is not a key of the dictionary

    check.equal(int(list_aa_age[0]['G_Avg']), int((int(list_age[0]['G1']) +
                int(list_age[0]['G2']) + int(list_age[0]['G3'])) // 3))  # Case 3: 'Age' is not a key of the dictionary

    check.equal(int(list_aa_failures[0]['G_Avg']), int((int(list_failures[0]['G1']) +
                int(list_failures[0]['G2']) + int(list_failures[0]['G3'])) // 3))  # Case 4: 'Failures' is not a key of the dictionary

    check.equal(int(list_aa_case5[0]['G_Avg']), int((int(list_case5[0]['G1']) +
                int(list_case5[0]['G2']) + int(list_case5[0]['G3'])) // 3))  # Case 5: All keys present

    check.summary()


# Do NOT include a main script in your submission

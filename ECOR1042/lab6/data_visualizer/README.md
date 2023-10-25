#ECOR-1042-Winter 2023 README for LAB PROJECT 
Date: 04/11/2023 
Software: Python version 3.11.2 
Contact information: Jacob Aydin - jacobaydin@cmail.carleton.ca

#Description \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

The purpose of the software is to give students information to the user.
The user can select 4 different attributes (School, Health, Age,
Failures) and specify the value for the attribute. The software will
give the students information that has the same value as the attribute.
The user can also get all of the students' information. Then the user
can sort the list of information by the desired attribute and desired
order (ascending/descending). Lastly, the user can see the equation of
students' average grades and observe a histogram of students' average
grades.

#Dependencies \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-Python 3.11.2 
-Numpy 
-Matplotlib 
-Wing101

#Installation \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1- Unzip the file downloaded from Brightspace
2- Open Wing101
3- From the file drag the batch_UI.py or text_UI.py file onto the Wing101 
app (it won't matter which one the user choose since they are identical)
4- Run the software by clicking the green triangle next to search button
5- The user should now be able to see the interface

#Usage \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

See the video tutorial for explanation of how to use the software

#Credits \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Team members and the functions they implemented

Jacob Aydin
-student_school_list
-load_data
-test_return_list
-sort_students_age_bubble
-sort
-curve_fit
-README

Spencer Edmonds
-student_age_list
-test_return_list_correct_length
-sort_students_g_avg_insertion
-text_UI.py

Anneli Sheridan
-student_failures_list 
-test_add_average
-sort_students_failures_bubble
-batch_UI.py 

Pagalavan Sivakumar
-student_health_list
-add_average
-test_return_correct_dict_inside_list
-sort_students_time_selection
-histogram

#License \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MIT License

Copyright (c) \[year\] \[fullname\]

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

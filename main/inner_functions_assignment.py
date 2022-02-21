"""
Assignment: Inner Functions Assignment
Program: inner_functions_assignment.py
Author: Colby Boell
Last date modified: 02/20/2022

The purpose of this program is to have a function that accepts a list of measurements for a rectangle
and returns a string with perimeter and area. The two inner functions accepts the list as perimeter
area(a_list) calculates the area and perimeter(_list) calculates the perimeter. The outer measurement
function will build and return a string with the perimeter and area results.
Also do the same for a square to get the perimeter and area.
"""


# outer function to calculate perimeter, accepts a list as a parameter
def measurements(a_list):
    # inner function
    def perimeter(b_list):
        calculated_perimeter = 0
        # for square
        if len(b_list) == 1:
            calculated_perimeter = a_list[0] * 4
        # for rectangle
        elif len(b_list) == 2:
            calculated_perimeter = (a_list[0] + a_list[1]) * 2
        # returns result
        return calculated_perimeter

    # inner function to calculate area, accepts a list as a parameter
    def area(b_list):
        calculated_area = 0
        # for square
        if len(b_list) == 1:
            calculated_area = a_list[0] * a_list[0]
        # for rectangle
        elif len(b_list) == 2:
            calculated_area = a_list[0] * a_list[1]
        # returns result
        return calculated_area
    # variables that call the inner functions
    the_area = area(a_list)
    the_perimeter = perimeter(a_list)
    # the outer function returns a string to the main
    return f'Perimeter = {the_perimeter} Area = {the_area}'


# main
if __name__ == '__main__':
    # creates list variable
    rectangle = [2.1, 3.4]
    # variable that calls function
    result = measurements(rectangle)
    # prints result
    print(result)
    # creates variables and prints results below
    square = [3.5]
    result = measurements(square)
    print(result)

"""
Test results:
Perimeter = 11.0 Area = 7.14
Perimeter = 14.0 Area = 12.25
"""

# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 3
Version: v0.1.0
"""

def distances_from_average(test_list):
    # Calculate the average
    average = sum(test_list) / len(test_list)

    # Calculate the signed distances from the average, rounded to 2 decimal places
    differences = [round(average - value, 2) for value in test_list]

    # Convert floating point number approximately equal to 0.0 to integer 0 using a tolerance
    tolerance = 1e-9  # Small tolerance for floating-point comparison
    differences = [0 if abs(diff) < tolerance else diff for diff in differences]

    return differences

distances_from_average([55, 95, 62, 36, 48])          # [4.2, -35.8, -2.8, 23.2, 11.2]
distances_from_average([1, 1, 1, 1, 1])               # [0, 0, 0, 0, 0]
distances_from_average([1, -1, 1, -1, 1, -1])         # [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]
distances_from_average([1, -1, 1, -1, 1])             # [-0.8, 1.2, -0.8, 1.2, -0.8]
distances_from_average([2, -2])                       # [-2.0, 2.0]
distances_from_average([1])                           # [0]
distances_from_average([123, -65, 32432, -353, -534]) # [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]

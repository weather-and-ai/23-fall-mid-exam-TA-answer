# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 4
Version: v0.1.0
"""

import unittest

def multiply(n):
    if n == 0:  # If the number is 0, the result will be 0 regardless of its digit count
        return 0

    # Calculate the power of 5 raised to the number of digits in the absolute value of the input number
    power = abs(n)
    power_of_five = 5 ** len(str(power))

    # Multiply the number by the calculated power of 5 and return the result with the sign of the input number
    result = n * power_of_five
    return result

multiply(10)  #250
multiply(5)   #25
multiply(200) #25000
multiply(0)   #0
multiply(-2)  #-10

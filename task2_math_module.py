# Task 2: Using the Math Module for Calculations

import math

try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive number for logarithm and square root.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)  # input is in radians

        print(f"Square root of {number}: {square_root}")
        print(f"Natural logarithm of {number}: {natural_log}")
        print(f"Sine of {number} (in radians): {sine_value}")

except ValueError:
    print("Invalid input! Please enter a numeric value.")

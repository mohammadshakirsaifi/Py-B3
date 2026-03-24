# math_functions.py
# Custom math functions module for demonstration

import math

def custom_factorial(n):
    """Custom factorial function with detailed output"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    result = 1
    steps = []
    
    for i in range(1, n + 1):
        result *= i
        steps.append(f"{i} × ")
    
    # Format steps string
    if steps:
        steps_str = "".join(steps)[:-3]  # Remove last " × "
        steps_str += f" = {result}"
    else:
        steps_str = "1"
    
    return result, steps_str

def get_number_properties(num):
    """Get various mathematical properties of a number"""
    properties = {}
    
    # Basic properties
    properties["Absolute Value"] = abs(num)
    properties["Sign"] = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    properties["Is Integer"] = num == int(num)
    
    # Number type
    properties["Even"] = num % 2 == 0 if properties["Is Integer"] else "N/A"
    properties["Odd"] = not properties["Even"] if properties["Is Integer"] else "N/A"
    properties["Prime"] = is_prime(num) if num > 0 and properties["Is Integer"] else "N/A"
    
    # Mathematical properties
    properties["Square"] = num ** 2
    properties["Cube"] = num ** 3
    properties["Square Root"] = math.sqrt(num) if num >= 0 else "Undefined"
    
    return properties

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Task 2: Using the Math Module for Calculations
# This program demonstrates various mathematical operations using Python's math module

import math

def get_valid_float(prompt):
    """
    Get and validate user input for a floating-point number
    
    Args:
        prompt (str): Input prompt to display
    
    Returns:
        float: Validated number
    """
    while True:
        try:
            value = input(prompt).strip()
            
            if not value:
                print("Error: No input provided. Please enter a number.")
                continue
            
            return float(value)
            
        except ValueError:
            print(f"Error: '{value}' is not a valid number. Please enter a numeric value.")

def calculate_square_root(number):
    """
    Calculate square root of a number
    
    Args:
        number (float): Input number
    
    Returns:
        float: Square root
    """
    if number < 0:
        return None, "Square root is not defined for negative numbers in real numbers"
    return math.sqrt(number), None

def calculate_logarithm(number):
    """
    Calculate natural logarithm of a number
    
    Args:
        number (float): Input number
    
    Returns:
        float: Natural logarithm
    """
    if number <= 0:
        return None, "Logarithm is only defined for positive numbers"
    return math.log(number), None

def calculate_sine(number):
    """
    Calculate sine of a number (in radians)
    
    Args:
        number (float): Input number
    
    Returns:
        float: Sine value
    """
    return math.sin(number), None

def calculate_additional_operations(number):
    """
    Calculate additional mathematical operations for demonstration
    
    Args:
        number (float): Input number
    
    Returns:
        dict: Dictionary of additional operations and their results
    """
    operations = {}
    
    try:
        # Exponential function
        operations["Exponential (e^x)"] = math.exp(number)
        
        # Cosine
        operations["Cosine (radians)"] = math.cos(number)
        
        # Tangent
        operations["Tangent (radians)"] = math.tan(number)
        
        # Degrees to radians and vice versa
        operations["Degrees to Radians"] = math.radians(number)
        operations["Radians to Degrees"] = math.degrees(number)
        
        # Ceiling and floor
        operations["Ceiling"] = math.ceil(number)
        operations["Floor"] = math.floor(number)
        
        # Power functions
        operations[f"Square ({number}²)"] = math.pow(number, 2)
        operations[f"Cube ({number}³)"] = math.pow(number, 3)
        
    except Exception as e:
        operations["Error"] = str(e)
    
    return operations

def display_results(number, operations):
    """
    Display the calculation results in a formatted way
    
    Args:
        number (float): Original input number
        operations (dict): Dictionary of operations and their results
    """
    print("\n" + "=" * 60)
    print(f"MATHEMATICAL OPERATIONS FOR NUMBER: {number}")
    print("=" * 60)
    
    for operation, (result, error) in operations.items():
        if error:
            print(f"\n{operation:25} : {error}")
        else:
            print(f"\n{operation:25} : {result:.6f}")
            
            # Show some additional info for specific operations
            if operation == "Square Root":
                print(f"{' ':27}({result:.6f} × {result:.6f} = {result*result:.6f})")
            elif operation == "Logarithm (natural)":
                print(f"{' ':27}(e^{result:.6f} = {math.exp(result):.6f})")
            elif operation == "Sine":
                angle_deg = math.degrees(number)
                print(f"{' ':27}({angle_deg:.2f}° in degrees)")

def main():
    """
    Main function to run the math operations program
    """
    print("=" * 60)
    print("TASK 2: MATHEMATICAL OPERATIONS USING MATH MODULE")
    print("=" * 60)
    print("\nThis program performs various mathematical operations")
    print("using Python's built-in math module.")
    
    while True:
        try:
            # Get number from user
            print("\n" + "-" * 60)
            number = get_valid_float("Enter a number: ")
            
            print(f"\nProcessing number: {number}")
            
            # Perform calculations
            operations = {}
            
            # Required operations from task
            sqrt_result, sqrt_error = calculate_square_root(number)
            operations["Square Root"] = (sqrt_result, sqrt_error)
            
            log_result, log_error = calculate_logarithm(number)
            operations["Logarithm (natural)"] = (log_result, log_error)
            
            sine_result, sine_error = calculate_sine(number)
            operations["Sine"] = (sine_result, sine_error)
            
            # Additional operations for demonstration
            additional_ops = calculate_additional_operations(number)
            
            # Display results
            display_results(number, operations)
            
            # Ask if user wants to see additional operations
            show_more = input("\nDo you want to see additional mathematical operations? (yes/no): ").strip().lower()
            
            if show_more in ['yes', 'y']:
                print("\n" + "-" * 60)
                print("ADDITIONAL MATHEMATICAL OPERATIONS:")
                print("-" * 60)
                
                for op_name, result in additional_ops.items():
                    if isinstance(result, (int, float)):
                        print(f"{op_name:25} : {result:.6f}")
                    else:
                        print(f"{op_name:25} : {result}")
            
            # Show mathematical constants
            print("\n" + "-" * 60)
            print("MATHEMATICAL CONSTANTS FROM MATH MODULE:")
            print("-" * 60)
            print(f"π (pi)        : {math.pi:.10f}")
            print(f"e (Euler's)   : {math.e:.10f}")
            print(f"τ (tau)       : {math.tau:.10f}")
            print(f"∞ (infinity)  : {math.inf}")
            
            # Ask if user wants to continue
            print("\n" + "-" * 60)
            choice = input("Do you want to perform operations on another number? (yes/no): ").strip().lower()
            
            if choice not in ['yes', 'y']:
                print("\nThank you for using the Math Operations Calculator!")
                print("=" * 60)
                break
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()

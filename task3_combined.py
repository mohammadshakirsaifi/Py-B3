# Combined Program: Functions and Modules Demonstration
# This program combines both factorial calculation and math module operations

import math
from task1_factorial import factorial_iterative, get_valid_number
from task2_math_operations import get_valid_float, calculate_square_root, calculate_logarithm, calculate_sine

def display_menu():
    """
    Display the main menu
    """
    print("\n" + "=" * 60)
    print("COMBINED FUNCTIONS & MODULES DEMONSTRATION")
    print("=" * 60)
    print("\n1. Calculate Factorial")
    print("2. Mathematical Operations (using math module)")
    print("3. Quick Demo (Calculate factorial and math operations for same number)")
    print("4. Exit")
    print("-" * 60)

def quick_demo():
    """
    Perform both factorial and math operations on the same number
    """
    print("\n" + "=" * 60)
    print("QUICK DEMO: FACTORIAL AND MATH OPERATIONS")
    print("=" * 60)
    
    try:
        # Get integer for factorial
        num = int(get_valid_float("Enter an integer number: "))
        
        print(f"\nFor number: {num}")
        print("-" * 40)
        
        # Calculate factorial
        if num >= 0:
            fact = factorial_iterative(num)
            print(f"Factorial: {num}! = {fact}")
        else:
            print("Factorial: Not defined for negative numbers")
        
        # Calculate math operations
        print("\nMathematical Operations:")
        print("-" * 40)
        
        # Square root
        sqrt_result, sqrt_error = calculate_square_root(num)
        if sqrt_error:
            print(f"Square Root: {sqrt_error}")
        else:
            print(f"Square Root: {sqrt_result:.6f}")
        
        # Logarithm
        log_result, log_error = calculate_logarithm(num)
        if log_error:
            print(f"Natural Logarithm: {log_error}")
        else:
            print(f"Natural Logarithm: {log_result:.6f}")
        
        # Sine
        sine_result, _ = calculate_sine(num)
        print(f"Sine ({num} radians): {sine_result:.6f}")
        print(f"Sine ({math.degrees(num):.2f} degrees): {sine_result:.6f}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function for combined program
    """
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Run factorial calculator
            print("\n" + "=" * 60)
            print("FACTORIAL CALCULATOR")
            print("=" * 60)
            number = get_valid_number()
            result = factorial_iterative(number)
            print(f"\nFactorial of {number} is: {result}")
            
        elif choice == '2':
            # Run math operations
            print("\n" + "=" * 60)
            print("MATHEMATICAL OPERATIONS")
            print("=" * 60)
            number = get_valid_float("Enter a number: ")
            
            operations = {}
            sqrt_result, sqrt_error = calculate_square_root(number)
            operations["Square Root"] = (sqrt_result, sqrt_error)
            
            log_result, log_error = calculate_logarithm(number)
            operations["Logarithm"] = (log_result, log_error)
            
            sine_result, _ = calculate_sine(number)
            operations["Sine"] = (sine_result, None)
            
            print("\nResults:")
            print("-" * 40)
            for op_name, (result, error) in operations.items():
                if error:
                    print(f"{op_name}: {error}")
                else:
                    print(f"{op_name}: {result:.6f}")
            
        elif choice == '3':
            # Quick demo
            quick_demo()
            
        elif choice == '4':
            print("\nThank you for using the Combined Functions & Modules Program!")
            print("=" * 60)
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

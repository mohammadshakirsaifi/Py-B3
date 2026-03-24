# Task 1: Calculate Factorial Using a Function
# This program defines a function to calculate factorial using different methods

def factorial_iterative(n):
    """
    Calculate factorial using iterative approach (loop)
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursive approach
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_math(n):
    """
    Calculate factorial using math module (alternative method)
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    import math
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def get_valid_number():
    """
    Get and validate user input for a non-negative integer
    
    Returns:
        int: Validated number
    """
    while True:
        try:
            num = input("Enter a number to calculate factorial: ").strip()
            
            if not num:
                print("Error: No input provided. Please enter a number.")
                continue
            
            num = int(num)
            
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
                print("Please enter a non-negative integer (0 or greater).")
                continue
                
            return num
            
        except ValueError:
            print(f"Error: '{num}' is not a valid integer. Please enter a whole number.")

def main():
    """
    Main function to run the factorial calculator
    """
    print("=" * 50)
    print("TASK 1: FACTORIAL CALCULATOR")
    print("=" * 50)
    
    while True:
        try:
            # Get valid number from user
            number = get_valid_number()
            
            print(f"\nCalculating factorial of {number}...")
            print("-" * 40)
            
            # Calculate factorial using different methods
            print("1. Using iterative method (loop):")
            result_iterative = factorial_iterative(number)
            print(f"   {number}! = {result_iterative}")
            
            print("\n2. Using recursive method:")
            result_recursive = factorial_recursive(number)
            print(f"   {number}! = {result_recursive}")
            
            print("\n3. Using math module:")
            result_math = factorial_math(number)
            print(f"   {number}! = {result_math}")
            
            # Verify all methods give same result
            if result_iterative == result_recursive == result_math:
                print(f"\n✓ All methods agree: Factorial of {number} is: {result_iterative}")
            else:
                print("\n✗ Warning: Different methods gave different results!")
            
            print("\n" + "=" * 50)
            
            # Show factorial sequence
            if number <= 10:  # Limit display for large numbers
                print(f"\nFactorial sequence:")
                print(f"{number}! = ", end="")
                if number == 0:
                    print("1")
                else:
                    for i in range(1, number + 1):
                        if i < number:
                            print(f"{i} × ", end="")
                        else:
                            print(f"{i} = {result_iterative}")
            
            # Ask if user wants to continue
            choice = input("\nDo you want to calculate another factorial? (yes/no): ").strip().lower()
            
            if choice not in ['yes', 'y']:
                print("\nThank you for using the Factorial Calculator!")
                break
            
            print("\n" + "=" * 50 + "\n")
            
        except ValueError as ve:
            print(f"Error: {ve}")
        except RecursionError:
            print("Error: Recursion limit exceeded. The number might be too large for recursive method.")
            print("Try using the iterative method or math module for large numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()

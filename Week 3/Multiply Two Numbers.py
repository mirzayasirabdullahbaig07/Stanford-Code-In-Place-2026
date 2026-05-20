"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    
    # Get inputs
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    
    # Convert to integers
    num1 = int(num1)
    num2 = int(num2)
    
    # Multiply and print result
    result = num1 * num2
    print(result)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
def divide_numbers():
    try:
        # Input two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Try dividing the numbers
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

def read_file(filename):
    try:
        # Try opening and reading a file
        with open(filename, 'r') as file:
            data = file.read()
            print(f"File content:\n{data}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")

# Call functions with error handling
divide_numbers()
read_file('example.txt')

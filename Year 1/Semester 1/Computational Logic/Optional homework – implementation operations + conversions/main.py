import numpy as np
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


# This function performs the specified arithmetic operation on num1 and num2 in the given base
def perform_operation(operation, base, num1, num2):
    """
    Perform a mathematical operation on two numbers in the specified base.

    Parameters:
    operation (int): The operation to be performed. 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division.
    base (int): The base in which the numbers are represented.
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    str: The result of the operation in the specified base.
    """
    # Perform addition if operation is 1
    if operation == 1:
        result = int(str(num1), base) + int(str(num2), base)
    # Perform subtraction if operation is 2
    elif operation == 2:
        result = int(str(num1), base) - int(str(num2), base)
    # Perform multiplication if operation is 3
    elif operation == 3:
        result = int(str(num1), base) * int(str(num2), base)
    # Perform division if operation is 4
    elif operation == 4:
        result = int(str(num1), base) // int(str(num2), base)

    # Convert the result back to the specified base
    result = np.base_repr(result, base=base)
    return result

# This function displays the result of the arithmetic operation
def show_result(operation, base, num1, num2):
    """
    Displays the result of an arithmetic operation on the GUI.

    Parameters:
    - operation (str): The arithmetic operation to be performed.
    - base (int): The base of the numbers involved in the operation.
    - num1 (int): The first number.
    - num2 (int): The second number.

    Returns:
    None
    """
    result = perform_operation(operation, base, num1, num2)
    equation = f"{num1}({base}) {get_operation_symbol(operation)} {num2}({base}) = {result}({base})"
    # Update the result label with the equation
    result_label.config(text=equation, font=("Arial", 20), justify="center")

def get_operation_symbol(operation):
    """
    Returns the symbol corresponding to the arithmetic operation.

    Parameters:
    - operation (str): The arithmetic operation.

    Returns:
    str: The symbol corresponding to the arithmetic operation.
    """
    if operation == 1:
        return "+"
    elif operation == 2:
        return "-"
    elif operation == 3:
        return "*"
    elif operation == 4:
        return "/"
    else:
        return ""



def handle_arithmetic():
    """
    Handles arithmetic operations based on user input.

    This function prompts the user to choose an arithmetic operation, a base, and two numbers.
    It performs the selected arithmetic operation on the given numbers and displays the result.

    Returns:
        None
    """

    # Prompt the user to choose an arithmetic operation
    operation = simpledialog.askinteger("Arithmetic Operations", "Choose operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division by one digit")

    # Check if the operation is valid
    if operation not in [1, 2, 3, 4]:
        messagebox.showerror("Error", "Invalid operation. Please enter a number from 1 to 4.")
        return
    
    # Prompt the user to choose a base
    base = simpledialog.askinteger("Choose Base", "Enter base (2 to 16):")

    # Check if the base is valid
    if base not in range(2, 17):
        messagebox.showerror("Error", "Invalid base. Please enter a number from 2 to 16.")
        return

    # Prompt the user to enter two numbers
    num1 = simpledialog.askstring("Enter Number 1", "Enter the first number:")
    num2 = simpledialog.askstring("Enter Number 2", "Enter the second number:")

    # Check if num1 and num2 are valid for the chosen base
    valid_digits = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(base-10)]
    for num in [num1, num2]:
        if any(digit not in valid_digits for digit in str(num)):
            messagebox.showerror("Error", f"Invalid number. Please enter a number in base {base}.")
            return
        
    # Check if num2 is a one-digit number for division operation
    if operation == 4 and len(str(num2)) != 1:
        messagebox.showerror("Error", "Invalid number. Please enter a one digit number.")
        return

    # Call the show_result function to display the result
    show_result(operation, base, num1, num2)
    print(operation, base, num1, num2)






#CONVERSIONS

def convert_from_base_a_to_base_b(initial_base, final_base, num):
    """
    Convert a number from base a to base b.

    Parameters:
    - initial_base (string): The initial base of the number.
    - final_base (string): The final base to convert the number to.
    - num (str): The number to be converted.

    Returns:
    str: The result of the conversion in the specified base.
    """
    # Convert the number from the initial base to base 10

    num_base_10 = int(num, initial_base)
    # Convert the number from base 10 to the final base
    num_final = np.base_repr(num_base_10, base=final_base)

    return num_final

def addition(num1, num2, base):
    """
    Perform addition of two numbers in the specified base.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        base (int): The base in which the addition should be performed.

    Returns:
        str: The result of the addition in the specified base.
    """
    # Perform addition
    result = int(str(num1), base) + int(str(num2), base)
    # Convert the result back to the specified base
    result = np.base_repr(result, base=base)
    return result

def subtraction(num1, num2, base):
    """
    Perform subtraction of two numbers in the specified base.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        base (int): The base in which the numbers are represented.

    Returns:
        str: The result of the subtraction in the specified base.
    """
    # Perform subtraction
    result = int(str(num1), base) - int(str(num2), base)
    # Convert the result back to the specified base
    result = np.base_repr(result, base=base)
    return result

def multiplication(num1, num2, base):
    """
    Perform multiplication of two numbers in the specified base.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        base (int): The base in which the multiplication is performed.

    Returns:
        str: The result of the multiplication in the specified base.
    """
    # Perform multiplication
    result = int(str(num1), base) * int(str(num2), base)
    # Convert the result back to the specified base
    result = np.base_repr(result, base=base)
    return result

def power(num1, num2, base):
    """
    Calculate the power of a number.

    Args:
        num1 (int): The base number.
        num2 (int): The exponent.
        base (int): The base for modular arithmetic.

    Returns:
        int: The result of raising `num1` to the power of `num2` modulo `base`.
    """
    # Perform power using successive multiplication
    result = 1
    for i in range(num2):
        result = multiplication(result, num1, base)
    return result

def convert_from_base_10_to_base_b(final_base, num):
    """
    Convert a number from base 10 to the final base.

    Parameters:
    final_base (int): The base to convert the number to.
    num (int): The number to be converted.

    Returns:
    str: The converted number in the final base.
    """
    num_final = np.base_repr(num, base=final_base)
    return num_final

def remainder_function(num1, num2, base):
    """
    Calculate the remainder of two numbers in a specified base.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    base (int): The base in which the calculation is performed.

    Returns:
    str: The remainder of num1 divided by num2 in the specified base.
    """
    
    # Perform remainder
    result = int(str(num1), base) % int(str(num2), base)
    
    # Convert the result back to the specified base
    result = np.base_repr(result, base=base)
    
    return result

def division(num1, num2, base):
    """
    Perform division of two numbers in a specified base.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.
        base (int): The base in which the division is performed.

    Returns:
        str: The result of the division in the specified base.
    """
    result = int(str(num1), base) // int(str(num2), base)
    result = np.base_repr(result, base=base)
    return result

def perform_substitution_conversion(initial_base, final_base, num):
    """
    Perform substitution conversion from initial_base to final_base for a given number.

    Args:
        initial_base (int): The initial base of the number.
        final_base (int): The final base to convert the number to.
        num (str): The number to be converted.

    Returns:
        str: The converted number in the final base.

    Raises:
        None.

    Specification:
        - The function takes in the initial_base, final_base, and num as arguments.
        - It performs the conversion using the substitution method.
        - The result is calculated in the final_base.
        - The function returns the converted number in the final_base.
    """

    result_digits = []
    for digit in num:
        base_final_digit = np.base_repr(int(digit, initial_base), base=final_base)
        result_digits.append(base_final_digit)

    # Calculate the result in base final_base
    result = '0'
    to_print = ""
    to_print_sum = ""
    for i, digit in enumerate(result_digits):
        #convert initial_base from base 10 to base final_base
        converted_initial_base = np.base_repr(initial_base, base=final_base)
        base_to_exp = power(converted_initial_base, (len(result_digits) - i - 1), final_base)
        to_add = multiplication(digit, base_to_exp, final_base)
        result = addition(result, to_add, final_base)
        to_print += f"{digit}({final_base}) * {converted_initial_base}({final_base})^({len(result_digits) - i - 1}) + "
        to_print_sum += f"{to_add}({final_base}) +"

    to_print = to_print[:-3]
    to_print_sum = to_print_sum[:-3]
    
    # Display the to_print variable
    
    # Display the result
    result_label.config(text=f"{to_print}\n{to_print_sum}\n{num}({initial_base}) = {result}({final_base})", font=("Arial", 20), justify="center")


def perform_successive_division_conversion(initial_base, final_base, num):
    """
    Converts a number from one base to another using successive division method.

    Args:
        initial_base (int): The initial base of the number.
        final_base (int): The final base to convert the number to.
        num (str): The number to be converted.

    Returns:
        None. The result is displayed on the result_label.

    Raises:
        None.
    """

    if initial_base > final_base:
        copy_num = num
        
        remainders = []
        to_print = ""
        while int(num, initial_base) > 0:
            print(num, final_base, initial_base)
            my_remainder = remainder_function(num, final_base, initial_base) #num % final_base
            print(my_remainder)
            quotient = division(num, final_base, initial_base)  #num // final_base
            #transform the remainders into a string, if the number is 10 or more, we will use letters
            to_print += f"{num}({initial_base}) / {final_base}({initial_base}) = {quotient}({initial_base})    |    {num}({initial_base}) % {final_base}({initial_base}) = {my_remainder}({initial_base})"
            #if my remainder is larger than 9, we will use letters
            if int(my_remainder) > 9:
                my_remainder = chr(ord('A') + int(my_remainder) - 10)
            remainders.append(my_remainder)
            to_print += f" = {my_remainder}({final_base})\n"
            num =  quotient
        
        # Reverse the remainders
        remainders.reverse()
        #transform the remainders into a string, if the number is 10 or more, we will use letters
        result = to_print
        result += f"{copy_num}({initial_base}) = "
        result += ''.join([str(i) for i in remainders]) 
        result += f"({final_base})"

        result_label.config(text=result, font=("Arial", 20), justify="center")
    else:
        copy_num = num
        num = int(num, initial_base)

        # Step 1: Initialize an empty list to store remainders
        remainders = []
        to_print = ""
        # Step 2: Perform successive division until num becomes 0
        while num > 0:
            # Calculate remainder and quotient
            remainder = num % final_base
            quotient = num // final_base
            to_print += f"{num} / {final_base} = {quotient}    |    {num} % {final_base} = {remainder}"
            # Append the remainder to the list
            remainders.append(remainder)
            #check if the remainder is larger than 9, if so, we will use letters
            if remainder > 9:
                remainder = chr(ord('A') + remainder - 10)
            to_print += f" = {remainder}({final_base})\n"
            # Update num for the next iteration
            num = quotient

        # Step 3: Reverse the list of remainders to get the final result
        result = remainders[::-1]
        #if the number is 10 or more, we will use letters
        
        result = ''.join([str(i) if i < 10 else chr(ord('A') + i - 10) for i in result])
        result += f"({final_base})"
        to_print += f"{copy_num}({initial_base}) = {result}"
        result_label.config(text=to_print, font=("Arial", 20), justify="center")

def perform_rapid_conversions(initial_base, final_base, num):
    """
    Perform rapid conversions between different number bases.

    Args:
        initial_base (int): The initial base of the number.
        final_base (int): The final base to convert the number to.
        num (str): The number to be converted.

    Returns:
        None

    Raises:
        ValueError: If the initial_base or final_base is not a power of 2 or not in [2, 4, 8, 16].

    Specifications:
        - The function performs conversion using rapid conversions only if the bases are powers of 2.
        - If the bases are not powers of 2 or not in [2, 4, 8, 16], a ValueError is raised.
        - If either the initial_base or final_base is not equal to 2, an error message is displayed.
        - The function converts the number to binary if the final_base is 2.
        - The function converts the number to the final base if the initial_base is 2.
        - The function groups the digits in the number based on the number of digits in each group (group_size).
        - The function adds insignificant digits based on the power of the final base and initial base.
        - The function displays the result in the format "{grouped_result}({initial_base}) = {result}({final_base})".
    """

    # Perform conversion using rapid conversions only if the bases are powers of 2

    # Check if the bases are from 2, 4, 6, 16
    if initial_base not in [2, 4, 8, 16] or final_base not in [2, 4, 8, 16]:
        #check it either final_base or initial_base is equal to 2
        if initial_base != 2 and final_base != 2:
            messagebox.showerror("Error", "Invalid bases. Please enter bases from 2, 4, 8, 16. Either initial base or final base must be 2.")
            return
    
    if final_base == 2:
        # Loop through each digit in num
        result = ""
        for digit in num:
            # Convert the digit to binary
            binary_digit = np.base_repr(int(digit, initial_base), base=2)
            # Add insignificant digits based on the power of the final base and initial base
            insignificant_digits = "0" * (int(np.log2(initial_base)) - len(binary_digit))
            result += insignificant_digits + binary_digit + " "
        result_label.config(text=f"{num}({initial_base}) = {result}({final_base})", font=("Arial", 20), justify="center")
    
    if initial_base == 2:
        group_size = int(np.log2(final_base))  # Number of digits in each group
        result = ""
        for i in range(len(num)-1, -1, -group_size):
                # Get the group of digits
                group = num[max(i-group_size+1, 0):i+1]
                # Convert the group to the final base
                final_base_group = np.base_repr(int(group, initial_base), base=final_base)
                # Add insignificant digits based on the power of the final base and initial base
                result = final_base_group + result  # Change order

        # Display the result
        #convert num in string and then split it into groups of group_size separated by space, add insignificant digits if necessary
        #for example for group_size = 2, 10000 will be 01 00 00, adding insignifiant zeros at the left of the number
        num_str = str(num)
        num_str = num_str.zfill(len(num_str) + (group_size - len(num_str) % group_size) % group_size)  # Add leading zeros
        grouped_result = ' '.join([num_str[i:i+group_size] for i in range(0, len(num_str), group_size)])

        result_label.config(text=f"{grouped_result}({initial_base}) = {result}({final_base})", font=("Arial", 20), justify="center")


        
def perform_conversion_using_10(initial_base, final_base, num):
    """
    Converts a number from an initial base to a final base using base 10 as an intermediate step.
    
    Parameters:
        initial_base (int): The initial base of the number.
        final_base (int): The final base to convert the number to.
        num (str): The number to be converted.
    
    Returns:
        None
    """

    # Convert the number from the initial base to base 10
    num_base_10 = int(num, initial_base)
    
    # Convert the number from base 10 to the final base
    num_final = np.base_repr(num_base_10, base=final_base)

    # Display the result
    result_label.config(text=f"{num}({initial_base}) = {num_base_10}({10}) = {num_final}({final_base})", font=("Arial", 20), justify="center")
    

def handle_conversion():
    """
    Handles number conversions based on user input.

    This function prompts the user to choose a conversion method, an initial base, a final base and a number to transform.
    It performs the selected conversion method on a given number and displays the result.

    Returns:
        None
    """

    # Prompt the user to choose a conversion method
    conversion_method = simpledialog.askinteger("Number Conversions", "Choose conversion method:\n1. Substitution Method\n2. Successive Division\n3. Rapid Conversions\n4. Conversion using 10 as an intermediate base")

    # Check if the conversion method is valid
    if conversion_method not in [1, 2, 3, 4]:
        messagebox.showerror("Error", "Invalid conversion method. Please enter a number from 1 to 3.")
        return
    
    # Prompt the user to choose an initial base
    initial_base = simpledialog.askinteger("Choose Initial Base", "Enter initial base (2 to 16):")

    # Check if the initial base is valid
    if initial_base not in range(2, 17):
        messagebox.showerror("Error", "Invalid initial base. Please enter a number from 2 to 16.")
        return

    # Prompt the user to choose a final base
    final_base = simpledialog.askinteger("Choose Final Base", "Enter final base (2 to 16):")

    # Check if the final base is valid
    if final_base not in range(2, 17):
        messagebox.showerror("Error", "Invalid final base. Please enter a number from 2 to 16.")
        return
    
    # Prompt the user to enter a number
    num = simpledialog.askstring("Enter Number", "Enter the number:")
    valid_digits = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(initial_base-10)]
    if any(digit not in valid_digits for digit in str(num)):
        messagebox.showerror("Error", f"Invalid number. Please enter a number in base {initial_base}.")
        return

    # Perform the selected conversion method based on the given bases
    if conversion_method == 1:
        # Perform conversion using substitution method
        perform_substitution_conversion(initial_base, final_base, num)
    elif conversion_method == 2:
        # Perform conversion using successive division
        perform_successive_division_conversion(initial_base, final_base, num)
    elif conversion_method == 3:
        # Perform conversion using rapid conversions
        perform_rapid_conversions(initial_base, final_base, num)
    elif conversion_method == 4:
        # Perform conversion using conversion using 10 as an intermediate base
        perform_conversion_using_10(initial_base, final_base, num)





# Create the main application window
app = tk.Tk()
app.title("Your App")
app.geometry("900x600")

# Create the menu bar
menu = tk.Menu(app)
app.config(menu=menu)

# Create the main menu dropdown
main_menu = tk.Menu(menu)
menu.add_cascade(label="Main Menu", menu=main_menu)

# Add commands to the main menu dropdown
main_menu.add_command(label="Arithmetic Operations", command=handle_arithmetic)
main_menu.add_command(label="Conversions of Natural Numbers", command=handle_conversion)

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Arial", 20), justify="center")
result_label.pack()

# Create a label to display the author information
author_label = tk.Label(app, text="Author: Mogovan Jonathan - Group 915 English Year I - 2023", font=("Arial", 12), justify="center")
author_label.pack(side="bottom")

# Run the application
app.mainloop()


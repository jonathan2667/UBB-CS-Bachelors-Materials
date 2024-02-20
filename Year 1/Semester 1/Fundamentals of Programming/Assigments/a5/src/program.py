#
# Write the implementation for A5 in this file
#

import random
import math

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

class ComplexNumberUsingList:
    def __init__(self, real_value = 0, imaginary_value = 0):
        self.number = [real_value, imaginary_value]

    def get_real_value(self):
        return self.number[0]

    def get_imaginary_value(self):
        return self.number[1]

    def set_real_value(self, real_value):
        self.number[0] = real_value

    def set_imaginary_value(self, imaginary_value):
        self.number[1] = imaginary_value

    def to_string_complex_number(self):
        return f"{self.number[0]} + {self.number[1]}i"

    def get_modulus_complex_number(self):
        return math.sqrt(self.number[0] * self.number[0] + self.number[1] * self.number[1])


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

class ComplexNumberUsingDictionary:
    def __init__(self, real_value = 0, imaginary_value = 0):
        self.number = {'real_value': real_value, 'imaginary_value': imaginary_value}

    def get_real_value(self):
        return self.number['real_value']

    def get_imaginary_value(self):
        return self.number['imaginary_value']

    def set_real_value(self, real_value):
        self.number['real_value'] = real_value

    def set_imaginary_value(self, imaginary_value):
        self.numer['imaginary_value'] = imaginary_value

    def to_string_complex_number(self):
        return f"{self.number['real_value']} + {self.number['imaginary_value']}i"

    def get_modulus_complex_number(self):
        return math.sqrt(self.number['real_value'] * self.number['real_value'] + self.number['imaginary_value'] * self.number['imaginary_value'])

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def length_and_elements_of_longest_subarray_of_numbers_having_the_same_modulus(list_of_complex_numbers):
    maximum_length_of_numbers_having_same_modulus = 1
    current_length_of_numbers_having_same_modulus = 1
    longest_subarray_of_numbers_having_same_modulus = [list_of_complex_numbers[0]]

    for i in range(1, len(list_of_complex_numbers)):
        if list_of_complex_numbers[i - 1].get_modulus_complex_number() == list_of_complex_numbers[i].get_modulus_complex_number():
            current_length_of_numbers_having_same_modulus += 1
            if current_length_of_numbers_having_same_modulus > maximum_length_of_numbers_having_same_modulus:
                maximum_length_of_numbers_having_same_modulus = current_length_of_numbers_having_same_modulus
                longest_subarray_of_numbers_having_same_modulus = list_of_complex_numbers[i - current_length_of_numbers_having_same_modulus + 1 : i + 1]
        else:
            current_length_of_numbers_having_same_modulus = 1


    return maximum_length_of_numbers_having_same_modulus, longest_subarray_of_numbers_having_same_modulus

def longest_alternating_subsequence_using_numbers_modulus(list_of_complex_numbers):
    """longest_alterning_subsequence[i][0] = Length of the longest alternating subsequence ending at index i and last element is greater than its previous element
       longest_alterning_subsequence[i][1] = Length of the longest  alternating subsequence ending at index i and last element is smaller than its previous element"""

    longest_alterning_subsequence_matrix = [[0 for i in range(2)]
                                            for j in range(len(list_of_complex_numbers))]

    for i in range(len(list_of_complex_numbers)):
        longest_alterning_subsequence_matrix[i][0], longest_alterning_subsequence_matrix[i][1] = 1, 1

    result_longest_alterning_subsequence = 1

    for i in range(1, len(list_of_complex_numbers)):
        for j in range(0, i):
            if list_of_complex_numbers[j].get_modulus_complex_number() < list_of_complex_numbers[i].get_modulus_complex_number() and longest_alterning_subsequence_matrix[i][0] < longest_alterning_subsequence_matrix[j][1] + 1:
                longest_alterning_subsequence_matrix[i][0] = longest_alterning_subsequence_matrix[j][1] + 1
            if list_of_complex_numbers[j].get_modulus_complex_number() > list_of_complex_numbers[i].get_modulus_complex_number() and longest_alterning_subsequence_matrix[i][1] < longest_alterning_subsequence_matrix[j][0] + 1:
                longest_alterning_subsequence_matrix[i][1] = longest_alterning_subsequence_matrix[j][0] + 1
        if result_longest_alterning_subsequence < max(longest_alterning_subsequence_matrix[i][0], longest_alterning_subsequence_matrix[i][1]):
            result_longest_alterning_subsequence = max(longest_alterning_subsequence_matrix[i][0], longest_alterning_subsequence_matrix[i][1])

    return result_longest_alterning_subsequence


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def print_subarray(subarray):
    for i in range(len(subarray)):
        print(subarray[i].to_string_complex_number(), end=" ")

def print_solution_problem_maximum_length_of_numbers_having_same_modulus(maximum_length_of_numbers_having_same_modulus, longest_subarray_of_numbers_having_same_modulus):
    print("Solution for first problem:\n")
    print("Maximum_length_of_numbers_having_same_modulus ", maximum_length_of_numbers_having_same_modulus)
    print("longest_subarray_of_numbers_having_same_modulus")
    print_subarray(longest_subarray_of_numbers_having_same_modulus)

def print_list(list_of_complex_numbers):
    print("The list of complex numbers is : \n")
    for i in range(len(list_of_complex_numbers)):
        print(list_of_complex_numbers[i].to_string_complex_number())

def read_complex_numbers_using_list(list_of_complex_numbers, numbers_of_complex_numbers_to_read):
    if numbers_of_complex_numbers_to_read == 0:
        for i in range(10):
            list_of_complex_numbers.append(ComplexNumberUsingList(random.randint(1, 10), random.randint(1, 10)))
    else:
        for i in range(numbers_of_complex_numbers_to_read):
            real_value = int(input("Real Value: "))
            imaginary_value = int(input("Imaginary Value: "))
            list_of_complex_numbers.append(ComplexNumberUsingList(real_value, imaginary_value))

def solve_problems_using_list():
    """
            solve problems using list:
            1. Length and elements of a longest subarray of numbers having the same modulus.
            2. The length of a longest alternating subsequence, when considering each number's
            modulus (e.g., given sequence [1, 3, 2, 4, 10, 6, 1], [1, 3, 2, 10] is an alternating subsequence, because 1 < 3 > 2 < 10)
            :return:
            """
    list_of_complex_numbers = []
    numbers_of_complex_numbers_to_read = int(input("How many numbers would you like to read?\n*By pressing 0, you will automatically get 10 random complex numbers*"))

    read_complex_numbers_using_list(list_of_complex_numbers, numbers_of_complex_numbers_to_read)
    print_list(list_of_complex_numbers)

    maximum_length_of_numbers_having_same_modulus, longest_subarray_of_numbers_having_same_modulus = length_and_elements_of_longest_subarray_of_numbers_having_the_same_modulus(list_of_complex_numbers)
    print_solution_problem_maximum_length_of_numbers_having_same_modulus(maximum_length_of_numbers_having_same_modulus, longest_subarray_of_numbers_having_same_modulus)

    result_longest_alterning_subsequence = longest_alternating_subsequence_using_numbers_modulus(list_of_complex_numbers)
    print("\n\nSolution for the length of a longest alternating subsequence, when considering each number's modulus", result_longest_alterning_subsequence)

def print_dictionary(dictionary_of_complex_numbers):
    print("The dictionary of complex numbers is : \n")
    for i in range(len(dictionary_of_complex_numbers)):
        print(dictionary_of_complex_numbers[i].to_string_complex_number())

def read_complex_numbers_using_dictionary(dictionary_of_complex_numbers, numbers_of_complex_numbers_to_read):

    if numbers_of_complex_numbers_to_read == 0:
        for i in range(10):
            dictionary_of_complex_numbers.append(ComplexNumberUsingList(random.randint(1, 10), random.randint(1, 10)))
    else:
        for i in range(numbers_of_complex_numbers_to_read):
            real_value = int(input("Real Value: "))
            imaginary_value = int(input("Imaginary Value: "))
            dictionary_of_complex_numbers.append(ComplexNumberUsingList(real_value, imaginary_value))

def solve_problems_using_dictionary():
    """
    solve problems using dictionary:
    1. Length and elements of a longest subarray of numbers having the same modulus.
    2. The length of a longest alternating subsequence, when considering each number's
    modulus (e.g., given sequence [1, 3, 2, 4, 10, 6, 1], [1, 3, 2, 10] is an alternating subsequence, because 1 < 3 > 2 < 10)
    :return:
    """
    dictionary_of_complex_numbers = []
    numbers_of_complex_numbers_to_read = int(input("How many numbers would you like to read?\n*By pressing 0, you will automatically get 10 random complex numbers*"))

    read_complex_numbers_using_dictionary(dictionary_of_complex_numbers, numbers_of_complex_numbers_to_read)
    print_dictionary(dictionary_of_complex_numbers)

    maximum_length_of_numbers_having_same_modulus, longest_subarray_of_numbers_having_same_modulus = length_and_elements_of_longest_subarray_of_numbers_having_the_same_modulus(dictionary_of_complex_numbers)
    print_solution_problem_maximum_length_of_numbers_having_same_modulus(maximum_length_of_numbers_having_same_modulus, longest_subarray_of_numbers_having_same_modulus)

    result_longest_alterning_subsequence = longest_alternating_subsequence_using_numbers_modulus(dictionary_of_complex_numbers)
    print("\n\nSolution for the length of a longest alternating subsequence, when considering each number's modulus", result_longest_alterning_subsequence)


if __name__ == "__main__":

    user_choose_value_for_list_or_dictionary = int(input("Press 1 for List Representation or 2 for Dictionary Representation. "))

    if user_choose_value_for_list_or_dictionary == 1:
        solve_problems_using_list()
    else:
        solve_problems_using_dictionary()





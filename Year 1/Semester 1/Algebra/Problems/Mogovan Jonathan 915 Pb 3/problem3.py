import itertools
import numpy as np
from scipy.linalg import lu
from numpy.linalg import LinAlgError
from numpy.linalg import det
import pyperclip

# Function to calculate the number of bases for a given dimension
def num_bases(n):
    result = 1
    for i in range(n):
        result *= 2**n - 2**i
    return result

# Function to print bases for a 4x4 matrix
def print_bases_4(n):
    cnt = 0
    str_to_print = ""
    # Iterate through all possible combinations of 0 and 1 for a 4x4 matrix
    for vectors in itertools.product(range(2), repeat=n * n):
        matrix_np = np.array(vectors).reshape(n, n) 
        det_value = int(round(np.linalg.det(matrix_np))) % 2  # Calculate determinant modulo 2
        if det_value == 1:
            matrix_tuple = tuple(tuple(row) for row in matrix_np)
            str_to_print += str(matrix_tuple) + "\n"
            cnt += 1
    print(str_to_print)
    pyperclip.copy(str_to_print)  # Copy the result to the clipboard
    print("Number of bases printed - to check we printed all of them: ", cnt)

# Function to print bases for a 3x3 matrix
def print_bases_3(n):
    unique_vectors = set()
    cnt = 0
    vectors = list(itertools.product([0, 1], repeat=n))
    # Iterate through all combinations of three vectors for a 3x3 matrix
    for vector1 in vectors:
        for vector2 in vectors:
            if np.array_equal(vector1, vector2):
                continue
            for vector3 in vectors:
                if np.array_equal(vector1, vector3) or np.array_equal(vector2, vector3):
                    continue

                matrix_np = np.array([vector1, vector2, vector3]) 
                if (det(matrix_np) % 2 == 1):  # Check if determinant modulo 2 is 1
                    cnt += 1
                    print(tuple(map(tuple, matrix_np)))

    print("Number of bases printed - to check we printed all of them: ", cnt)

# Function to print bases for a 2x2 matrix
def print_bases_2(n):
    cnt = 0
    vectors = list(itertools.product([0, 1], repeat=n))
    # Iterate through all combinations of two vectors for a 2x2 matrix
    for vector1 in vectors:
        for vector2 in vectors:
            if np.array_equal(vector1, vector2):
                continue 
            matrix_np = np.array([vector1, vector2]) 

            if (det(matrix_np) % 2 == 1):  # Check if determinant modulo 2 is 1
                print(tuple(map(tuple, matrix_np)))
                cnt += 1    

    print("Number of bases printed - to check we printed all of them: ", cnt)

# Get user input for the matrix dimension
n = int(input("Enter a non-zero natural number: "))

# Print the total number of bases for the given dimension
print("The number of bases is ", num_bases(n))

# Print bases for specific dimensions (2x2, 3x3, 4x4) if the dimension is less than 5
if (n < 5):

    if (n == 4):
        print_bases_4(4)
    if (n == 2):
        print_bases_2(2)
    if (n == 3):
        print_bases_3(3)

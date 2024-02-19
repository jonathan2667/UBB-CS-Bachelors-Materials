"""
Starting with ths definition, we will define a function to check if a matrix is in reduced row-echelon form. Then, we will define a function to generate matrices in reduced row-echelon form. Finally, we will generate matrices in reduced row-echelon form and print them.

Reduced row echelon form is a type of matrix used to solve systems of linear equations. Reduced row echelon form has four requirements:


1. The first non-zero number in the first row (the leading entry) is the number 1.

2. The second row also starts with the number 1, which is further to the right than the leading entry in the first row. For every subsequent row, the number 1 must be further to the right.

3. The leading entry in each row must be the only non-zero number in its column.

4. Any non-zero rows are placed at the bottom of the matrix.
"""


# Importing necessary libraries
"""
Finding the number of matrices in reduced row-echelon form is a difficult task for n and m large. We will use the following formula to find the number of matrices in reduced row-echelon form:

https://math.stackexchange.com/questions/3482267/counting-echelon-form-matrices

"""
from itertools import product
import numpy as np

from sympy import symbols, summation, Eq, solve, binomial

def nu(m, n):
    total = 0
    for k in range(min(m, n) + 1):
        for alpha in product(range(n+1), repeat=k+1):
            if sum(alpha) == n-k and all(a >= 0 for a in alpha):
                total += 2 ** sum(p * alpha[p] for p in range(k + 1))
    return total


# Function to check if a matrix is in reduced row-echelon form
def is_reduced_row_echelon(matrix):
    m, n = matrix.shape
    last_leading_one_index = -1
    zero_row_encountered = False
    for r in range(m):
        row = matrix[r]
        leading_one_index = -1
        for c in range(n):
            if row[c] == 1:
                leading_one_index = c
                break
        if leading_one_index != -1:
            # Check if leading one index is in increasing order and no zero rows encountered before
            if leading_one_index <= last_leading_one_index or zero_row_encountered:
                return False
            # Check if the column containing the leading one has all other elements as zero
            if np.any(matrix[:, leading_one_index] != [1 if i == r else 0 for i in range(m)]):
                return False
            last_leading_one_index = leading_one_index
        else:
            zero_row_encountered = True
    return True

# Function to generate matrices in reduced row-echelon form
def generate_matrices(m, n):
    matrices = []
    for elements in product([0, 1], repeat=m*n):
        matrix = np.array(elements).reshape(m, n)
        if is_reduced_row_echelon(matrix):
            matrices.append(matrix)
    return matrices

# Define the dimensions of the matrix
m = 6
n = 6

# Define the path to the output folder
folder_path = 'C:\\Users\\jmogo\\My Drive\\University\\Homework\\Algebra\\Mogovan_Jonathan_915 Pb 5'

# Open the input file in write mode
with open(f'{folder_path}/in7.txt', 'w') as f:
    # Write m and n to the file
    f.write(f"{m}\n{n}\n")

# Open the output file in write mode
with open(f'{folder_path}/out7.txt', 'w') as f:
    if m > 5 or n > 5:
        # Write the number of matrices in reduced row-echelon form to the file
        f.write(str(nu(m, n)) + '\n')  
    else:
        # Generate matrices in reduced row-echelon form
        matrices = generate_matrices(m, n)

        # Write the number of matrices in reduced row-echelon form to the file
        f.write(f"Number of matrices in reduced row-echelon form: {len(matrices)}\n")

        # Write each matrix in reduced row-echelon form to the file
        for matrix in matrices:
            f.write(str(matrix) + '\n\n')

import itertools
import sympy
import numpy as np

#choose value k, n
k = 2
n = 3

#check wheter 2 bases are equal using sympy lirary - useful library for linear algebra, rref - reduced row echelon format matrix for linear independency
def are_bases_equal(first_base, second_base):
    sympy1 = sympy.Matrix(first_base)
    sympy2 = sympy.Matrix(second_base)
    return np.array_equal(np.array(sympy1.rref()[0]).astype(np.int64) % 2, np.array(sympy2.rref()[0]).astype(np.int64) % 2)

def check_rank_matrix(rank, k):
    return rank == k

#generate all k dimensional subspaced using itertools and verifying the conditions of rank
def generate_all_subsets(n, k):
    all_matrix = []
    k_dimensional_subspaces = itertools.product(range(2), repeat=k * n)
    for combinations in k_dimensional_subspaces:
        matrix_converted_from_subsets_tupple = np.array(combinations)
        matrix_converted_from_subsets_tupple = matrix_converted_from_subsets_tupple.reshape(k, n)
        rank_of_matrix = np.linalg.matrix_rank(matrix_converted_from_subsets_tupple)
        if check_rank_matrix(rank_of_matrix, k):
            all_matrix.append(matrix_converted_from_subsets_tupple)
    return all_matrix

#input data, calling the functions
combinations_bases = generate_all_subsets(n, k)
cnt = 1
combinations_set = [combinations_bases[0]]

#checking we do not have same bases
for basis in combinations_bases:
    if all(not are_bases_equal(basis, existing_basis) for existing_basis in combinations_set):
        combinations_set.append(basis)
        cnt += 1

#printing results
print("The number of", k, "-dimensional subspaces of the vector space (Z_2) ^ ", n, "over Z_2 is: ", cnt)
for matrix_combination in combinations_set:
    matrix_tuple = tuple(tuple(row) for row in matrix_combination)
    print(matrix_tuple)



import itertools
import sympy
import numpy as np


def check(basis1, basis2):
    sympy_basis1 = sympy.Matrix(basis1)
    sympy_basis2 = sympy.Matrix(basis2)

    basis1 = np.array(sympy_basis1.rref()[0]).astype(np.int64) % 2
    basis2 = np.array(sympy_basis2.rref()[0]).astype(np.int64) % 2

    return np.array_equal(basis1, basis2)


def solve(n, k):
    matrix_set = []
    k_dim_subspaces = itertools.product(range(2), repeat=k * n)

    for subset in k_dim_subspaces:
        matrix = np.array(subset)
        matrix = matrix.reshape(k, n)

        rank = np.linalg.matrix_rank(matrix)

        if rank == k:
            matrix_set.append(matrix)

    return matrix_set


def main():
    k = int(input())
    n = int(input())

    matrix_set = solve(n, k)
    final_matrix_set = [matrix_set[0]]
    counter = 1

    for basis in matrix_set:
        if all(not check(basis, existing_basis) for existing_basis in final_matrix_set):
            final_matrix_set.append(basis)
            counter += 1

    print(counter)
    for matrix in final_matrix_set:
        print(matrix)


while True:
    main()

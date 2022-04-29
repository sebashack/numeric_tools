import numpy as np

from partial_pivot import partial_pivot, partial_pivot_with_permutation
from matrix_utils import to_aug


def solve_by_gaussian_elim_with_partial_pivot(a, b, print_k=False):
    ab = to_aug(a, b)
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]

    # Stages
    for k in range(0, n - 1):
        partial_pivot(ab, k)
        # Compute multiplier for row in stage.
        for i in range(k + 1, n):
            multiplier = ab[i][k] / ab[k][k]
            for j in range(k, n + 1):
                ab[i][j] = ab[i][j] - (multiplier * ab[k][j])
        if print_k:
            print(f"stage {k}")
            print(ab)
            print("----")

    return ab


# WARNING: This function mutates input matrix a
def lu_factorization_with_partial_pivot(a, print_k=False):
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]
    permutation = np.identity(n, dtype=np.float64)
    lower_tri = np.identity(n, dtype=np.float64)

    # Stages
    for k in range(0, n - 1):
        partial_pivot_with_permutation(a, lower_tri, permutation, k)
        # Compute multiplier for row in stage.
        for i in range(k + 1, n):
            multiplier = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - (multiplier * a[k][j])
                if i > j:
                    lower_tri[i][j] = multiplier
        if print_k:
            print(f"stage {k}")
            print(a)
            print("----")

    return (lower_tri, permutation)

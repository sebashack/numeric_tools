import numpy as np

from matrix_utils import to_aug


def solve_by_simple_gaussian_elim(a, b, print_k=False):
    ab = to_aug(a, b)
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]

    # Stages
    for k in range(0, n - 1):
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
def simple_gaussian_elim(a, print_k=False):
    assert a.shape[0] == a.shape[1]
    n = a.shape[0]
    lower_tri = np.identity(n)

    # Stages
    for k in range(0, n - 1):
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

    return lower_tri

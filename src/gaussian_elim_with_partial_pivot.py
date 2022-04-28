import numpy as np

from partial_pivot import partial_pivot


def solve_by_gaussian_elim_with_partial_pivot(a, b, print_k=False):
    ab = np.column_stack((a, b))
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]

    # Stages
    for k in range(0, n - 1):
        partial_pivot(ab, k)
        # Compute factor for row in stage.
        for i in range(k + 1, n):
            factor = ab[i][k] / ab[k][k]
            for j in range(k, n + 1):
                ab[i][j] = ab[i][j] - (factor * ab[k][j])
        if print_k:
            print(f"stage {k}")
            print(ab)
            print("----")

    return ab


def gaussian_elim_with_partial_pivot(a, print_k=False):
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]

    # Stages
    for k in range(0, n - 1):
        partial_pivot(a, k)
        # Compute factor for row in stage.
        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - (factor * a[k][j])
        if print_k:
            print(f"stage {k}")
            print(a)
            print("----")

    return a

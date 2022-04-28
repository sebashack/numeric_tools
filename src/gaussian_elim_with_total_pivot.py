import numpy as np

from total_pivot import total_pivot


def solve_by_gaussian_elim_with_total_pivot(a, b, print_k=False):
    ab = np.column_stack((a, b))
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]
    labels = list(range(0, n))

    # Stages
    for k in range(0, n - 1):
        total_pivot(ab, k, labels)
        # Compute multiplier for row in stage.
        for i in range(k + 1, n):
            multiplier = ab[i][k] / ab[k][k]
            for j in range(k, n + 1):
                ab[i][j] = ab[i][j] - (multiplier * ab[k][j])
        if print_k:
            print(f"stage {k}")
            print(ab)
            print("----")

    return (ab, labels)

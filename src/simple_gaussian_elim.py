import numpy as np


def simple_gaussian_elim(a, b):
    ab = np.column_stack((a, b))
    assert a.shape[0] == a.shape[1]

    n = a.shape[0]

    # Stages
    for k in range(0, n - 1):
        # Compute factor for row in stage.
        for i in range(k + 1, n):
            factor = ab[i][k] / ab[k][k]
            for j in range(k, n + 1):
                ab[i][j] = ab[i][j] - (factor * ab[k][j])

    return ab

import numpy as np


def progressive_substitution(ab):
    n = ab.shape[0]
    assert ab.shape[1] == n + 1

    xs = np.zeros(n, dtype=np.float64)
    xs[0] = ab[0][n] / ab[0][0]

    for i in range(1, n):
        accum = 0
        for p in range(0, i):
            accum += ab[i][p] * xs[p]
        xs[i] = (ab[i][n] - accum) / ab[i][i]

    return xs

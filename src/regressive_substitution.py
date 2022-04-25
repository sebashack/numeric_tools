import numpy as np


def regressive_substitution(ab):
    n = ab.shape[0]
    assert ab.shape[1] == n + 1

    xs = np.zeros(n)
    xs[n - 1] = ab[n - 1][n] / ab[n - 1][n - 1]

    # Loop backwards
    for i in range(n - 2, -1, -1):
        accum = 0
        for p in range(i + 1, n):
            accum += ab[i][p] * xs[p]
        xs[i] = (ab[i][n] - accum) / ab[i][i]
    return xs

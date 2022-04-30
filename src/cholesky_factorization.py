import numpy as np


def cholesky_factorization(a):
    n = a.shape[0]
    lower_tri = np.identity(n, dtype=np.float64)
    upper_tri = np.identity(n, dtype=np.float64)

    for k in range(0, n):
        sum0 = 0
        # Compute lower_tri[k][k]
        for p in range(0, k):
            sum0 += lower_tri[k][p] * upper_tri[p][k]
        upper_tri[k][k] = np.sqrt(a[k][k] - sum0)
        lower_tri[k][k] = upper_tri[k][k]

        # Compute lower_tri[i][k]
        for i in range(k + 1, n):
            sum1 = 0
            for p in range(0, k):
                sum1 += lower_tri[i][p] * upper_tri[p][k]
            lower_tri[i][k] = (a[i][k] - sum1) / lower_tri[k][k]

        # Compute upper_tri[k][j]
        for j in range(k + 1, n):
            sum2 = 0
            for p in range(0, k):
                sum2 += lower_tri[k][p] * upper_tri[p][j]
            upper_tri[k][j] = (a[k][j] - sum2) / upper_tri[k][k]

    return (lower_tri, upper_tri)

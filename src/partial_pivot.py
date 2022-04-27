# This procedure mutates the input matrix.
def partial_pivot(ab, k):
    largest = abs(ab[k][k])
    largest_row = k
    n = ab.shape[0]

    for s in range(k + 1, n):
        current = abs(ab[s][k])
        if current > largest:
            largest = current
            largest_row = s
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            ab[[k, largest_row]] = ab[[largest_row, k]]

# This procedure mutates the input matrix.
def partial_pivot(ab, k):
    largest = abs(ab[k][k])
    largest_row = k
    n = ab.shape[0]

    for r in range(k + 1, n):
        current = abs(ab[r][k])
        if current > largest:
            largest = current
            largest_row = r
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            ab[[k, largest_row]] = ab[[largest_row, k]]


# This procedure mutates the input a and permutation matrices
def partial_pivot_with_permutation(a, lower_tri, permutation, k):
    assert a.shape == permutation.shape

    largest = abs(a[k][k])
    largest_row = k
    n = a.shape[0]

    for r in range(k + 1, n):
        current = abs(a[r][k])
        if current > largest:
            largest = current
            largest_row = r
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            a[[k, largest_row]] = a[[largest_row, k]]
            permutation[[k, largest_row]] = permutation[[largest_row, k]]
            if k > 0:
                # Swap multiplier values for stages < k
                for s in range(0, k):
                    lower_tri[largest_row][s], lower_tri[k][s] = (
                        lower_tri[k][s],
                        lower_tri[largest_row][s],
                    )

# This procedure mutates the input matrix and the column labels.
def total_pivot(ab, k, labels):
    largest = abs(ab[k][k])
    largest_row = k
    largest_column = k

    n = ab.shape[0]
    for r in range(k, n):
        for c in range(k, n):
            current = abs(ab[r][c])
            if current > largest:
                largest = current
                largest_row = r
                largest_column = c
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            ab[[k, largest_row]] = ab[[largest_row, k]]
        if largest_column != k:
            ab[:, [k, largest_column]] = ab[:, [largest_column, k]]
            labels[k], labels[largest_column] = labels[largest_column], labels[k]

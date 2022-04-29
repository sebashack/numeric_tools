from simple_gaussian_elim import simple_gaussian_elim
from gaussian_elim_with_partial_pivot import lu_factorization_with_partial_pivot
from progressive_substitution import progressive_substitution
from regressive_substitution import regressive_substitution
from matrix_utils import to_aug


# WARNING: This function mutates input matrix a
def solve_by_simple_gaussian_fac(a, b):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == b.shape[0]

    lower_tri = simple_gaussian_elim(a)
    z = progressive_substitution(to_aug(lower_tri, b))
    # a = upper_tri after lu_factorization_with_partial_pivot
    x = regressive_substitution(to_aug(a, z))

    return x


# WARNING: This function mutates input matrix a
def solve_by_lu_fac_with_partial_pivot(a, b):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == b.shape[0]

    lower_tri, permutation = lu_factorization_with_partial_pivot(a)
    pb = permutation.dot(b)
    z = progressive_substitution(to_aug(lower_tri, pb))
    # a = upper_tri after lu_factorization_with_partial_pivot
    x = regressive_substitution(to_aug(a, z))

    return x

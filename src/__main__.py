import sys
import math

from splines import (
    linear_splines,
    linear_eqs_strs,
    quadratic_splines,
    print_quadratic_coefficients,
    quadratic_eqs_strs,
)
from newton_interpolation import (
    newton_interpolation,
    print_bs,
    gen_poly,
    simp_poly,
    newton_interpolation_by_diffs,
)
from gaussian_elim_with_partial_pivot import (
    solve_by_gaussian_elim_with_partial_pivot,
    determinant_computation,
)
from matrix_utils import (
    set_print_opts,
    mk_vec,
    mk_mat,
    print_solution,
    copy,
    gen_spd_mat,
)
from iterative_methods import jacobi_method, seidel_method
from iterative_methods_mat_form import (
    spectral_radius,
    jacobi_method_mat,
    seidel_method_mat,
    tc_jacobi,
    tc_seidel,
)
from gaussian_elim_with_total_pivot import solve_by_gaussian_elim_with_total_pivot
from regressive_substitution import regressive_substitution
from simple_gaussian_elim import solve_by_simple_gaussian_elim
from factorization_solvers import (
    solve_by_cholesky_fac,
    solve_by_crout_fac,
    solve_by_dolittle_fac,
    solve_by_lu_fac_with_partial_pivot,
    solve_by_simple_gaussian_fac,
)

set_print_opts(3)


def main(argv):
    p = 94500000
    i1 = 0.0253
    i2 = 0.0278
    i3 = 0.0897
    j = 0.01
    cenp = 20000000
    g = 40000

    p36 = p * math.pow(1 + i1, 36)

    zi1 = (math.pow(1 + i1, 36) - math.pow(1 + j, 36)) / (i1 - j)

    zi2 = (1 - math.pow((1 + j) / (1 + i2), 60)) / (i2 - j)

    z = math.pow(1 + j, 36 - 1) * (1 + j)

    a1__ = p36 / ((z * zi2) + zi1)
    a1_ = a1__ * z

    fi136 = a1__ * zi1
    pi236 = a1_ * (1 - math.pow((1 + j) / (1 + i2), 18)) / (i2 - j)
    s = (fi136 + pi236) * math.pow(1 + i2, 18)
    p54 = p36 * math.pow(1 + i2 , 18)
    p_ = p54 - s - cenp
    p__ = p_ * math.pow(1 + i3, 2)

    ag = g * ((1/i3) - (20 / (math.pow(1 + i3, 20) - 1)))
    at = p__ * ((math.pow(1 + i3, 20) * i3) / (math.pow(1 + i3, 20) - 1))
    a1 = at - ag

    # print(p36)
    # print(zi2)
    # print(zi1)
    # print(z)
    # print(a1__)
    # print(a1_)
    # print(p54)
    # print(fi136)
    # print(pi236)
    # print(s)
    # print(p54)
    # print(p_)
    # print(p__)
    # print(ag)
    # print(at)
    print(a1)


if __name__ == "__main__":
    main(sys.argv[1:])

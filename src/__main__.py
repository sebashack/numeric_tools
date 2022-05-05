import sys
import math

from newton_interpolation import newton_interpolation, print_bs, print_poly, newton_interpolation_by_diffs
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
    # a = gen_spd_mat(18, seed=0)
    # b = mk_vec([30, 43, 1, -10, 30, 7, 10, -13, 30, 8, 1, -10, 50, 8, 100, -10, 21, 32])
    # init = mk_vec([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    # ab = solve_by_simple_gaussian_elim(a, b)
    # xs = regressive_substitution(ab)
    # print_solution(xs)
    # print("--")

    # ab = solve_by_gaussian_elim_with_partial_pivot(a, b)
    # xs = regressive_substitution(ab)
    # print_solution(xs)
    # print("--")

    # ab, labels = solve_by_gaussian_elim_with_total_pivot(a, b)
    # xs = regressive_substitution(ab, labels)
    # print_solution(xs)
    # print("--")

    # xs = solve_by_simple_gaussian_fac(copy(a), copy(b))
    # print_solution(xs)
    # print("--")

    # xs = solve_by_lu_fac_with_partial_pivot(copy(a), copy(b))
    # print_solution(xs[0])
    # print("--")

    # xs = solve_by_crout_fac(a, b)
    # print_solution(xs)
    # print("--")

    # xs = solve_by_dolittle_fac(a, b)
    # print_solution(xs)
    # print("--")

    # xs = solve_by_cholesky_fac(a, b)
    # print_solution(xs)
    # print("--")

    # m = mk_mat(
    #     [
    #         [1, 32, 1, 22, 2],
    #         [2, 32, 32, 98, -8],
    #         [3, 10, 1, 90, -3],
    #         [3, 3, 5, 19, -1],
    #         [3, 2, 5, 19, 100],
    #     ]
    # )
    # det_m = determinant_computation(m)
    # print(det_m)
    # print("--")

    # a = mk_mat(
    #     [
    #         [45, 13, -4, 8],
    #         [-5, -28, 4, -14],
    #         [9, 15, 63, -7],
    #         [2, 3, -8, -42],
    #     ]
    # )
    # b = mk_vec([-25, 82, 75, -43])
    # init = mk_vec([2, 2, 2, 2])
    # tol = 0.5 * math.pow(10, -5)
    # print(spectral_radius(tc_jacobi(a, b)[0]))
    # print_solution(jacobi_method(a, b, init, tol, 15))
    # print_solution(jacobi_method_mat(a, b, init, tol, 15))
    # print("--")

    # print(spectral_radius(tc_seidel(a, b)[0]))
    # print_solution(seidel_method(a, b, init, tol, 15))
    # print_solution(seidel_method_mat(a, b, init, tol, 15))
    # print("--")

    points = [
        (1, 0.6747),
        (1.2, 0.8491),
        (1.4, 1.1214),
        (1.6, 1.4921),
        (1.8, 1.9607),
        (2, 2.5258),
    ]
    # bs = newton_interpolation(points)
    # print_bs(bs)
    # print_poly(points, bs)
    tab = newton_interpolation_by_diffs(points)
    print(tab)
    print("--")


if __name__ == "__main__":
    main(sys.argv[1:])

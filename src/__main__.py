import sys

from gaussian_elim_with_partial_pivot import (
    solve_by_gaussian_elim_with_partial_pivot,
)
from matrix_utils import set_print_opts, mk_mat, mk_vec, print_solution, copy
from gaussian_elim_with_total_pivot import solve_by_gaussian_elim_with_total_pivot
from regressive_substitution import regressive_substitution
from simple_gaussian_elim import solve_by_simple_gaussian_elim
from factorization_solvers import (
    solve_by_simple_gaussian_fac,
    solve_by_lu_fac_with_partial_pivot,
    solve_by_crout_fac,
    solve_by_dolittle_fac,
)

set_print_opts(4)


def main(argv):
    a = mk_mat(
        [
            [7, 2, 5, 12, 3, 3, 6, 1, 8, 8, 1, -1],
            [2, 3, 1, 2, 9, 5, 4, 9, 3, -9, 1, 1],
            [1, 43, 7, 3, 5, 6, 25, 2, 1, 2, 4, 91],
            [4, 4, 900, 5, 3, 2, 67, 9, 9, 4, 1, 1],
            [4, -9, 3, 8, 5, 7, 3, 2, 2, 5, 1, 41],
            [8, 7, 9, 500, 5, 9, 3, 4, 5, -3, 1, 1],
            [4, 4, 5, 3, 1, 3, 9, 1, 800, 8, 2, -1],
            [1, 4, 2, 2, 1, 5, 7, 1, 7, 3, 1, 1],
            [2, 7, 4, 4, 1, 8, 7, 4, 7, 4, 1, 31],
            [4, 17, 5, 5, 10, 5, 2, 3, 9, 8, 1, 1],
            [4, 2, 4, 5, 2, 2, 2, 1, 2, -8, 5, 1],
            [4, 22, 4, 5, 8, 2, 2, 1, 2, -8, 5, 123],
        ]
    )
    b = mk_vec([30, 8, 1, -10, 4, 4, 90, 6, 9, 6, -3, 100])

    ab = solve_by_simple_gaussian_elim(a, b)
    xs = regressive_substitution(ab)
    print_solution(xs)
    print("--")

    ab = solve_by_gaussian_elim_with_partial_pivot(a, b)
    xs = regressive_substitution(ab)
    print_solution(xs)
    print("--")

    ab, labels = solve_by_gaussian_elim_with_total_pivot(a, b)
    xs = regressive_substitution(ab, labels)
    print_solution(xs)
    print("--")

    xs = solve_by_simple_gaussian_fac(copy(a), copy(b))
    print_solution(xs)
    print("--")

    xs = solve_by_lu_fac_with_partial_pivot(copy(a), copy(b))
    print_solution(xs)
    print("--")

    xs = solve_by_crout_fac(a, b)
    print_solution(xs)
    print("--")

    xs = solve_by_dolittle_fac(a, b)
    print_solution(xs)
    print("--")


if __name__ == "__main__":
    main(sys.argv[1:])

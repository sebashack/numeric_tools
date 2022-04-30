import sys

from gaussian_elim_with_partial_pivot import (
    solve_by_gaussian_elim_with_partial_pivot,
)
from matrix_utils import (
    set_print_opts,
    mk_vec,
    print_solution,
    copy,
    gen_spd_mat,
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

set_print_opts(4)


def main(argv):
    a = gen_spd_mat(18, seed=0)
    b = mk_vec([30, 43, 1, -10, 30, 7, 10, -13, 30, 8, 1, -10, 50, 8, 100, -10, 21, 32])

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

    xs = solve_by_cholesky_fac(a, b)
    print_solution(xs)
    print("--")


if __name__ == "__main__":
    main(sys.argv[1:])

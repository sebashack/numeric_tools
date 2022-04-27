import sys

from gaussian_elim_with_partial_pivot import gaussian_elim_with_partial_pivot
from matrix_utils import set_print_opts, mkMat, mkVec, print_solution
from gaussian_elim_with_total_pivot import gaussian_elim_with_total_pivot
from regressive_substitution import regressive_substitution
from simple_gaussian_elim import simple_gaussian_elim

set_print_opts(4)


def main(argv):
    a = mkMat([[2, -1, -3, 2], [5, -10, 2, -6], [5, -9, 15, -6], [2, 1, -1, 10]])
    b = mkVec([4, 3, 2, 1])

    ab = simple_gaussian_elim(a, b)
    xs = regressive_substitution(ab)
    print(ab)
    print_solution(xs)
    print("--")

    a = mkMat([[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 5], [-12, 13, -8, -4]])
    b = mkVec([-12, 13, 31, -32])
    ab = gaussian_elim_with_partial_pivot(a, b, print_k=True)
    xs = regressive_substitution(ab)
    print(ab)
    print_solution(xs)
    print("--")

    a = mkMat([[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 13], [-12, 13, -8, -4]])
    b = mkVec([-12, 13, 31, -32])
    ab, labels = gaussian_elim_with_total_pivot(a, b, print_k=True)
    xs = regressive_substitution(ab, labels)
    print(ab)
    print_solution(xs)
    print("--")


if __name__ == "__main__":
    main(sys.argv[1:])

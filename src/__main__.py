import sys
import math

from matrix_utils import set_print_opts, mkMat, mkVec
from simple_gaussian_elim import simple_gaussian_elim


set_print_opts(3)


def main(argv):
    a = mkMat([[14, 6, -2, 3], [3, 15, 2, -5], [-7, 4, -23, 2], [1, -3, -2, 16]])
    b = mkVec([12, 32, -24, 14])
    ab = simple_gaussian_elim(a, b)
    print(ab)


if __name__ == "__main__":
    main(sys.argv[1:])

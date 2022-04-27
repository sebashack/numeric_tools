import numpy as np


def set_print_opts(decimal_places):
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=decimal_places)


def mkMat(lss):
    return np.array(lss).astype(np.float64)


def mkVec(vec):
    return np.array(vec).astype(np.float64)


def print_solution(vec):
    for i, x in enumerate(vec):
        print(f"x{i+1} = {x}")

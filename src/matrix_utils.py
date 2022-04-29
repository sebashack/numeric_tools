import numpy as np


def set_print_opts(decimal_places):
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=decimal_places)


def to_aug(a, b):
    return np.column_stack((a, b))


def mk_mat(lss):
    return np.array(lss).astype(np.float64)


def copy(m):
    return np.copy(m)


def mk_vec(vec):
    return np.array(vec).astype(np.float64)


def print_solution(vec):
    for i, x in enumerate(vec):
        print(f"x{i+1} = {x}")

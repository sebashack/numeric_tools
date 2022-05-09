import sys
import math

from bisection import bisection
from false_rule import false_rule
from fixed_point import fixed_point
from fun_plot import plot
from incremental_search import incremental_search
from maximum_dg import maximum_dg
from newton import newton
from secant import secant
from multiple_roots import multiple_roots


def main(argv):
    # def f(x):
    #     v = (1/x) + 0.4 - (1.74 * (math.log(50 * math.sqrt(x))))
    #     return v

    # def g(x):
    #     v = -0.4 + (1.74 * (math.log(50 * math.sqrt(x))))
    #     return 1 / v

    # tolerance = 5 * math.pow(10, -3)
    # fixed_point(f, g, None, 0.5, tolerance, 100, err_type="rel")

    # print(0.0009223349719091456 < tolerance)
    # def g(x):
    #     return math.pow(math.e, -x)

    # def dg(x):
    #     return -math.pow(math.e, -x)

    # def f(x):
    #     return math.pow(math.e, -x) - x

    # def df(x):
    #     return -math.pow(math.e, -x) - 1

    # def ddf(x):
    #     return math.pow(math.e, -x)

    # tolerance = 5 * math.pow(10, -5)
    # secant(f, (0, 1), tolerance, 100, err_type="abs")
    # print("----")
    # multiple_roots(f, df, ddf, 0, tolerance, 100, err_type="abs")
    # print("----")
    # newton(f, df, 0, tolerance, 100, err_type="abs")
    # print("----")
    # fixed_point(f, g, dg, 0, tolerance, 100, err_type="abs")
    # print("----")
    # false_rule(f, -2, 5.0, tolerance, err_type="abs")
    # print("----")
    # bisection(f, -2, 5.0, tolerance, err_type="abs")
    # print("----")
    # incremental_search(f, 0, 0.00001, 100000)

    pfondo = 20000000
    pdeuda = 146000000
    pinit = pdeuda * 0.4
    i1 = 0.015
    i2 = 0.018
    j = 0.02

    print(pinit)
    a1 = (pdeuda - pinit) * ((i1 - j) / (1 - math.pow((1 + j) / (1 + i1), 120)))
    print(a1)

    z = (pinit / math.pow(1 + i2, 60)) + (((a1 / (i2 - j)) * (1 - math.pow((1 + j) / (1 + i2), 120))) / math.pow(1 + i2, 60))
    d = (math.pow(1 + i2, 180) - 1) / (math.pow(1 + i2, 180) * i2)
    a = (z - pfondo) / d

    print(f"pdeuda = {pdeuda}")
    print(f"pfondo = {pfondo}")
    print(f"pinit = {pinit}")
    print(f"pdeuda = {pdeuda}")
    print(f"a1 = {a1}")
    print(f"z = {z}")
    print(f"d = {d}")
    print(f"a = {a}")




if __name__ == "__main__":
    main(sys.argv[1:])

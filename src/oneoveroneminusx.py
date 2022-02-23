import math


# Taylor series for 1/(1-x)
def exec_taylor():
    accum = 1
    disp = None
    dc = 24
    tolerance = 0.5 * (math.pow(10, -dc))
    x = 0.05

    for i in range(1, 20):
        print("--")
        print(f"iter={i+1}")

        next_result = math.pow(x, i)
        accum = accum + next_result
        print(f"subf(x)={accum}")

        disp = next_result
        print(f"disp={disp}")

        if abs(disp) <= tolerance:
            print("HIT!!")

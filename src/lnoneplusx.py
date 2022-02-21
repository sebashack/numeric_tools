import math


# Taylor series for ln(1 + x)
def exec_taylor():
    accum = 0.1
    disp = None
    dc = 0.5 * (math.pow(10, -4))

    for i in range(2, 5):
        print("--")
        print(f"iter={i}")

        next_result = math.pow(0.1, i) / i
        if (i % 2 == 0):
            accum = accum - next_result
            print(f"subf(x)={accum}")
        else:
            accum = accum + next_result
            print(f"addf(x)={accum}")

        disp = next_result
        print(f"disp={disp}")

        if abs(disp) <= dc:
            print("HIT!!")

import sys
import baseconvert
from oneoveroneminusx import exec_taylor


def base(num, inbase, outbase):
    return baseconvert.base(num, inbase, outbase, string=True)


def main(argv):
    # exec_taylor()
    # base(number, input_base, output_base)
    print(base("55.1231923", 10, 2))


if __name__ == "__main__":
    main(sys.argv[1:])

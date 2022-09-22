#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a: int = 10
    b: int = 5
    print(" {:d} + {;d}  = {:d}".format(a, b, (add(a, b))))
    print(" {:d} - {:d}  = {:d}".format(a, b, (sub(a, b))))
    print(" {:d} * {:d}  = {:d}".format(a, b, (mul(a, b))))
    print(" {:d} / {:d}  = {:d}".format(a, b, (div(a, b))))

# Version >= Python3.5
try:
    from math import gcd
# else
except ImportError:
    from fractions import gcd


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(usage='calculate the greatest common divisor of two numbers')
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    args = parser.parse_args()

    print(gcd(args.a, args.b))

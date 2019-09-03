"""fibSeq_recursive.py

Module implementing recursive routines for the calculation of Fibonacci numbers

Notes:
  - Fibonacci numbers are defined by the recursion relation:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)

  - The first few numbers in the Fibonacci sequence read
    n     : 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10
    fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

  - tested using python3 2019-08-29

AUTHOR: OM
DATE: 2019-08-26
"""
import sys


def fib_recursive_BAD(n):
    """Recursive routine for calculating Fibonacci numbers

    Notes:
        - Fibonacci numbers of order n=0,1 are treated as special cases
        - routine has two exit points (that's considered BAD style)

    Args:
        n (int): order of the Fibonacci number

    Returns:
        result (int): n-th Fibonacci number
    """
    if n>=2:
       return fib_recursive_BAD(n-1) + fib_recursive_BAD(n-2)
    else:
       return n


def fib_recursive(n):
    """Recursive routine for calculating Fibonacci numbers

    Notes:
        - Fibonacci numbers of order n=0,1 are treated as special cases
        - routine has only a SINGLE exit point

    Args:
        n (int): order of the Fibonacci number

    Returns:
        result (int): n-th Fibonacci number
    """
    return fib_recursive(n-1) + fib_recursive(n-2) if n>=2 else n



def main():
    N = int(sys.argv[1])
    res = fib_recursive(N)
    print (res)


if __name__=='__main__':
    main()

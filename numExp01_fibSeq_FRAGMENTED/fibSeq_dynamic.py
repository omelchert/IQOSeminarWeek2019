"""fibSeq_dynamic.py

Module implementing dynamic programming routine for the calculation of Fibonacci numbers

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


def fib_dynamic(n):
    """Dynamic programming routine for calculating Fibonacci numbers

    Dynamic programming routine storing all intermediate results in an array.
    Upon completing the main loop, the result is located in the last array
    entry.

    Args:
        n (int): order of the Fibonacci number

    Returns:
        result (int): n-th Fibonacci number
    """
    fSeq = [0]*(n+1)

    if n >=1:
       fSeq[1] = 1
       for i in range(2,n+1):
          fSeq[i]=fSeq[i-1]+fSeq[i-2]

    return fSeq[-1]


def fib_iterative(n):
    """Iterative routine for calculating Fibonacci numbers

    TODO: amend the function to solve the Fibonacci recurrence
        relation using a small number of variables

    Args:
        n (int): order of the Fibonacci number

    Returns:
        result (int): n-th Fibonacci number
    """
    pass


def main():
    N = int(sys.argv[1])
    res =fib_dynamic(N)
    print(res)


if __name__=='__main__':
    main()

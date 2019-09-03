"""main_timing.py

Skript implementing a benchmark test, measuting the execution time of the
Fibonacci algorithms fib_recursive() and fib_dynamic().

NOTE:
  - tested using python3 2019-08-29

AUTHOR: OM
DATE: 2019-08-26
"""
from timeit import Timer
import matplotlib.pyplot as plt


def main():
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    nMax = 25       # maximum order
    tList_rec = []  # array holding timing results
    tList_dyn = []  # array holding timing results

    # -- PART 2: RUN SIMULATION
    for N in range(nMax):

        # -- SET UP TIMER FOR RECURSIVE ROUTINE
        t_rec = Timer(
            "fib_recursive(%d)"%(N),
            "from fibSeq_recursive import fib_recursive"
            )

        # -- SET UP TIMER FOR DYNAMIC ROUTINE
        t_dyn = Timer(
            "fib_dynamic(%d)"%(N),
            "from fibSeq_dynamic import fib_dynamic"
            )

        # -- EXECUTE 10 TIMES AND KEEP MINIMAL VALUE
        tList_rec.append( min(t_rec.repeat(10,1)) )
        tList_dyn.append( min(t_dyn.repeat(10,1)) )

    # -- PART 3: SAVE OR SHOW SIMULATION RESULTS 
    plt.figure()
    plt.plot(range(nMax),tList_rec,marker='o',label='recursive')
    plt.plot(range(nMax),tList_dyn,marker='s',label='dynamic')
    plt.yscale('log')
    plt.title('Benchmark test for Fibonacci algorithms')
    plt.ylabel('Execution time $t$ (s)')
    plt.legend(title='Algorithm type:', loc=2)
    plt.xlabel('Order $n$')
    plt.show()


main()

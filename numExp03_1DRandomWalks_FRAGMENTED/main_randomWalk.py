"""main_randomWalk.py

Skript implementing a basic 1D random walk class and
deriving two simple models studied in statistical pysics:
  - 1D random walk
  - restricted 1D random walk

NOTE:
  - tested using python3 2019-08-29

AUTHOR: OM
DATE: 2019-08-26
"""
import sys
import numpy as np
from random import random, seed


class RandomWalk(object):
    """Random walk base class

    Implements data structure allowing to derive subclasses
    specifying more specific types of random walks.

    Args:
        x0 (int): initial position
        p (float): probability to yield step-increment +1 (default: p=0.5)

    Attributes:
        n (int): number of steps in random walk
        x0 (int): initial position
        p (float): probability to yield step-increment +1
        x (int): current position
        dx (object): function implenting random variable used as
            step-increment
    """
    def __init__(self, x0, p=0.5):
        self.n = 0
        self.x0 = x0
        self.x = x0
        self.dx = lambda: -1 if random()<p else 1

    def step(self):
        """Advance random walker by performing a single step."""
        # -- draw random increment and perform step
        self.x += self.dx()
        # -- keep track of the number of steps taken
        self.n += 1


def runUntilTrapped(W, trapSites):
    """advance random walker until it gets trapped

    Function implementing restricted random walk

    Note:
       Considers a 1D lattice with trap-sites at x=0 and x=L (L>0).  A walker
       starts at site x0 (0<x0<L) and takes unit steps to the left and right
       with equal probability. When the walker arrives at a trap site, it can
       no longer move.

    Args:
        W (RandomWalk object): random walker
        trapSites (set): integer ids of trapping sites

    Returns:
        nSteps (int): number of steps until trapping occurs
    """
    while W.x not in trapSites:
       W.step()
    return W.n


def main01():
    """example program implementing a short 1D random walk."""
    N = 20
    W = RandomWalk(0)
    for n in range(N):
        W.step()
        print(n,W.x)


def main02():
    """example program comuting the endpoint distribution of 1D random walks."""
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    M = 10000           # number of independent runs
    N = 80              # number of steps to take
    hist = dict()       # dictionary used as endpoint histogram

    # -- PART 2: PERFORM SIMULATION 
    for m in range(M):
        W = RandomWalk(0)
        for n in range(N):
            W.step()
        hist[W.x] = hist.setdefault(W.x,0) + 1

    # -- GET SORTED KEYS AND VALUES
    keys,vals = zip(*sorted(hist.items()))

    # -- NORMALIZE values
    vals = np.asarray(vals,dtype=float)/np.sum(vals)

    # -- PART 3: SHOW RESULTS
    import matplotlib.pyplot as plt
    plt.plot(keys,vals,marker='o')
    plt.xlabel('endpoint')
    plt.ylabel('pmf')
    plt.show()


def main03():
    """example program implementing a restricted 1D random walk."""
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    s0 = 1000       # seed for random number generator
    x0 = 20         # initial position of random walker
    sites = (0,100) # trap sites

    seed(s0)
    W = RandomWalk(20)

    # -- PART 2: PERFORM SIMULATION 
    runUntilTrapped(W,sites)

    # -- PART 3: SHOW SIMULATION RESULTS 
    print ('# (nSteps) (trapped at site)')
    print(W.n,W.x)


def main_displacement():
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    M = 20000           # number of independent runs
    N = 100             # number of stes to take
    x0 = 0              # initial position of walker
    x = np.zeros(N+1)   # average displacement 
    x2 = np.zeros(N+1)  # mean square displacement
    fName = 'RW_displacement.dat' # out-file name

    # -- PART 2: PERFORM SIMULATION
    # -- LOOP OVER INDEPENDENT RUNS
    for m in range(M):
        W = RandomWalk(x0)
        # -- PERFORM WALK AND ACCUMULATE STATISTICS 
        for n in range(N):
           W.step()
           # TODO: amend the lines below to accumulate displacement 
           # and squared displacement
           x[W.n] += 0.0
           x2[W.n] += 0.0
        del W

    # -- PART 3: SAVE RESULTS
    np.savez_compressed(fName,x=x/M, x2=x2/M)


def main_restrictedRW():
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    M = 50000           # number of independent runs
    x0 = 15             # initial position of walker
    L = 50              # trapping sites
    D = 0.5             # 1D diffusion coefficient
    tau = np.zeros(M)   # steps until trapping occurs
    tauExact = x0*(L-x0)/2.0/D
    fName = 'RRW_meanFirstPassageTime.dat'

    # -- PART 2: PERFORM SIMULATION
    for m in range(M):
        W = RandomWalk(x0)
        # TODO: amend loop so that the number of steps until 
        # trapping occurs is recorded for each independent walk
        tau[m] = 0

    # -- NORMALIZE RUNNING AVERAGE
    tauAv = np.cumsum(tau)/np.arange(1,tau.size+1)

    # -- PART 3: SAVE RESULTS
    np.savez_compressed(fName,tau=tauAv,tauEx=tauExact)


def main_endpointDistribution():
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    M = 10000           # number of independent runs
    N = 80              # number of steps to take
    p = 0.1             # probability to step to left/right
    hist = dict()       # dictionary used as endpoint histogram

    # -- PART 2: PERFORM SIMULATION 
    for m in range(M):
        W = RandomWalk(0)
        for n in range(N):
            W.step()
        hist[W.x] = hist.setdefault(W.x,0) + 1

    # -- GET SORTED KEYS AND VALUES
    keys,vals = zip(*sorted(hist.items()))

    # -- NORMALIZE values
    vals = np.asarray(vals,dtype=float)/np.sum(vals)

    # -- PART 3: SHOW RESULTS
    import matplotlib.pyplot as plt
    plt.plot(keys,vals,marker='o')
    plt.xlabel('endpoint')
    plt.ylabel('pmf')
    plt.show()


#main01()
#main02()
#main03()
#main_displacement()
#main_restrictedRW()
#main_endpointDistribution()

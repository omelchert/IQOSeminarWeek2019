"""figure_diffusionCoefficient.py

Skript for basic analysis and figure generation.

NOTE:
  - tested using python3 2019-08-29

AUTHOR: OM
DATE: 2019-08-29
"""
import numpy as np
import matplotlib.pyplot as plt



def main():
    fName = 'RRW_meanFirstPassageTime.dat.npz'

    # -- FETCH DATA FROM FILE
    dat = np.load(fName)
    tau = dat['tau']
    tauExact = dat['tauEx']
    n = np.arange(1,tau.size+1)

    plt.plot(n,tau)
    plt.ylim(0.95*tauExact,1.05*tauExact)
    plt.axhline(tauExact,color='black', linestyle='--')
    plt.ylabel(r'Mean first passage time $\tau$')
    plt.xlabel(r'number of steps')

    plt.show()


main()

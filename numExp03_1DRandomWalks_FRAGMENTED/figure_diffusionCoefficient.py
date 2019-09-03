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
    fName = 'RW_displacement.dat.npz'

    # -- FETCH DATA FROM FILE
    dat = np.load(fName)
    x = dat['x']
    x2 = dat['x2']
    n = np.arange(1,x.size+1)

    # -- COMPUTE SELF-DIFFUSION COEFFICIENT
    D = 0.5*x2/n
    D_exact = 0.5

    # -- PREPARE FIGURE
    plt.figure(1)
    plt.subplot(211)
    plt.plot(n,x)
    plt.axhline(0,color='black', linestyle='--')
    plt.ylabel(r'Average displacement $\langle x \rangle$')

    plt.subplot(212)
    plt.plot(n,x2)
    plt.plot(n, n, color='black', linestyle='--')
    plt.xlabel(r'number of steps')
    plt.ylabel(r'Mean-square displacement $\langle x^2 \rangle$')

    plt.figure(2)
    plt.ylim(0.3,0.55)
    plt.plot(n,D)
    plt.axhline(D_exact, color='black', linestyle='--')
    plt.xlabel(r'number of steps')
    plt.ylabel(r'Diffusion coefficient $D$')

    plt.show()


main()

"""main_1DDiffusionEq.py

Skript implementing forward-time centered space solver
for 1D diffusion equation.

NOTE:
  - tested using python3 2019-08-30

AUTHOR: OM
DATE: 2019-08-29
"""
import sys
import time
import numpy as np
import matplotlib.pyplot as plt


def FTCS_sequential(x,t,u0,D=1.0):
    """Solver for 1D diffusion equation (serial version)

    Implements forward-time centered-space discretization
    of one-dimensional diffusion equation.

    Args:
        x (1D numpy array, float): 1D space-coordinate mesh
        t (1D numpy array, float): 1D time-coordinate mesh
        u0 (1D numpy array, float): initial condition
        D (float): diffusion coefficient (default: D=0.5)

    Returns:
        u (1D numpy array, float): final system state
    """
    dt = t[1]-t[0]
    dx = x[1]-x[0]
    C = D*dt/dx/dx
    um = np.copy(u0)
    u = np.copy(u0)

    for ti in range(t.size):

        # -- UPDATE INNER MESH POINTS
        for i in range(1,x.size-1):
            u[i] = um[i] + C*(um[i-1] - 2*um[i] + um[i+1])

        # -- IMPOSE BOUNDARY CONDITIONS
        u[0]=0; u[-1]=0

        # -- PROCEED TO NEXT STEP
        um[:]=u

    return u


def FTCS_vectorized(x, t, u0, D=0.5):
    """Solver for 1D diffusion equation (vectorized version)

    Implements forward-time centered-space discretization
    of one-dimensional diffusion equation.

    Notes:
        - vectorized version using displaced system slices
        - implies boundary conditions u[0]=u[-1]=0

    Args:
        x (1D numpy array, float): 1D space-coordinate mesh
        t (1D numpy array, float): 1D time-coordinate mesh
        u0 (1D numpy array, float): initial condition
        D (float): diffusion coefficient (default: D=0.5)

    Returns:
        u (1D numpy array, float): final system state
    """
    dt = t[1]-t[0]
    dx = x[1]-x[0]
    C = D*dt/dx/dx
    u = np.copy(u0)

    for ti in range(t.size):
        u[1:-1] = u[1:-1] + C*(u[:-2] - 2*u[1:-1] + u[2:])

    return u


def fetchSolver(algType='vec'):
    """Solver handler

    Switch for easy access to implemented solver types

    Args:
      algType (str): type of algorithm to use (default: vec)

    Returns:
      alg (object): algorithm
    """
    return {
      'seq': FTCS_sequential,
      'vec': FTCS_vectorized
    }.get(algType)


def main():
    # -- PART 1: DECLARE/INITIALIZE PARAMETERS
    tMax = 100.     # upper bound for time evolution 
    Nt = 301        # number of time-steps
    Nx = 2001       # number of space point
    xMin = -1000.   # lower bound for simulation domain
    xMax = 1000.    # upper bound for simulation domain
    D = 0.5         # diffusion coefficient
    sType = 'vec'   # solver type: choices are 'seq' or 'vec'

    # -- initialize computational domain
    x = np.linspace(xMin,xMax,Nx,endpoint=True)
    t = np.linspace(0.,tMax,Nt,endpoint=True)

    # -- initialze solver
    solver = fetchSolver(sType)

    # -- set initial condition
    u0 = np.zeros(Nx); u0[int(Nx/2)]=1.

    # -- exact solution
    # TODO: Amend the line below to implement the 1D exact result
    uExFunc = None

    # -- PART 2: PERFORM SIMULATION 
    tIni = time.clock()
    u = solver(x,t,u0,D)
    tFin = time.clock()

    # -- PART 3: SHOW SIMULATION RESULTS 
    # -- DUMP CPU-TIME SPEND BY SOLVER
    print("# sType: %s, CPU-time: %lf s"%(sType, tFin-tIni))

    # -- PREPARE FIGURE SHOWING FINAL CONFIGURATION
    plt.plot(x,u,label='numerical solution')
    # TODO: Insert a line adding the 1D analytic result to the generated plot
    plt.xlim(-50,50)
    plt.xlabel(r'Coordinate $x$')
    plt.ylabel(r'Field-value $u(x)$')
    plt.title(r'FTCS-approximation to 1D diffusion equation, solver type: %s'%(sType))
    plt.legend()
    plt.show()


main()

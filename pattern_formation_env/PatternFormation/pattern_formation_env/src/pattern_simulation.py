import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend

import numpy as np
import matplotlib.pyplot as plt
from .reaction_diffusion import finite_difference_step, f, g

def main():
    # Parameters
    L = 1.0
    N = 100
    dx = L / N
    dt = 0.01
    Tmax = 500
    delta1 = 0.16
    delta2 = 0.08

    # Initial conditions
    u = np.random.rand(N, N)
    v = np.random.rand(N, N)

    # Simulation loop
    for t in range(Tmax):
        u, v = finite_difference_step(u, v, delta1, delta2, dt, dx)

        if t % 50 == 0:
            plt.imshow(u, cmap='hot', interpolation='nearest')
            plt.colorbar()
            plt.title(f"Time step {t}")
            plt.savefig(f"pattern_{t}.png")  # Save the plot as an image

if __name__ == "__main__":
    main()

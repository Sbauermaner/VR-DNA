import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dna_helix(n_turns=10, points_per_turn=50):
    """Генерация спирали ДНК в 3D"""
    theta = np.linspace(0, 2 * np.pi * n_turns, points_per_turn * n_turns)
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.linspace(0, n_turns, points_per_turn * n_turns)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label="ДНК спираль")
    ax.legend()
    plt.show()

# Пример
dna_helix()

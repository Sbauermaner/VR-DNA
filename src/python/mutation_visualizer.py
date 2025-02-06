import matplotlib.pyplot as plt
import numpy as np

def visualize_mutation(sequence, mutation_index):
    dna_colors = ['#FF0000' if i == mutation_index else '#0000FF' for i in range(len(sequence))]
    plt.bar(range(len(sequence)), np.ones(len(sequence)), color=dna_colors)
    plt.show()

visualize_mutation("ATCGGCTA", 3)

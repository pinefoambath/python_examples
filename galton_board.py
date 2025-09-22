# This program creates a computer simulation of a Galton Board.The simulation works in these steps:

# Setup: It asks you for the height of the board (how many rows of nails) and the number of balls to drop. It then creates a series of collection "bins" at the bottom using a NumPy vector.

# Random Path Simulation: For each ball, the program simulates its journey. At every level of the board (for the given height), a 50/50 random choice is made, causing the ball's position to shift slightly left or right.

# Data Collection: After a ball has passed all the nails, its final horizontal position determines which bin it falls into. The program calculates the correct bin and adds one to its counter in the NumPy vector.

# Visualization: Once all balls have been dropped, the program prints the final counts and, most importantly, uses Matplotlib to generate a bar chart. This chart visually shows the distribution of the balls in the bins. You will see that most balls cluster in the center, forming a bell-shaped curve.

# It's basically a Monte Carlo Simulation: A Monte Carlo simulation is a method that uses a large number of repeated random experiments to solve a problem. This program runs the random experiment of dropping a ball thousands of times to find the final, predictable distribution pattern.

# A stochastic system is one influenced by randomness. The path of a single ball is random and unpredictable. However, this simulation shows that the collective result of many random events is not random at all, but forms a structured pattern (the Binomial distribution).


import random as rd
import numpy as np
import matplotlib.pyplot as plt

height = int(input("Height? "))
num_balls = int(input("Number of balls? "))

num_bins = height + 1
bins = np.zeros(num_bins, dtype=int)

for _ in range(num_balls):
  
    position = 0

    for _ in range(height):

        if rd.random() < 0.5:
            position -= 0.5  # Move left
        else:
            position += 0.5  # Move right
            
    bin_index = int(position + height / 2)
    bins[bin_index] += 1


print("\n--- Simulation Results ---")
print(f"Final counts in the {num_bins} bins:")
print(bins)


bin_labels = np.arange(num_bins) # Create labels 0, 1, 2,etc for x-axis

plt.bar(bin_labels, bins, color='teal')
plt.title("Galton Board Simulation Results")
plt.xlabel("Bin Number")
plt.ylabel("Number of Balls")
plt.xticks(bin_labels) 
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()

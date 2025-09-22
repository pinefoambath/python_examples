"""
This program creates a computer simulation of a Galton Board.

The simulation works in these steps:
1. Setup: 
   Asks for the board height and number of balls. It then creates 
   a series of collection "bins" using a NumPy vector.

2. Random Path Simulation: 
   For each ball, the program simulates its journey. At every level of 
   the board, a 50/50 random choice is made, causing the ball's 
   position to shift left or right.

3. Data Collection: 
   After a ball passes all the nails, its final position determines 
   which bin it falls into. The program calculates the correct bin and 
   adds one to its counter in the NumPy vector.

4. Visualization: 
   Once all balls are dropped, the program uses Matplotlib to generate 
   a bar chart, showing the final distribution in the bins, which 
   forms a bell-shaped curve.

Key Concepts:
- Monte Carlo Simulation: The program runs thousands of random experiments 
  (dropping a ball) to find a predictable, overall pattern.
  
- Stochastic System: The path of a single ball is random, but the 
  collective result of many balls is an orderly, predictable pattern 
  (the Binomial distribution; bell curve).
"""


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

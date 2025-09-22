"""
# --- KEY LEARNINGS FOR FOREST FIRE SIMULATION ---

This program is a practical exercise in modeling a complex, dynamic system 
(a forest ecosystem) using a NumPy matrix. It's a classic example of a cellular automaton, where simple local rules lead to complex global behavior.

### 1. Modeling a Complex System with a Matrix
- The forest is represented by a 2D NumPy array (a grid), where 
  each cell has a state (Empty, Tree, or Fire). This demonstrates how to 
  translate a real-world environment into a data structure.

### 2. Emergent Behavior from Simple Rules
- This is the most important lesson. The simulation is governed 
  by simple, local rules (e.g., a tree only checks its immediate neighbors 
  to see if they are on fire). However, running the simulation reveals 
  complex, large-scale patterns (emergent behavior) like how the fire 
  spreads and dies out.
- The `update()` function applies these simple rules to each 
  cell, but the overall result is a dynamic, unpredictable simulation.

### 3. The Power of Simulation
- It's impossible to write a single mathematical equation to 
  perfectly describe the fire's spread. Instead, we simulate the process 
  step-by-step to observe and understand its dynamics.
- The main loop (`for t in range(...)`) repeatedly calls 
  `update()` to move the simulation forward in time, allowing us to see how 
  the forest evolves.

### 4. Data Collection and Visualization
- A simulation's value comes from analyzing its results. We 
  collect data at each step and then visualize it to understand what's happening.
- The `count()` function gathers data (number of burning trees) at each time step
  At the end, `matplotlib.pyplot.plot()` creates a graph showing the history of the fire, making the trend easy to interpret.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import os

def print_grid(grid):
    """Prints the current state of the forest."""
    for row in grid:
        print(" ".join(row))
    print()

def setup():
    """Initializes the forest grid based on simulation parameters."""
    new_grid = np.full((size, size), EMPTY, dtype=str)
    
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            if np.random.rand() < grow_start:
                new_grid[r, c] = TREE
    return new_grid

def burn(grid, r, c):
    """Checks if any neighbor of a cell (r, c) is on fire."""
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue # Don't check the cell itself
            if grid[r + i, c + j] == FIRE:
                return True # Found a burning neighbor
    return False

def count(grid):
    return np.count_nonzero(grid == FIRE)

def update(grid):
    # Create a new grid to store the next state
    new_grid = np.copy(grid)

    # Loop through each cell in the interior of the grid
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            cell = grid[r, c]
            
            # Rule 1: An empty cell can grow a tree
            if cell == EMPTY:
                if np.random.rand() < p:
                    new_grid[r, c] = TREE
            
            # Rule 2: A tree can catch fire
            elif cell == TREE:
                # Check for burning neighbors
                if burn(grid, r, c):
                    new_grid[r, c] = FIRE
                # Check for a random lightning strike
                elif np.random.rand() < lightning:
                    new_grid[r, c] = FIRE
            
            # Rule 3: A burning tree turns to ash (empty)
            elif cell == FIRE:
                new_grid[r, c] = EMPTY
                
    return new_grid


# States
EMPTY = "."
TREE  = "🌳"
FIRE  = "🔥"

# Simulation parameters
size = 30         # Grid size (including a 1-cell border)
grow_start = 0.6  # Probability that there is a tree at the beginning
p = 0.01          # Probability of a new tree growing on an empty cell
lightning = 0.001 # Probability of a lightning strike starting a fire
tEnd = 200        # Number of time steps to simulate

# A list to store the number of burning trees at each time step
fire_counts = []

# Initial matrix
Grid = setup()
fire_counts.append(count(Grid))

# Print start simulation
print("Time: 0")
print_grid(Grid)
time.sleep(1)

# --- Simulation Loop ---
for t in range(1, tEnd + 1):
    Grid = update(Grid)
    fire_counts.append(count(Grid))
    
    # Print the current state
    print(f"Time: {t}")
    print_grid(Grid)
    print(f"Burning Trees: {fire_counts[-1]}")
    time.sleep(0.1) # Pause to make the animation viewable

# --- Visualization ---
print("\nSimulation finished. Generating plot...")

plt.figure(figsize=(12, 6))
plt.plot(range(tEnd + 1), fire_counts, color='red')
plt.title(f'Forest Fire Simulation (size={size-2}x{size-2}, p={p}, lightning={lightning})')
plt.xlabel('Time')
plt.ylabel('Number of Burning Trees')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
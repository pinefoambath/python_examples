"""
# --- KEY LEARNINGS ---

This program models how heat spreads across a 2D plate, demonstrating 
concepts from computational physics.

1.  Modeling with a Matrix: The physical plate is represented by a 2D 
    NumPy array, where each cell's value is its temperature.

2.  Discretization: We solve the continuous problem of heat flow by 
    breaking it into discrete parts: a grid of cells and a series of time 
    steps. The temperature of each cell is updated based on its neighbors, 
    approximating the real-world heat equation.

3.  Simulation over Time: The `animate` function is called repeatedly to 
    show how the system evolves from its initial state, with the new state 
    depending on the previous one.

4.  Animation: `matplotlib.animation.FuncAnimation` is used to visualize the results of the simulation dynamics.
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Plate at the beginning with a base temperature of 20 degrees
plate = np.zeros((24,24),int)
plate[:,:] = 20
# heat sources
plate[4,4:21]  = 99
plate[5:10,20] = 80
plate[11:20,4] = 50
plate[20,4:21] = 60

# heat conduction coefficient
prop = 0.2

# cycles
cycles = 50

# height and width of the plate
height, width = plate.shape
  
...
  
print("heat conduction coefficient:", prop)
print("number of cycles:", cycles)
print("matrix size:", height,"x",width)

# copy values of plate into plate_new
plate_old = np.copy(plate)
plate_new = np.copy(plate)

def animate(cycles):
  global plate_old
  global plate_new
  plt.title("Heat propagation in a plate (cycle: " + str(cycles) + ")")
  
  contour = plt.contourf(plate_old)

  for i in range(1, height - 1):
      for j in range(1, width - 1):
        center = plate_old[i, j]
        above = plate_old[i - 1, j]
        below = plate_old[i + 1, j]
        left = plate_old[i, j - 1]
        right = plate_old[i, j + 1]
        sum_neighbors = left + right + above + below
        plate_new[i, j] = (1 - 4 * prop) * center + prop * sum_neighbors
  
        plate_new[4,4:21]  = 99
        plate_new[5:10,20] = 80
        plate_new[11:20,4] = 50
        plate_new[20,4:21] = 60
    
  # Update the newly calculated matrix values
  plate_old = np.copy(plate_new)

# Animate
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=cycles, interval=10, blit=False)

contour = plt.contourf(plate) 
plt.colorbar(contour)


writer = animation.PillowWriter(fps=1)
ani.save("./cx_out/case_study_plate.gif", writer=writer)

for i in range (0,24):
  for j in range (0,24):
      print(plate[i][j], end= " ")
  print()
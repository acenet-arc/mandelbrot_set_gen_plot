''' This version both generates and plots data
'''

import numpy as np
import matplotlib
#matplotlib.use('Agg')
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

#NOTE: setting parameters (these values can be changed)
settings={
  "x_limits":(-2.0,2.0),
  "y_limits":(-2.0,2.0),
  "resolution":(500,500),
  "bound": 2,
  "max_iterations": 50,
  "colormap":"nipy_spectral"
}

xDomain = np.linspace(settings["x_limits"][0], settings["x_limits"][1], settings["resolution"][0])
yDomain = np.linspace(settings["y_limits"][0], settings["y_limits"][1], settings["resolution"][1])

func = lambda z, p, c: z**p + c

#NOTE: computing 2-d array to represent the mandelbrot-set
iterationArray = []
for y in yDomain:
    row = []
    for x in xDomain:
        z = 0
        p = 2
        c = complex(x, y)
        for iterationNumber in range(settings["max_iterations"]):
            if abs(z) >= settings["bound"]:
                row.append(iterationNumber)
                break
            else:
                try:
                    z = func(z, p, c)
                except(ValueError, ZeroDivisionError):
                    z = c
        else:
            row.append(0)

    iterationArray.append(row)

#NOTE: plotting the data
ax = plt.axes()
ax.set_aspect("equal")
graph = ax.pcolormesh(xDomain, yDomain, iterationArray, cmap=settings["colormap"])
plt.colorbar(graph)
plt.xlabel("Real-Axis")
plt.ylabel("Imaginary-Axis")
plt.show()

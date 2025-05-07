''' This version generates and writes out data
'''

import numpy as np

#NOTE:  setting parameters (these values can be changed)
settings={
  "x_limits":(-2.0,2.0),
  "y_limits":(-2.0,2.0),
  "resolution":(800,400),
  "bound": 2.0,
  "max_iterations": 50,
  "outputFileName":"set.txt",
  "outputNumberWidth":3
}

#NOTE: evaluate at cell centers rather than cell boundaries so that plotting 
#is accurate otherwise it will be off by half a cell, little difference seen
#between the two really
if False:
    x_delta=( settings["x_limits"][1]-settings["x_limits"][0] )/float(settings["resolution"][0])
    x_delta2=x_delta*0.5
    y_delta=( settings["y_limits"][1]-settings["y_limits"][0] )/float(settings["resolution"][1])
    y_delta2=y_delta*0.5
    xDomain = np.linspace(settings["x_limits"][0]+x_delta2, settings["x_limits"][1]-x_delta2, settings["resolution"][0])
    yDomain = np.linspace(settings["y_limits"][0]+y_delta2, settings["y_limits"][1]-y_delta2, settings["resolution"][1])
else:
    xDomain = np.linspace(settings["x_limits"][0], settings["x_limits"][1], settings["resolution"][0])
    yDomain = np.linspace(settings["y_limits"][0], settings["y_limits"][1], settings["resolution"][1])

func = lambda z, p, c: z**p + c

#NOTE: computing 2-d array to represent the mandelbrot-set
iterationArray = []
for y in yDomain:
    row = []
    line=""
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

#NOTE: write out set
file=open(settings["outputFileName"],"w")
file.write(str(settings["x_limits"][0])+" "+str(settings["x_limits"][1])+" "+str(settings["y_limits"][0])+" "+str(settings["y_limits"][1])+"\n")
file.write(str(settings["resolution"][0])+" "+str(settings["resolution"][1])+"\n")
for j in range(settings["resolution"][1]):
  line=""
  for i in range(settings["resolution"][0]):
    line+=("%"+str(settings["outputNumberWidth"])+"d") % iterationArray[settings["resolution"][1]-j-1][i]
  file.write(line+"\n")
file.close()


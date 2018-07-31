import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2: return n
        z = z*z + c
    return max_iter


xmin = -1.5
xmax = 0.6
ymin = -1
ymax = 1

width = 1000
height = 1000
max_iter = 50

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, width)

mbrot = np.array(
    [mandelbrot(complex(i,j), max_iter) for i in x for j in y]
).reshape(width, height).transpose()
plt.matshow(mbrot)
plt.show()

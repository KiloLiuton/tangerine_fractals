import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    '''Determines if complex number c belongs to the Mandelbrot set.
    Parameters:
    c - python complex number
    max_iter - integer: the maximum number of iterations allowed to determine if
    the series diverges

    Returns:
    n - integer: the number of iterations it took for point c to diverge or
    max_iter
    '''
    z = c
    for n in range(1, max_iter + 1):
        if abs(z) > 2: return n
        z = z*z + c
    return n


# define the boundaries of the plot
xmin = -1.5
xmax = 0.6
ymin = -1
ymax = 1

# define how many points will be sampled inside the boundaries
width = 1000
height = 1000
max_iter = 50

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, width)

# for each complex point c in the xy grid, determine if it belongs to the
# Mandelbrot set
mbrot = np.array(
    [mandelbrot(complex(i,j), max_iter) for i in x for j in y]
).reshape(width, height).transpose()
plt.matshow(mbrot)
plt.show()

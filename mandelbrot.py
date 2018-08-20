import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def mandelbrot(c, max_iter):
    '''Determines if complex number c belongs to the Mandelbrot set.
    Parameters:
    c - python complex number: point under consideration
    max_iter - integer: the maximum number of iterations allowed to determine
    if the series diverges

    Returns:
    n - integer: the number of iterations it took for point c to diverge or
    max_iter
    '''
    z = c
    for n in range(max_iter):
        if (abs(z) > 2):
            return n
        z = z*z + c
    return max_iter


def mandelbrot_arr(c_arr, max_iter):
    z = c_arr
    result = np.empty(z.shape)
    diverged = np.full(z.shape, False)
    for n in range(max_iter):
        tmp = abs(z) > 2
        result[tmp & ~diverged] = n
        diverged += tmp
        z = z*z + c_arr
    result[~diverged] = max_iter
    return result


def julia_arr(z_arr, c, max_iter):
    result = np.empty(z_arr.shape)
    diverged = np.full(z_arr.shape, False)
    for n in range(max_iter):
        tmp = abs(z_arr) > 2
        result[tmp & ~diverged] = n
        diverged += tmp
        z_arr = z_arr*z_arr + c
    result[~diverged] = max_iter
    return result


# define the boundaries of the plot
xmin = -1.2
xmax = 1.2
ymin = -1.2
ymax = 1.2

# define how many points will be sampled inside the boundaries
width = 1000
height = 1000
max_iter = 70

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
arr = np.meshgrid(x, y)
arr = arr[0] + 1j*arr[1]

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111)


def save_julia_ani(fps, duration, fname='foo.mp4'):
    im = ax.matshow(julia_arr(arr, 0, max_iter))

    def init():
        im.set_data(np.zeros(arr.shape))
        return im,

    def update(c):
        jul = julia_arr(arr, c, max_iter)
        im.set_data(jul)
        return im,

    n_frames = duration * fps
    frames = 0.7885*np.exp(1j*np.linspace(0, 2*np.pi, n_frames))
    ani = FuncAnimation(
                fig, update,
                init_func=init,
                frames=frames,
                interval=1000 / fps
            )
    ani.save(fname)


if __name__ == "__main__":
    ax.imshow(mandelbrot_arr(arr, max_iter))
    plt.show()


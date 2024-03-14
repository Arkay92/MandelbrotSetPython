import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def display_mandelbrot(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256):
    dpi = 100
    img_width = dpi * width
    img_height = dpi * height
    x, y, mandelbrot_set = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

    plt.figure(figsize=(width, height), dpi=dpi)
    plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax), cmap="hot")
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

# Parameters
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 10, 10
max_iter = 256

display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

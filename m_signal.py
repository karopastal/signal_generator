import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

T = 20
MASS_NUM = 1000
MIN_MASS = 1
MAX_MASS = 10000
AMPLITUDE_DECAY_RATE = 0.09


def amplitude(n):
    return np.exp(-1*AMPLITUDE_DECAY_RATE*n)


def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset


def gaussianify(all_periods, n, height, center, width, offset):
    for j in range(all_periods.shape[1]):
        all_periods[n, j] = gaussian(j, height, center, width, offset)


def psi(mass_range):
    all_periods = np.zeros((T, len(mass_range)))

    for n in range(T):
        height = amplitude(n)
        center = 10 + n*50
        width = 3 + n
        offset = 0

        gaussianify(all_periods, n, height, center, width, offset)

    return all_periods.sum(axis=0)


def main():
    mass_range = np.linspace(MIN_MASS, MAX_MASS, 500)
    plt.plot(mass_range, psi(mass_range))

    plt.title(r"Signal")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()

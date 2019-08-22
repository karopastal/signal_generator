import numpy as np
import matplotlib.pyplot as plt

T = 50
MASS_NUM = 15000
MIN_MASS = 1
MAX_MASS = 15000
AMPLITUDE_DECAY_RATE = 0.1


def amplitude(n):
    return np.exp(-1*AMPLITUDE_DECAY_RATE*n)


def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset


def gaussianify(all_periods, n, height, center, width, offset):
    for j in range(all_periods.shape[1]):
        all_periods[n, j] = gaussian(j, height, center, width, offset)


def mass_range():
    return np.linspace(MIN_MASS, MAX_MASS, MASS_NUM)


def psi_signal():
    x = mass_range()
    all_periods = np.zeros((T, len(x)))

    for n in range(T):
        height = 50*amplitude(n)
        center = n*1000
        width = 50 + n*20
        offset = 0

        gaussianify(all_periods, n, height, center, width, offset)

    return all_periods.sum(axis=0)


def main():
    x = mass_range()

    plt.plot(x, psi_signal())
    plt.title(r"Signal")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()

import numpy as np
import matplotlib.pyplot as plt
import background
import mass_signal

RANGE_NUM = 1000
MIN_RANGE = 1
MAX_RANGE = 10000


def fluctuations_range():
    return np.linspace(MIN_RANGE, MAX_RANGE, RANGE_NUM)


def psi_fluctuations():
    return background.psi_background() + mass_signal.psi_signal()


def main():
    x = fluctuations_range()

    plt.plot(x, psi_fluctuations())
    plt.title(r"Signal")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()
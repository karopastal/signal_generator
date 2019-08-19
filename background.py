import numpy as np
import matplotlib.pyplot as plt

BACKGROUND_DECAY_RATE = 0.00005
BG_NUM = 100000
MIN_BG = 1
MAX_BG = 100000


def max_bg():
    return MAX_BG


def bg_num():
    return BG_NUM


def amplitude():
    return 10


def background_noise(n):
    return amplitude()*np.exp(-1*BACKGROUND_DECAY_RATE*n)


def background_range():
    return np.linspace(MIN_BG, MAX_BG, BG_NUM)


def psi_background():
    x = background_range()
    out = np.zeros_like(x)

    for n in range(len(out)):
        out[n] = background_noise(n)

    return out


def main():
    plt.plot(background_range(), psi_background())

    plt.title(r"Background")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()



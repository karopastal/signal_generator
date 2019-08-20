import numpy as np
import matplotlib.pyplot as plt
import background
import clean

RANGE_NUM = background.bg_num()
MIN_RANGE = 1
MAX_RANGE = background.max_bg()


def bins_mean():
    return clean.bins_segments().mean(axis=1) * clean.bin_segment_size()


def fluctuations_range():
    return np.linspace(MIN_RANGE, MAX_RANGE, RANGE_NUM)


def psi_fluctuations():
    x = fluctuations_range()
    out = np.zeros_like(x)

    for bin_idx, lam in enumerate(bins_mean()):
        rand_bin = np.random.poisson(lam, clean.bin_segment_size())
        start_bin = bin_idx * clean.bin_segment_size()
        end_bin = start_bin + clean.bin_segment_size()
        out[start_bin:end_bin] = rand_bin

    return out


def main():
    x = fluctuations_range()

    plt.plot(x, psi_fluctuations())
    plt.title(r"Signal + Background + Noise")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()
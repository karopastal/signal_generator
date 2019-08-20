import numpy as np
import matplotlib.pyplot as plt
import background
import mass_signal

RANGE_NUM = background.bg_num()
MIN_RANGE = 1
MAX_RANGE = background.max_bg()
BIN_SEGMENT = 1000


def clean_range():
    return np.linspace(MIN_RANGE, MAX_RANGE, RANGE_NUM)


def psi_clean():
    # default to the median of the background
    signal_start_index = int(background.max_bg()/2)
    signal_end_index = signal_start_index + mass_signal.psi_signal().shape[0]

    out = background.psi_background()
    out[signal_start_index:signal_end_index] += mass_signal.psi_signal()

    return out


def bins_segments():
    return psi_clean().reshape(int(background.max_bg()/BIN_SEGMENT), BIN_SEGMENT)


def bin_segment_size():
    return BIN_SEGMENT


def main():
    x = clean_range()

    plt.plot(x, psi_clean())
    plt.title(r"Signal + Background")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()
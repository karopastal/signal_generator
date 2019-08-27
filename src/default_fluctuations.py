import numpy as np
import matplotlib.pyplot as plt
from default_clean import psi_clean
from default_signal import DefaultSignal
from default_background import DefaultBackground

BIN_SEGMENT = 10


def bins_segments(ds, dbg):
    return psi_clean(ds, dbg).reshape(int(dbg.max_bg / BIN_SEGMENT), BIN_SEGMENT)


def bins_mean(ds, dbg):
    return bins_segments(ds, dbg).mean(axis=1)*BIN_SEGMENT


def psi_fluctuations(ds, dbg):
    x = dbg.background_range()
    out = np.zeros_like(x)

    for bin_idx, lam in enumerate(bins_mean(ds, dbg)):
        rand_bin = np.random.poisson(lam, BIN_SEGMENT)
        start_bin = bin_idx * BIN_SEGMENT
        end_bin = start_bin + BIN_SEGMENT
        out[start_bin:end_bin] = rand_bin

    return out


def main():
    ds = DefaultSignal(id=0)
    dbg = DefaultBackground(id=0)

    x = dbg.background_range()

    plt.plot(x, psi_fluctuations(ds, dbg))
    plt.title(r"Signal + Background + Noise")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()
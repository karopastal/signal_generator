import numpy as np
import matplotlib.pyplot as plt
from default_signal import DefaultSignal
from default_background import DefaultBackground


def psi_clean(ds, dbg):
    # default to the median of the backgrounds
    signal_start_index = int(dbg.max_bg / 2)
    signal_end_index = signal_start_index + ds.psi_signal().shape[0]

    out = dbg.psi_background()
    out[signal_start_index:signal_end_index] += ds.psi_signal()

    return out


def main():
    ds = DefaultSignal(id=0)
    dbg = DefaultBackground(id=0)

    x = dbg.background_range()

    plt.plot(x, psi_clean(ds, dbg))
    plt.title(r"Signal + Background")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()

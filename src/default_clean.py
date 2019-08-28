import sys
import numpy as np
import matplotlib.pyplot as plt
from default_signal import DefaultSignal
from default_background import DefaultBackground


def signal_id():
    try:
        return int(sys.argv[1:][0])
    except:
        print("INFO: illegal or missing SIGNAL_ID, using default")
        return 0


def background_id():
    try:
        return int(sys.argv[1:][1])
    except:
        print("INFO: illegal or missing BG_ID, using default")
        return 0


def psi_clean(ds, dbg):
    # default to the median of the backgrounds
    signal_start_index = int(dbg.bg_num/2)
    signal_end_index = signal_start_index + ds.mass_num

    out = dbg.psi_background()
    out[signal_start_index:signal_end_index] += ds.psi_signal()

    return out


def main():
    ds = DefaultSignal(id=signal_id())
    dbg = DefaultBackground(id=background_id())

    x = dbg.background_range()

    plt.plot(x, psi_clean(ds, dbg))
    plt.title(r"Signal + Background")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()

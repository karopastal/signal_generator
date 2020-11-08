import sys
import os
import matplotlib.pyplot as plt
from src.default_signal import DefaultSignal
from src.default_background import DefaultBackground


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


def save_clean_plot(path, s_id, bg_id):
    ds = DefaultSignal(id=s_id)
    dbg = DefaultBackground(id=bg_id)

    x = dbg.background_range()

    plt.plot(x, psi_clean(ds, dbg))
    plt.title(r"Signal + Background")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    if os.path.isfile(path):
        os.remove(path)

    plt.savefig(path)
    plt.close('all')


def main():
    ds = DefaultSignal(id=signal_id())
    dbg = DefaultBackground(id=background_id())

    x = dbg.background_range()

    fig, ax = plt.subplots(figsize=(9, 7))

    plt.plot(x, psi_clean(ds, dbg))
    plt.title(r"Background + Signal", fontsize=20)
    plt.ylabel("Events/Mass Unit", fontsize=18)
    plt.xlabel("Mass", fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    path = 'docs/output/cwt/clean_bg_signal.jpeg'
    plt.savefig(path)
    plt.close('all')


if __name__ == '__main__':
    main()


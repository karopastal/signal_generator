import sys
import json
import numpy as np
import matplotlib.pyplot as plt


def signal_id():
    try:
        return int(sys.argv[1:][0])
    except:
        print("INFO: illegal or missing SIGNAL_ID, using default")
        return 0


def load_config(id, data):
    if id >= len(data) or id < 0:
        print("WARNING: '%s' wrong SIGNAL_ID, using default." % id)
        return data[0]
    else:
        return data[id]


def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset


def gaussianify(all_periods, n, x_signal_range, height, center, width, offset):
    for j in range(all_periods.shape[1]):
        all_periods[n, j] = gaussian(x_signal_range[j], height, center, width, offset)


class DefaultSignal:
    def __init__(self, id=0):
        with open("config/signals/default_signal.json") as f:
            data = json.load(f)

        config = load_config(id, data)

        self.height = config["gaussian"]["height"]
        self.center = config["gaussian"]["center"]
        self.width = config["gaussian"]["width"]
        # self.offset = config["gaussian"]["offset"]

        self.T = int(config["range"]["T"])
        self.min_mass = int(config["range"]["MIN_MASS"])
        self.max_mass = int(config["range"]["MAX_MASS"])
        self.mass_num = int(config["range"]["MASS_NUM"])
        self.amplitude_decay_rate = float(config["range"]["AMPLITUDE_DECAY_RATE"])

    def amplitude(self, n):
        return np.exp(-1*n*self.amplitude_decay_rate)

    def signal_range(self):
        return np.linspace(self.min_mass, self.max_mass, self.mass_num)

    def psi_signal(self):
        x_signal_range = self.signal_range()
        all_periods = np.zeros((self.T, len(x_signal_range)))

        for n in range(self.T):
            height = float(eval(self.height))*self.amplitude(n)
            center = eval(self.center)
            width = eval(self.width)
            # offset = eval(self.offset)
            offset = 0

            gaussianify(all_periods, n, x_signal_range, height, center, width, offset)

        return all_periods.sum(axis=0)


def main():
    ds = DefaultSignal(id=signal_id())

    plt.plot(ds.signal_range(), ds.psi_signal())
    plt.title('Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('Mass')

    plt.show()


if __name__ == '__main__':
    # main(
    pass

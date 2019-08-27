import json
import numpy as np
import matplotlib.pyplot as plt


def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset


def gaussianify(all_periods, n, height, center, width, offset):
    for j in range(all_periods.shape[1]):
        all_periods[n, j] = gaussian(j, height, center, width, offset)


class DefaultSignal:
    def __init__(self, id=0):
        with open("src/signals/default_signal.json") as f:
            config = json.load(f)[id]

        self.height = config["gaussian"]["height"]
        self.center = config["gaussian"]["center"]
        self.width = config["gaussian"]["width"]
        self.offset = config["gaussian"]["offset"]

        self.T = config["range"]["T"]
        self.min_mass = config["range"]["MIN_MASS"]
        self.max_mass = config["range"]["MAX_MASS"]
        self.mass_num = config["range"]["MASS_NUM"]
        self.amplitude_decay_rate = config["range"]["AMPLITUDE_DECAY_RATE"]

    def amplitude(self, n):
        return np.exp(-1*n*self.amplitude_decay_rate)

    def mass_range(self):
        return np.linspace(self.min_mass, self.max_mass, self.mass_num)

    def psi_signal(self):
        x = self.mass_range()
        all_periods = np.zeros((self.T, len(x)))

        for n in range(self.T):
            height = eval(self.height)*self.amplitude(n)
            center = eval(self.center)
            width = eval(self.width)
            offset = eval(self.offset)

            gaussianify(all_periods, n, height, center, width, offset)

        return all_periods.sum(axis=0)


def main():
    ds = DefaultSignal(id=0)
    plt.plot(ds.mass_range(), ds.psi_signal())
    plt.title(r"Signal")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()

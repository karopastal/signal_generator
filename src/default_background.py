import json
import numpy as np
import matplotlib.pyplot as plt


class DefaultBackground:
    def __init__(self, id=0):
        with open("src/backgrounds/default_background.json") as f:
            config = json.load(f)[id]

        self.amplitude = config["range"]["amplitude"]
        self.min_bg = config["range"]["MIN_BG"]
        self.max_bg = config["range"]["MAX_BG"]
        self.bg_num = config["range"]["BG_NUM"]
        self.background_decay_rate = config["range"]["BACKGROUND_DECAY_RATE"]

    def background_noise(self, n):
        return self.amplitude*np.exp(-1*n*self.background_decay_rate)

    def background_range(self):
        return np.linspace(self.min_bg, self.max_bg, self.bg_num)

    def psi_background(self):
        x = self.background_range()
        out = np.zeros_like(x)

        for n in range(len(out)):
            out[n] = self.background_noise(n)

        return out


def main():
    dbg = DefaultBackground(id=0)

    plt.plot(dbg.background_range(), dbg.psi_background())
    plt.title(r"Background")
    plt.ylabel("Amplitude")
    plt.xlabel("Mass")

    plt.show()


if __name__ == '__main__':
    main()

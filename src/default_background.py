import sys
import json
import numpy as np
import matplotlib.pyplot as plt


def background_id():
    try:
        return int(sys.argv[1:][0])
    except:
        print("INFO: illegal or missing BG_ID, using default")
        return 0


def load_config(id, data):
    if id >= len(data) or id < 0:
        print("WARNING: '%s' wrong BG_ID, using default." % id)
        return data[0]
    else:
        return data[id]


class DefaultBackground:
    def __init__(self, id=0):
        with open("config/backgrounds/default_background.json") as f:
            data = json.load(f)

        config = load_config(id, data)

        self.amplitude = float(config["range"]["amplitude"])
        self.min_bg = int(config["range"]["MIN_BG"])
        self.max_bg = int(config["range"]["MAX_BG"])
        self.bg_num = int(config["range"]["BG_NUM"])
        self.background_decay_rate = float(config["range"]["BACKGROUND_DECAY_RATE"])

    def background_noise(self, n):
        return self.amplitude*np.exp(-1*n*self.background_decay_rate)

    def background_range(self):
        return np.linspace(self.min_bg, self.max_bg, self.bg_num)

    def psi_background(self):
        x_background_range = self.background_range()
        out = np.zeros_like(x_background_range)

        for n in range(len(out)):
            out[n] = self.background_noise(x_background_range[n])

        return out


def main():
    dbg = DefaultBackground(id=background_id())

    plt.plot(dbg.background_range(), dbg.psi_background())
    plt.title('Background')
    plt.ylabel('Amplitude')
    plt.xlabel('Mass')

    plt.show()


if __name__ == '__main__':
    pass
    # main()

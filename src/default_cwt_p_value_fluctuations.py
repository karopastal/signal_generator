import sys
import pywt
import json
import numpy as np
import matplotlib.pyplot as plt

from src.old.analysis.datasets_factory.p_value_transformation import p_value_transformation_local
from src.default_fluctuations import psi_fluctuations
from src.default_clean import psi_clean
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


def wavelet_id():
    try:
        return int(sys.argv[1:][2])
    except:
        print("INFO: illegal or missing WAVELET_ID, using default")
        return 0


def load_config(id, data):
    if id >= len(data) or id < 0:
        print("WARNING: '%s' wrong SIGNAL_ID, using default." % id)
        return data[0]
    else:
        return data[id]


class DefaultCWTFluctuations:
    def __init__(self, id=0):
        with open("config/wavelets/default_wavelet.json") as f:
            data = json.load(f)

        config = load_config(id, data)

        self.B = float(config["wavelet"]["B"])
        self.C = float(config["wavelet"]["C"])
        self.name = config["wavelet"]["name"]
        self.min_scales = int(config["wavelet"]["min_scales"])
        self.max_scales = int(config["wavelet"]["max_scales"])
        self.scales = np.arange(self.min_scales, self.max_scales)
        self.wavelet = pywt.ContinuousWavelet('%s%s-%s' % (self.name, self.B, self.C))

    def generate_coefficients(self, data):
        return pywt.cwt(data, self.scales, self.wavelet)


def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)


def main():
    ds = DefaultSignal(id=signal_id())
    dbg = DefaultBackground(id=background_id())
    cmor = DefaultCWTFluctuations(id=wavelet_id())

    print(cmor.wavelet)

    data = psi_fluctuations(ds, dbg)
    # data = psi_clean(ds, dbg)
    coeffs, freqs = cmor.generate_coefficients(data)

    amp = np.abs(coeffs)
    # new_shape = [48, 64]
    new_shape = [48, 64]

    amp_p_value = p_value_transformation_local(rebin(amp, new_shape), new_shape)

    fig, ax = plt.subplots(figsize=(12, 12))

    img = ax.imshow(rebin(amp, new_shape),
                    extent=(dbg.min_bg, dbg.max_bg, cmor.max_scales, cmor.min_scales),
                    interpolation='sinc',
                    aspect='auto',
                    cmap='bwr')

    ax.set_ylim(cmor.min_scales, cmor.max_scales)
    fig.colorbar(img, ax=ax)

    # plt.title('CWT - scales range: (%s, %s)' % (cmor.min_scales, cmor.max_scales))
    plt.title('CWT of Background + Signal w/ Fluctuations', fontsize=18)
    plt.ylabel('Scales', fontsize=16)
    plt.xlabel('Mass', fontsize=16)
    plt.show()


if __name__ == '__main__':
    main()

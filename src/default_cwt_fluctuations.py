import pywt
import json
import numpy as np
import matplotlib.pyplot as plt
from default_fluctuations import psi_fluctuations
from default_signal import DefaultSignal
from default_background import DefaultBackground

# SAMPLING_RATE = default_fluctuations.sampling_range()
# SAMPLING_PERIOD = 1/SAMPLING_RATE


class DefaultCWTClean:
    def __init__(self, id=0):
        with open("src/wavelets/default_wavelet.json") as f:
            config = json.load(f)[id]

        self.B = config["wavelet"]["B"]
        self.C = config["wavelet"]["C"]
        self.name = config["wavelet"]["name"]
        self.min_scales = config["wavelet"]["min_scales"]
        self.max_scales = config["wavelet"]["max_scales"]
        self.scales = np.arange(self.min_scales, self.max_scales)
        self.wavelet = pywt.ContinuousWavelet('%s%s-%s' % (self.name, self.B, self.C))


def main():
    ds = DefaultSignal(id=0)
    dbg = DefaultBackground(id=0)
    cmor = DefaultCWTClean(id=0)

    print(cmor.wavelet)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = pywt.cwt(data, cmor.scales, cmor.wavelet)

    amp = np.abs(coeffs)

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(amp, interpolation='nearest', aspect='auto')
    plt.show()


if __name__ == '__main__':
    main()

"""
create p_value distribution for a background

1. generate backgrounds
2. determine binning
3. return p-value map
4. how to use it with signal?

working with session: "autoencoder_toy_dataset"

"""

import numpy as np
from scipy.stats import norm

from src.default_background import DefaultBackground
from src.default_signal import DefaultSignal
from src.default_cwt_clean import DefaultCWTClean
from src.default_fluctuations import psi_fluctuations


def generate_sample(signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)
    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def p_value_transformation(x, signal_id=0, bg_id=0, wavelet_id=0):
    samples = []

    for i in range(5):
        samples.append(generate_sample())
        print(generate_sample().shape)

    samples = np.array(samples)

    x = generate_sample()
    mean = np.mean(samples, axis=0)
    sigma = np.std(samples, axis=0)
    z_score = (x - mean) / sigma
    p_value = norm.cdf(z_score)

    return p_value


def main():
    x = generate_sample()
    print(p_value_transformation(x, signal_id=0, bg_id=0, wavelet_id=0))


if __name__ == '__main__':
    main()

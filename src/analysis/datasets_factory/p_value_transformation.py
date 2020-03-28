"""
create p_value distribution for a background

working with session: "autoencoder_toy_dataset"

"""

import numpy as np
from scipy.stats import norm

from src.default_background import DefaultBackground
from src.default_signal import DefaultSignal
from src.default_cwt_clean import DefaultCWTClean
from src.default_fluctuations import psi_fluctuations
from src.default_clean import psi_clean


def generate_sample_fluctuations(signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def generate_sample_clean(signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_clean(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def build_samples_and_probabilities(samples_num, signal_id=0, bg_id=1, wavelet_id=0):

    samples = []

    for i in range(samples_num):
        samples.append(generate_sample_fluctuations(signal_id=0, bg_id=1, wavelet_id=0))

    samples = np.array(samples)
    sum_samples = np.sum(samples, axis=0)
    probabilities = samples / sum_samples

    return samples, probabilities


def calculate_p_value_matrix(cwt_with_signal, samples, probabilities):

    keys = np.argwhere(cwt_with_signal > samples).T
    probabilities[keys[0], keys[1], keys[2]] = 0
    p_values = np.sum(probabilities, axis=0)

    return -1 * np.log(p_values)


def p_value_transformation_local(cwt_signal):

    samples = []

    for i in range(200):
        samples.append(generate_sample_fluctuations(signal_id=0, bg_id=1, wavelet_id=0))

    samples = np.array(samples)
    sum_samples = np.sum(samples, axis=0)
    probabilities = samples / sum_samples

    keys = np.argwhere(cwt_signal > samples).T
    probabilities[keys[0], keys[1], keys[2]] = 0
    p_values = np.sum(probabilities, axis=0)

    return -1 * np.log(p_values)


def main():

    x = generate_sample_clean(signal_id=0, bg_id=0, wavelet_id=0)
    print(p_value_transformation_local(x))


if __name__ == '__main__':
    main()

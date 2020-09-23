"""
create p_value distribution for a background

working with session: "autoencoder_toy_dataset"

"""

import numpy as np
import numpy.ma as ma
from scipy.stats import norm

from src.default_background import DefaultBackground
from src.default_signal import DefaultSignal
from src.default_cwt_clean import DefaultCWTClean
from src.default_fluctuations import psi_fluctuations
from src.default_clean import psi_clean


def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)


def generate_sample_fluctuations(signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def generate_rebined_sample_fluctuations(rebined_shape, signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    rebined_amp = rebin(amp, rebined_shape)

    return rebined_amp


def generate_sample_clean(signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_clean(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def build_samples_and_probabilities(samples_num, rebined_shape, signal_id=0, bg_id=0, wavelet_id=0):

    samples = []

    for i in range(samples_num):
        samples.append(generate_sample_fluctuations(signal_id,
                                                    bg_id,
                                                    wavelet_id))
    samples = np.array(samples)
    sum_samples = np.sum(samples, axis=0)
    probabilities = samples / sum_samples

    return samples, probabilities


def calculate_p_value_matrix(cwt_with_signal, samples, probabilities):

    probabilities_copy = np.copy(probabilities)

    keys = np.argwhere(cwt_with_signal > samples).T
    probabilities_copy[keys[0], keys[1], keys[2]] = 0
    p_values = np.sum(probabilities_copy, axis=0)

    ma_log_p_value = ma.log(p_values)

    return -1 * ma_log_p_value.filled(ma.min(ma_log_p_value))


def p_value_transformation_local(cwt_signal):
    new_shape = [49, 100]
    samples = []

    for i in range(500):
        cwt_record = generate_sample_fluctuations(signal_id=0, bg_id=0, wavelet_id=0)
        # samples.append(rebin(cwt_record, new_shape))
        samples.append(cwt_record)

    samples = np.array(samples)
    sum_samples = np.sum(samples, axis=0)
    probabilities = samples / sum_samples

    keys = np.argwhere(cwt_signal > samples).T
    probabilities[keys[0], keys[1], keys[2]] = 0
    p_values = np.sum(probabilities, axis=0)

    ma_log_p_value = ma.log(p_values)

    return -1 * ma_log_p_value.filled(ma.min(ma_log_p_value))


def main():
    pass
    # x = generate_sample_clean(signal_id=0, bg_id=0, wavelet_id=0)
    # print(p_value_transformation_local(x))


if __name__ == '__main__':
    main()

import numpy as np
import numpy.ma as ma

from src.default_background import DefaultBackground
from src.default_signal import DefaultSignal
from src.default_cwt_clean import DefaultCWTClean
from src.default_fluctuations import psi_fluctuations
from src.default_clean import psi_clean

RANGE_RESOLUTION = 500

""" p-values """


def get_bin_p_value(wt_value, bin_wt_range, bin_p_value_grid):
    if wt_value <= bin_wt_range[0]:
        return 1

    if wt_value >= bin_wt_range[-1]:
        return 0

    index = np.argmax(bin_wt_range > wt_value) - 1

    if index < 0:
        return 1

    return bin_p_value_grid[index]


def get_bin_wt_range(bin_wt_values, range_resolution):
    bin_wt_range = {}

    sorted_bin_wt_values = np.sort(bin_wt_values)
    bin_wt_range['min'] = sorted_bin_wt_values[0]
    bin_wt_range['max'] = sorted_bin_wt_values[-1]
    bin_wt_range['range'] = np.linspace(bin_wt_range['min'], bin_wt_range['max'], range_resolution)

    return bin_wt_range['range']


def build_samples_p_value_grid(samples, range_resolution=RANGE_RESOLUTION):
    range_resolution = 100

    grid_shape = (samples.shape[1], samples.shape[2], range_resolution)
    samples_wt_ranges = np.zeros(grid_shape)
    samples_p_value_grid = np.zeros(grid_shape)

    for i in range(samples_wt_ranges.shape[0]):
        for j in range(samples_wt_ranges.shape[1]):

            print("create_samples_p_value_grids ", i, j)

            bin_wt_values = samples[:, i, j]
            samples_wt_ranges[i, j] = get_bin_wt_range(bin_wt_values, range_resolution)

            for bin_wt_value in bin_wt_values:
                range_index = len(samples_wt_ranges[i, j]) - 1

                while bin_wt_value < samples_wt_ranges[i, j][range_index] and range_index > 0:
                    samples_p_value_grid[i, j, range_index] += 1
                    range_index -= 1

            samples_p_value_grid[i, j] = samples_p_value_grid[i, j] / len(bin_wt_values)
            samples_p_value_grid[i, j] = 1 - samples_p_value_grid[i, j]

    return samples_wt_ranges, samples_p_value_grid


def convert_wt_to_p_value(wt_record, samples_wt_ranges, samples_p_value_grid):
    p_value_record = np.zeros(wt_record.shape)

    for i in range(wt_record.shape[0]):
        for j in range(wt_record.shape[1]):
            wt_value = wt_record[i, j]
            bin_wt_range = samples_wt_ranges[i, j, :]
            bin_p_value_grid = samples_p_value_grid[i, j, :]

            p_value_record[i, j] = get_bin_p_value(wt_value, bin_wt_range, bin_p_value_grid)

    return p_value_record


def convert_record_log_p_value(record_p_values, samples_num):
    ma_log_p_value = ma.log(record_p_values)

    return -1 * ma_log_p_value.filled(np.log(1/samples_num))


""" samples """


def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)


def generate_rebined_sample_fluctuations(rebined_shape, signal_id=0, bg_id=0, wavelet_id=0):

    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    rebined_amp = rebin(amp, rebined_shape)

    return rebined_amp


def build_samples(samples_num, rebined_shape, signal_id=0, bg_id=0, wavelet_id=0):

    samples = []

    for i in range(samples_num):
        samples.append(generate_rebined_sample_fluctuations(rebined_shape,
                                                            signal_id,
                                                            bg_id,
                                                            wavelet_id))
    samples = np.array(samples)

    return samples


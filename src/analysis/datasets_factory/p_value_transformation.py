"""
create p_value distribution for a background

working with session: "test_dataset_2"

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


def build_samples(samples_num, rebined_shape, signal_id=0, bg_id=0, wavelet_id=0):

    samples = []

    for i in range(samples_num):
        samples.append(generate_rebined_sample_fluctuations(rebined_shape,
                                                            signal_id,
                                                            bg_id,
                                                            wavelet_id))
    samples = np.array(samples)
    # sum_samples = np.sum(samples, axis=0)
    # probabilities = samples / sum_samples

    return samples


def calculate_p_value_matrix(cwt_with_signal, samples_num, samples):
    keys = np.argwhere(cwt_with_signal < samples)
    pvalue_table = np.zeros(cwt_with_signal.shape)

    print(pvalue_table.shape)

    for key in keys:
        try:
            pvalue_table[key[1], key[2]] = pvalue_table[key[1], key[2]] + 1
        except:
            print("err!")

    p_values = pvalue_table / samples_num
    ma_log_p_value = ma.log(p_values)

    return -1 * ma_log_p_value.filled(np.log(1/samples_num))

#################################################################################################


def get_bin_p_value(wt_value, bin_wt_range, bin_p_value_grid):
    if wt_value <= bin_wt_range[0]:
        return 1

    if wt_value >= bin_wt_range[-1]:
        return 0

    index = np.argmax(bin_wt_range > wt_value) - 1

    if index < 0:
        return 1

    return bin_p_value_grid[index]


def convert_wt_to_p_value(wt_record, samples_wt_ranges, samples_p_value_grid):
    p_value_record = np.zeros(wt_record.shape)

    for i in range(wt_record.shape[0]):
        for j in range(wt_record.shape[1]):
            wt_value = wt_record[i, j]
            bin_wt_range = samples_wt_ranges[i, j, :]
            bin_p_value_grid = samples_p_value_grid[i, j, :]

            p_value_record[i, j] = get_bin_p_value(wt_value, bin_wt_range, bin_p_value_grid)

    return p_value_record


def build_p_values_grids(samples, path_p_value_grid, path_wt_ranges):
    samples_p_value_grid, samples_wt_ranges = create_samples_p_value_grids(samples)

    np.save(samples_p_value_grid, path_p_value_grid)
    np.save(samples_wt_ranges, path_wt_ranges)

    return samples_p_value_grid, samples_wt_ranges


def create_samples_p_value_grids(samples):
    range_resolution = 100

    grid_shape = (samples.shape[1], samples.shape[2], range_resolution)
    samples_p_value_grid = np.zeros(grid_shape)
    samples_wt_ranges = np.zeros(grid_shape)

    for i in range(samples_wt_ranges.shape[0]):
        for j in range(samples_wt_ranges.shape[1]):
            print("create_samples_p_value_grids ", i, j)
            bin_wt_values = samples[:, i, j]
            bin_wt_range = get_bin_wt_range(bin_wt_values, range_resolution)
            samples_wt_ranges[i, j] = bin_wt_range['range']

            for bin_wt_value in bin_wt_values:
                range_index = len(samples_wt_ranges[i, j]) - 1

                while bin_wt_value < samples_wt_ranges[i, j][range_index] and range_index > 0:
                    samples_p_value_grid[i, j, range_index] += 1
                    range_index -= 1

            samples_p_value_grid[i, j] = samples_p_value_grid[i, j] / len(bin_wt_values)

    return samples_p_value_grid, samples_wt_ranges


def build_p_values_grids_bin(samples, cell):
    samples_wt_ranges, samples_p_value_grid = create_samples_p_value_grids_bin(samples, cell)

    return samples_wt_ranges, samples_p_value_grid


def create_samples_p_value_grids_bin(samples, cell):
    range_resolution = 100

    grid_shape = (samples.shape[1], samples.shape[2], range_resolution)
    samples_p_value_grid = np.zeros(grid_shape)
    samples_wt_ranges = np.zeros(grid_shape)

    i = cell[0]
    j = cell[1]

    print("create_samples_p_value_grids ", i, j)
    bin_wt_values = samples[:, i, j]
    bin_wt_range = get_bin_wt_range(bin_wt_values, range_resolution)
    samples_wt_ranges[i, j] = bin_wt_range['range']

    print(samples_wt_ranges[i, j][0], samples_wt_ranges[i, j][-1])

    for bin_wt_value in bin_wt_values:
        range_index = len(samples_wt_ranges[i, j]) - 1

        while bin_wt_value < samples_wt_ranges[i, j][range_index] and range_index > 0:
            samples_p_value_grid[i, j, range_index] += 1
            range_index -= 1

    samples_p_value_grid[i, j] = samples_p_value_grid[i, j] / len(bin_wt_values)
    samples_p_value_grid[i, j] = 1 - samples_p_value_grid[i, j]

    return samples_wt_ranges, samples_p_value_grid


def get_bin_wt_range(bin_wt_values, range_resolution):
    bin_wt_range = {}

    sorted_bin_wt_values = np.sort(bin_wt_values)
    bin_wt_range['min'] = sorted_bin_wt_values[0]
    bin_wt_range['max'] = sorted_bin_wt_values[-1]
    bin_wt_range['range'] = np.linspace(bin_wt_range['min'], bin_wt_range['max'], range_resolution)

    return bin_wt_range

#################################################################################################


def p_value_transformation_local(cwt_signal):
    print(cwt_signal.shape)
    new_shape = [49, 100]
    samples = []

    for i in range(500):
        cwt_record = generate_sample_fluctuations(signal_id=0, bg_id=0, wavelet_id=0)
        # samples.append(rebin(cwt_record, new_shape))
        samples.append(cwt_record)

    samples = np.array(samples)
    keys = np.argwhere(cwt_signal < samples)
    pvalue_table = np.zeros((49, 500))

    print(pvalue_table.shape)

    for key in keys:
        try:
            pvalue_table[key[1], key[2]] = pvalue_table[key[1], key[2]] + 1
        except:
            print("err")

    p_values = pvalue_table / 500
    ma_log_p_value = ma.log(p_values)

    # return -1 * ma_log_p_value.filled(ma.min(ma_log_p_value))
    return -1 * ma_log_p_value.filled(np.log(1/500))


def main():
    pass
    # x = generate_sample_clean(signal_id=0, bg_id=0, wavelet_id=0)
    # print(p_value_transformation_local(x))


if __name__ == '__main__':
    main()

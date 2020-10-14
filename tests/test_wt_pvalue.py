import os
import matplotlib.pyplot as plt
from src.analysis.datasets_factory.p_value_transformation import *

BASEDIR = 'data/test'
PATH_SAMPLES = BASEDIR + '/samples.npy'

PATH_SAMPLES_WT_RANGES = BASEDIR + '/samples_p_values_grid.npy'
PATH_SAMPLES_P_VALUES_GRID = BASEDIR + '/samples_p_values_grid.npy'

SAMPLE_NUM = 5000
SHAPE = (49, 500)
REBINED_SHAPE = (49, 100)
CELL = (25, 50)


def generate_cwt_fluctuations(signal_id=0, bg_id=0, wavelet_id=0):
    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def generate_records(samples_num, samples, rebin_shape, signal_id=0, bg_id=0, wavelet_id=0):
    wts, p_values = [], []

    for i in range(4):
        cwt_bg_record = generate_cwt_fluctuations(signal_id, bg_id, wavelet_id)
        rebined_record = rebin(cwt_bg_record, rebin_shape)
        record = calculate_p_value_matrix(rebined_record, samples_num, samples)

        wts.append(rebined_record[CELL])
        p_values.append(np.exp(-1 * record[CELL]))

    return wts, p_values


def generate_wt_record(rebin_shape, signal_id=0, bg_id=0, wavelet_id=0):
        cwt_bg_record = generate_cwt_fluctuations(signal_id, bg_id, wavelet_id)
        rebined_record = rebin(cwt_bg_record, rebin_shape)

        return rebined_record


def plot_cell_histogram(cell, samples):
    x = samples[:, cell[0], cell[1]]
    print(x.shape)
    print(x)

    # the histogram of the data
    n, bins, patches = plt.hist(x, bins=150, facecolor='blue', alpha=0.7)

    print(bins.shape, n.shape)

    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()


def plot_pvalue_vs_wt(cell, samples, wts, p_values):
    x, count_wt = np.unique(samples[:, cell[0], cell[1]], return_counts=True)

    for i in range(len(count_wt) - 1):
        count_wt[i + 1] = count_wt[i + 1] + count_wt[i]

    # set pvalue = 0 for the first?
    # y = np.zeros_like(x)

    samples_p_values = 1 - (count_wt/len(x))

    fig, ax = plt.subplots()

    ax.plot(x, samples_p_values)
    plt.plot(wts, p_values, marker='.', linestyle='None', markersize=15, color="red")

    ax.set(xlabel='wt', ylabel='p_value', title='p_value vs wt')
    ax.grid()

    plt.show()


def test_naive_alg_1(samples):
    # wts, p_values = generate_records(SAMPLE_NUM,
    #                                samples,
    #                                REBINED_SHAPE,
    #                                signal_id=0,
    #                                bg_id=0,
    #                                wavelet_id=0)

    wts = [0.9918104171719835, 0.58844301221563, 1.4867735469468484, 0.6014293914024106]
    p_values = [0.2978, 0.6648, 0.06640000000000001, 0.6524]

    print(wts)
    print(p_values)

    plot_cell_histogram(CELL, samples)
    plot_pvalue_vs_wt(CELL, samples, wts, p_values)


def test_improved_alg_1(samples):
    samples_wt_ranges, samples_p_value_grid = build_p_values_grids_bin(samples, CELL)

    wts = samples_wt_ranges[CELL[0], CELL[1]]
    p_values = samples_p_value_grid[CELL[0], CELL[1]]

    plot_pvalue_vs_wt(CELL, samples, wts, p_values)


def test_improved_alg_2(samples):
    samples_wt_ranges, samples_p_value_grid = build_p_values_grids_bin(samples, CELL)

    wts = samples_wt_ranges[CELL[0], CELL[1]]
    p_values = samples_p_value_grid[CELL[0], CELL[1]]
    plot_pvalue_vs_wt(CELL, samples, wts, p_values)

    x = []
    y = []

    for i in range(20):
        wt_record = generate_wt_record(REBINED_SHAPE, signal_id=0, bg_id=0, wavelet_id=0)
        record_p_values = convert_wt_to_p_value(wt_record, samples_wt_ranges, samples_p_value_grid)

        x.append(wt_record[CELL])
        y.append(record_p_values[CELL])

    plot_pvalue_vs_wt(CELL, samples, x, y)


def main():
    os.makedirs(BASEDIR, exist_ok=True)

    try:
        samples = np.load(PATH_SAMPLES)
    except:
        samples = build_samples(SAMPLE_NUM, REBINED_SHAPE)
        np.save(PATH_SAMPLES, samples)

    # conceptual test
    # test_naive_alg_1(samples)

    # test that the grid is valid
    # test_improved_alg_1(samples)

    # test conversion of cwt to p_value
    test_improved_alg_2(samples)


if __name__ == '__main__':
    main()

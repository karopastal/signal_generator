import os
import numpy as np
import matplotlib.pyplot as plt

from src.datasets.utils import convert_record_log_p_value,\
                               generate_rebined_sample_fluctuations, \
                               convert_wt_to_p_value

BASEDIR = 'data/test/Oct-14-20T13-44-04$15000'
PATH_SAMPLES = BASEDIR + '/samples.npy'
PATH_SAMPLES_WT_RANGES = BASEDIR + '/samples_wt_ranges.npy'
PATH_SAMPLES_P_VALUES_GRID = BASEDIR + '/samples_p_value_grid.npy'

SAMPLE_NUM = 5000
SHAPE = (48, 500)
REBINED_SHAPE = (48, 100)
CELL = (26, 25)


def plot_wt_histogram(cell, samples):
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

    samples_p_values = 1 - (count_wt/len(x))

    fig, ax = plt.subplots()

    ax.plot(x, samples_p_values)
    plt.plot(wts, p_values, marker='.', linestyle='None', markersize=15, color="red")

    ax.set(xlabel='wt', ylabel='p_value', title='p_value vs wt')
    ax.grid()

    plt.show()


def plot_record(record):
    fig, ax = plt.subplots(figsize=(12, 12))

    img = ax.imshow(record,
                    extent=(0, SHAPE[1], SHAPE[0], 0),
                    interpolation='nearest',
                    aspect='auto',
                    cmap='pink')

    ax.set_ylim(0, SHAPE[0])
    fig.colorbar(img, ax=ax)

    plt.title('CWT w/ noise - scales range: (%s, %s)' % (0, SHAPE[0]))
    plt.ylabel('Scales')
    plt.xlabel('Translation')
    plt.show()


def test_record(samples_num, samples_wt_ranges, samples_p_value_grid):
    wt_record = generate_rebined_sample_fluctuations(REBINED_SHAPE,
                                                     signal_id=0,
                                                     bg_id=0,
                                                     wavelet_id=0)
    print(1, wt_record.shape)
    record_p_values = convert_wt_to_p_value(wt_record,
                                            samples_wt_ranges,
                                            samples_p_value_grid)
    print(2, record_p_values.shape)

    record_log_p_values = convert_record_log_p_value(record_p_values, samples_num)

    print(3, record_log_p_values.shape)

    plot_record(record_log_p_values)


def test_wt_to_pvalue(samples, samples_wt_ranges, samples_p_value_grid):
    plot_wt_histogram(CELL, samples)

    wts = []
    p_values = []

    for i in range(20):
        wt_record = generate_rebined_sample_fluctuations(REBINED_SHAPE,
                                                         signal_id=0,
                                                         bg_id=0,
                                                         wavelet_id=0)

        record_p_values = convert_wt_to_p_value(wt_record,
                                                samples_wt_ranges,
                                                samples_p_value_grid)

        wts.append(wt_record[CELL])
        p_values.append(record_p_values[CELL])

    plot_pvalue_vs_wt(CELL, samples, wts, p_values)


def main():
    os.makedirs(BASEDIR, exist_ok=True)

    samples = np.load(PATH_SAMPLES)
    samples_wt_ranges = np.load(PATH_SAMPLES_WT_RANGES)
    samples_p_value_grid = np.load(PATH_SAMPLES_P_VALUES_GRID)

    print(samples.shape, samples_wt_ranges.shape, samples_p_value_grid.shape)

    # test_wt_to_pvalue(samples, samples_wt_ranges, samples_p_value_grid)
    # test_record(len(samples), samples_wt_ranges, samples_p_value_grid)
    # todo: test_selected_items_from_dataset()


if __name__ == '__main__':
    main()

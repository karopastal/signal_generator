"""
-----------
dataset_v1_1 :
-----------
    ! rebining after transformation, not before.....
    0. session: test_dataset_2
    1. resolution: (49, 500)
    2. rebined resolution: (49, 100)
    3. p_value_transforamtion
"""

import os
from datetime import datetime, date
from src.analysis.datasets_factory.p_value_transformation import *
import matplotlib.pyplot as plt

# import numpy as np
# from src.default_clean import psi_clean

from src.default_background import DefaultBackground
from src.default_signal import DefaultSignal
from src.default_cwt_clean import DefaultCWTClean
from src.default_fluctuations import psi_fluctuations

SIGNALS_NUM = 2
SAMPLE_NUM = 500
TRAIN_SIZE = 100
TEST_SIGNALS_SIZE = 100
TEST_BACKGROUND_SIZE = 100

today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

NAME = 'dataset_v1_1'

DATA_BASEDIR = "data/" + NAME + "/%sT%s$%s" % (current_day,
                                               current_time,
                                               int(TRAIN_SIZE))

PATH_TO_SAMPLES = DATA_BASEDIR + '/p_value_samples'
PATH_TO_PROBABILITIES = DATA_BASEDIR + '/probabilities'
PATH_TRAIN = DATA_BASEDIR + '/train_backgrounds'
PATH_TEST_SIGNALS = DATA_BASEDIR + '/test_signals'
PATH_TEST_BACKGROUNDS = DATA_BASEDIR + '/test_backgrounds'

ORIGINAL_SHAPE = [49, 500]
REBINED_SHAPE = [49, 100]


def peek(record):
    fig, ax = plt.subplots(figsize=(12, 12))

    ax.imshow(record, interpolation='nearest', aspect='auto', cmap='pink')

    plt.ylabel('Scales')
    plt.xlabel('Translation')
    plt.show()


def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)


def generate_cwt_fluctuations(signal_id=0, bg_id=0, wavelet_id=0):
    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def generate_record(samples, probabilities, rebin_shape, signal_id=0, bg_id=0, wavelet_id=0):
    cwt_bg_record = generate_cwt_fluctuations(signal_id, bg_id, wavelet_id)
    record = calculate_p_value_matrix(cwt_bg_record, samples, probabilities)
    rebined_record = rebin(record, rebin_shape)

    return rebined_record


def create_train_dataset(samples, probabilities):
    arrays = []

    for i in range(TRAIN_SIZE):
        record = generate_record(samples, probabilities, REBINED_SHAPE, signal_id=0, bg_id=0, wavelet_id=0)
        arrays.append(record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    np.save(PATH_TRAIN, dataset)


def create_test_backgrounds_dataset(samples, probabilities):
    arrays = []

    for i in range(TEST_BACKGROUND_SIZE):
        record = generate_record(samples, probabilities, REBINED_SHAPE, signal_id=0, bg_id=0, wavelet_id=0)
        arrays.append(record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    np.save(PATH_TEST_BACKGROUNDS, dataset)


def create_test_signals_datasets(samples, probabilities):

    for signal_id in range(1, SIGNALS_NUM + 1):
        arrays = []

        for i in range(TEST_SIGNALS_SIZE):
            record = generate_record(samples, probabilities, REBINED_SHAPE, signal_id=signal_id, bg_id=0, wavelet_id=0)
            arrays.append(record)

        dataset = np.stack(arrays, axis=0)
        print(dataset.shape)
        np.save(PATH_TEST_SIGNALS + "_" + str(signal_id), dataset)


def build_samples_and_probabilities_local():
    print("samples, probabilities -> size: ", SAMPLE_NUM)
    samples, probabilities = build_samples_and_probabilities(samples_num=SAMPLE_NUM,
                                                             rebined_shape=REBINED_SHAPE,
                                                             signal_id=0,
                                                             bg_id=0,
                                                             wavelet_id=0)

    np.save(PATH_TO_SAMPLES, samples)
    np.save(PATH_TO_PROBABILITIES, probabilities)


def build():
    print("samples, probabilities -> size: ", SAMPLE_NUM)
    samples, probabilities = build_samples_and_probabilities(samples_num=SAMPLE_NUM,
                                                             rebined_shape=REBINED_SHAPE,
                                                             signal_id=0,
                                                             bg_id=0,
                                                             wavelet_id=0)

    np.save(PATH_TO_SAMPLES, samples)
    np.save(PATH_TO_PROBABILITIES, probabilities)

    print("train_dataset -> size: ", TRAIN_SIZE)
    create_train_dataset(samples, probabilities)

    print("test_bgs_dataset -> size: ", TEST_BACKGROUND_SIZE)
    create_test_backgrounds_dataset(samples, probabilities)

    print("test_signals_dataset -> size: ", TEST_SIGNALS_SIZE)
    create_test_signals_datasets(samples, probabilities)


def main():
    pass
    os.makedirs(DATA_BASEDIR, exist_ok=True)
    build()


if __name__ == '__main__':
    main()

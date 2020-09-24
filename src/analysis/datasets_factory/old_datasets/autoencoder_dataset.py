"""
working with the session: autoencoder_toy_dataset
"""

import os

from datetime import datetime, date
from src.analysis.datasets_factory.p_value_transformation import *

k = 1000
today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

SAMPLE_NUM = 1000
TRAIN_SIZE = 5000
TEST_SIGNALS_SIZE = 1000
TEST_BACKGROUND_SIZE = 2000

BASEDIR = "data/autoencoder/%sT%s$%sk-%sk-%sk-%sk" % (current_day,
                                                      current_time,
                                                      int(SAMPLE_NUM / k),
                                                      int(TRAIN_SIZE / k),
                                                      int(TEST_SIGNALS_SIZE / k),
                                                      int(TEST_BACKGROUND_SIZE / k))

PATH_TO_SAMPLES = BASEDIR + '/p_value_samples'
PATH_TO_PROBABILITIES = BASEDIR + '/probabilities'

PATH_AUTOENCODER_TRAIN = BASEDIR + '/train'
PATH_AUTOENCODER_TEST_SIGNALS = BASEDIR + '/test_signals'
PATH_AUTOENCODER_TEST_BACKGROUNDS = BASEDIR + '/test_backgrounds'


def generate_test_signals_dataset(samples, probabilities):

    arrays = []

    for i in range(TEST_BACKGROUND_SIZE):
        cwt_signal = generate_sample_fluctuations(signal_id=0, bg_id=1, wavelet_id=0)
        record = calculate_p_value_matrix(cwt_signal, samples, probabilities)
        arrays.append(record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)
    np.save(PATH_AUTOENCODER_TEST_BACKGROUNDS, dataset)


def generate_test_backgrounds_dataset(samples, probabilities):
    arrays = []

    for i in range(TEST_SIGNALS_SIZE):
        cwt_signal = generate_sample_fluctuations(signal_id=1, bg_id=1, wavelet_id=0)
        record = calculate_p_value_matrix(cwt_signal, samples, probabilities)
        arrays.append(record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    np.save(PATH_AUTOENCODER_TEST_SIGNALS, dataset)


def generate_train_dataset(samples, probabilities):

    arrays = []

    for i in range(TRAIN_SIZE):
        cwt_signal = generate_sample_fluctuations(signal_id=0, bg_id=1, wavelet_id=0)
        record = calculate_p_value_matrix(cwt_signal, samples, probabilities)
        arrays.append(record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    np.save(PATH_AUTOENCODER_TRAIN, dataset)


def build():

    print("building samples and probabilities")
    samples, probabilities = build_samples_and_probabilities(samples_num=SAMPLE_NUM,
                                                             signal_id=0,
                                                             bg_id=1,
                                                             wavelet_id=0)
    np.save(PATH_TO_SAMPLES, samples)
    np.save(PATH_TO_PROBABILITIES, probabilities)

    print("generating train dataset")
    generate_train_dataset(samples, probabilities)

    print("generating test backgrounds dataset")
    generate_test_backgrounds_dataset(samples, probabilities)

    print("generating test signals dataset")
    generate_test_signals_dataset(samples, probabilities)


def main():
    os.makedirs(BASEDIR, exist_ok=True)
    build()


if __name__ == '__main__':
    main()

"""

working with the session: autoencoder_toy_dataset

"""

import numpy as np

from src.analysis.datasets_factory.p_value_transformation import *

PATH_TO_SAMPLES = 'data/autoencoder_p_value_samples'
PATH_TO_PROBABILITIES = 'data/autoencoder_probabilities'

PATH_AUTOENCODER_TRAIN = 'data/autoencoder_train'
PATH_AUTOENCODER_TEST_SIGNALS = 'data/autoencoder_test_signals'
PATH_AUTOENCODER_TEST_BACKGROUNDS = 'data/autoencoder_test_backgrounds'

TRAIN_SIZE = 10000
TEST_SIGNALS_SIZE = 2000
TEST_BACKGROUND_SIZE = 8000


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
    samples, probabilities = build_samples_and_probabilities(samples_num=20000,
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
    build()


if __name__ == '__main__':
    main()

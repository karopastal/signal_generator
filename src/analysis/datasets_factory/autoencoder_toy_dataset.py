""" Autoencoder Toy Dataset:

1. Train dataset with backgrounds only
2. Test dataset with other backgrounds only (expected low loss upon reconstruction)
3. Test dataset with backgrounds and signals (expected high loss upon reconstruction for anomaly detection)
4. Generate a threshold from (2.) loss mean plus a safety margin.

"""

import json
import numpy as np

from src.default_signal import DefaultSignal
from src.default_background import DefaultBackground
from src.default_fluctuations import psi_fluctuations
from src.default_cwt_fluctuations import DefaultCWTFluctuations

PATH_SIGNALS = 'src/signals/default_signal.json'
PATH_BACKGROUNDS = 'src/backgrounds/default_background.json'
PATH_WAVELETS = 'src/wavelets/default_wavelet.json'

PATH_AUTOENCODER_TOY_TRAIN_DATASET = 'data/autoencoder_toy_train_dataset'
PATH_AUTOENCODER_TOY_TEST_SIGNALS_DATASET = 'data/autoencoder_toy_test_signals_dataset'
PATH_AUTOENCODER_TOY_TEST_BACKGROUNDS_DATASET = 'data/autoencoder_toy_backgrounds_test_dataset'

DATASET_SIZE = 1000


def to_json(path):
    with open(path) as f:
        data = json.load(f)

    return data


def all_signals():
    return to_json(PATH_SIGNALS)


def all_backgrounds():
    return to_json(PATH_BACKGROUNDS)


def all_wavelets():
    return to_json(PATH_WAVELETS)


def generate_autoencoder_toy_train_dataset():
    print("generating autoencoder_toy_dataset...")

    background_config = all_backgrounds()
    signal_config = all_signals()
    wavelet_config = all_wavelets()

    arrays = []

    dbg = DefaultBackground(background_config[0]['id'])
    ds = DefaultSignal(signal_config[3]['id'])  # no signal
    cmor = DefaultCWTFluctuations(wavelet_config[0]['id'])

    for j in range(DATASET_SIZE):
        data = psi_fluctuations(ds, dbg)
        [coeffs, freqs] = cmor.generate_coefficients(data)
        amp = np.abs(coeffs)
        arrays.append(amp)

        train_dataset = np.stack(arrays, axis=0)
        np.save(PATH_AUTOENCODER_TOY_TRAIN_DATASET, train_dataset)


def generate_autoencoder_toy_test_backgrounds_dataset():
    print("generate_autoencoder_toy_test_backgrounds_dataset...")

    background_config = all_backgrounds()
    signal_config = all_signals()
    wavelet_config = all_wavelets()

    arrays = []

    dbg = DefaultBackground(background_config[0]['id'])
    ds = DefaultSignal(signal_config[3]['id'])  # no signal
    cmor = DefaultCWTFluctuations(wavelet_config[0]['id'])

    for j in range(DATASET_SIZE):
        data = psi_fluctuations(ds, dbg)

        [coeffs, freqs] = cmor.generate_coefficients(data)

        amp = np.abs(coeffs)
        arrays.append(amp)

        test_backgrounds_dataset = np.stack(arrays, axis=0)
        np.save(PATH_AUTOENCODER_TOY_TEST_BACKGROUNDS_DATASET, test_backgrounds_dataset)


def generate_autoencoder_toy_test_signals_dataset():
    print("generate_autoencoder_toy_test_signals_dataset...")

    background_config = all_backgrounds()
    signal_config = all_signals()
    wavelet_config = all_wavelets()

    arrays = []

    dbg = DefaultBackground(background_config[0]['id'])
    cmor = DefaultCWTFluctuations(wavelet_config[0]['id'])

    ds_ids = [0, 1, 2]
    ds_prob = [0.33, 0.33, 0.34]
    ds_random_ids = np.random.choice(ds_ids, DATASET_SIZE, ds_prob)

    for ds_id in ds_random_ids:
        ds = DefaultSignal(signal_config[ds_id]['id'])
        data = psi_fluctuations(ds, dbg)

        [coeffs, freqs] = cmor.generate_coefficients(data)

        amp = np.abs(coeffs)
        arrays.append(amp)

    test_signals_dataset = np.stack(arrays, axis=0)
    np.save(PATH_AUTOENCODER_TOY_TEST_SIGNALS_DATASET, test_signals_dataset)


def main():
    generate_autoencoder_toy_train_dataset()
    generate_autoencoder_toy_test_backgrounds_dataset()
    generate_autoencoder_toy_test_signals_dataset()


if __name__ == '__main__':
    main()

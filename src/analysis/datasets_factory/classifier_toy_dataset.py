import json
import numpy as np

from src.default_signal import DefaultSignal
from src.default_background import DefaultBackground
from src.default_fluctuations import psi_fluctuations
from src.default_cwt_fluctuations_p_value import DefaultCWTFluctuations

PATH_SIGNALS = 'src/signals/default_signal.json'
PATH_BACKGROUNDS = 'src/backgrounds/default_background.json'
PATH_WAVELETS = 'src/wavelets/default_wavelet.json'

PATH_CLASSIFIER_TOY_DATASET = 'data/classifier_toy_dataset'
PATH_CLASSIFIER_TOY_LABELS = 'data/classifier_toy_labels'

"""
Tuning: 
    1. data: what is the intrinsic signal:background ratio?
    2. data: what backgrounds (regardless of the fluctuations) are a good choice to bundle the signals into?
    3. data: log scale for the scalogram?
    4. wavelets: how to take into account the 'a' factor that contributes to the scales?
    5. data: dimensions for compact toy dataset (light version)
    6. data: criteria for normalization (coefficients preprocessing)
    7. data: consider toy data-set of three types: 1 frequency, 2 frequencies and 3 frequencies.
    8. feature: add "make current-session"
    9. refactor: configure BIN_SEGMENT outside of the fluctuation module
    10. test: write test that validates that all the data is different from each other.
    11. visulalization: add visualization to the datasets 
"""


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


def randomize(x, y):
    s = np.arange(y.shape[0])
    np.random.shuffle(s)

    return x[s], y[s]


def generate_classifier_toy_dataset():
    signals = all_signals()
    background_config = all_backgrounds()[0]
    wavelet_config = all_wavelets()[0]

    arrays = []
    ids = []

    for signl_config in signals:
        ds = DefaultSignal(signl_config['id'])
        dbg = DefaultBackground(background_config['id'])
        cmor = DefaultCWTFluctuations(wavelet_config['id'])

        for j in range(2000):
            data = psi_fluctuations(ds, dbg)
            [coeffs, freqs] = cmor.generate_coefficients(data)
            amp = np.abs(coeffs)
            arrays.append(amp)
            ids.append(signl_config['id'])

    x = np.stack(arrays, axis=0)
    y = np.array(ids)

    toy_data_set, labels = randomize(x, y)

    np.save(PATH_CLASSIFIER_TOY_DATASET, toy_data_set)
    np.save(PATH_CLASSIFIER_TOY_LABELS, labels)

    print('generated classifier_toy_dataset successfully ', toy_data_set.shape)


def main():
    generate_classifier_toy_dataset()


if __name__ == '__main__':
    main()

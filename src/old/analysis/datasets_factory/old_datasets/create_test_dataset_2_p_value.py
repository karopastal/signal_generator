"""
signal 5 picks & 1 pick.
"""

import os

from datetime import datetime, date
from src.old.analysis.datasets_factory.p_value_transformation import *

from src.default_background import DefaultBackground
from src.default_signal import DefaultSignal
from src.default_cwt_clean import DefaultCWTClean
from src.default_fluctuations import psi_fluctuations

#######################
# test_dataset_2 ###
#######################

today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

TRAIN_SIZE = 5000
TEST_SIGNALS_SIZE = 1000
TEST_BACKGROUND_SIZE = 2500

SESSION = 'test_dataset_2_p_value'

DATA_BASEDIR = "data/" + SESSION + "/%sT%s$%s" % (current_day,
                                                  current_time,
                                                  int(TRAIN_SIZE))

PATH_TRAIN = DATA_BASEDIR + '/train_backgrounds'
PATH_TEST_SIGNALS = DATA_BASEDIR + '/test_signals'
PATH_TEST_BACKGROUNDS = DATA_BASEDIR + '/test_backgrounds'


SIGNALS_NUM = 5


def rebinning():
    return 0


def generate_cwt_fluctuations(signal_id=0, bg_id=0, wavelet_id=0):
    ds = DefaultSignal(signal_id)
    dbg = DefaultBackground(bg_id)
    cmor = DefaultCWTClean(wavelet_id)

    data = psi_fluctuations(ds, dbg)

    [coeffs, freqs] = cmor.generate_coefficients(data)
    amp = np.abs(coeffs)

    return amp


def create_train_dataset():
    arrays = []

    for i in range(TRAIN_SIZE):
        cwt_bg_record = generate_cwt_fluctuations(signal_id=0, bg_id=0, wavelet_id=0)
        rebinned_cwt_bg_record = rebinning(cwt_bg_record)
        arrays.append(rebinned_cwt_bg_record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    np.save(PATH_TRAIN, dataset)


def create_test_backgrounds_dataset():
    arrays = []

    for i in range(TEST_BACKGROUND_SIZE):
        cwt_bg_record = generate_cwt_fluctuations(signal_id=0, bg_id=0, wavelet_id=0)
        arrays.append(cwt_bg_record)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    np.save(PATH_TEST_BACKGROUNDS, dataset)


def create_test_signals_datasets():
    arrays = []

    for signal_id in range(1, SIGNALS_NUM + 1):
        for i in range(TEST_SIGNALS_SIZE):
            cwt_signal_record = generate_cwt_fluctuations(signal_id=signal_id,
                                                          bg_id=0,
                                                          wavelet_id=0)

            arrays.append(cwt_signal_record)

        dataset = np.stack(arrays, axis=0)
        print(dataset.shape)
        np.save(PATH_TEST_SIGNALS + "_" + str(signal_id), dataset)


def build():
    create_train_dataset()
    create_test_backgrounds_dataset()
    create_test_signals_datasets()


def main():
    os.makedirs(DATA_BASEDIR, exist_ok=True)
    # build()


if __name__ == '__main__':
    main()

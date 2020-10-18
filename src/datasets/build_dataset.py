import os
import logging
import numpy as np
import json

from datetime import datetime, date

from src.datasets.utils import build_samples, \
    build_samples_p_value_grid, \
    convert_wt_to_p_value, \
    convert_record_log_p_value, \
    generate_rebined_sample_fluctuations

SAMPLE_NUM = 10000
RANGE_RESOLUTION = 1000

TRAIN_SIZE = 25000
TEST_BACKGROUND_SIZE = 5000

SIGNALS_NUM = 5
TEST_SIGNALS_SIZE = 1000

ORIGINAL_SHAPE = [48, 512]
REBINED_SHAPE = [48, 64]

today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

NAME = 'dataset'

BASEDIR = "data/" + NAME + "/%sT%s$%s" % (current_day,
                                          current_time,
                                          int(TRAIN_SIZE))

PATH_LOG = BASEDIR + '/progress.log'

PATH_SAMPLES = BASEDIR + '/samples.npy'
PATH_TO_SAMPLES_WT_RANGES = BASEDIR + '/samples_wt_ranges.npy'
PATH_TO_SAMPLES_P_VALUE_GRID = BASEDIR + '/samples_p_value_grid.npy'

PATH_TRAIN = BASEDIR + '/train_backgrounds.npy'
PATH_TEST_BACKGROUNDS = BASEDIR + '/test_backgrounds.npy'
PATH_TEST_SIGNALS = BASEDIR + '/test_signals'

PATH_DATASET_CONFIG = BASEDIR + '/dataset_config.json'


def save_dataset_config(dataset_config={}):
    dataset_config['SAMPLE_NUM'] = SAMPLE_NUM
    dataset_config['RANGE_RESOLUTION'] = RANGE_RESOLUTION
    dataset_config['TRAIN_SIZE'] = TRAIN_SIZE
    dataset_config['TEST_BACKGROUND_SIZE'] = TEST_BACKGROUND_SIZE
    dataset_config['SIGNALS_NUM'] = SIGNALS_NUM
    dataset_config['TEST_SIGNALS_SIZE'] = TEST_SIGNALS_SIZE
    dataset_config['ORIGINAL_SHAPE'] = ORIGINAL_SHAPE
    dataset_config['ORIGINAL_SHAPE'] = REBINED_SHAPE

    with open(PATH_DATASET_CONFIG, 'w') as outfile:
        json.dump(dataset_config, outfile, indent=4, sort_keys=False)


def generate_dataset(size, samples_wt_ranges, samples_p_value_grid, signal_id=0, bg_id=0, wavelet_id=0):
    arrays = []

    for i in range(size):
        wt_record = generate_rebined_sample_fluctuations(REBINED_SHAPE,
                                                         signal_id=signal_id,
                                                         bg_id=bg_id,
                                                         wavelet_id=wavelet_id)

        record_p_values = convert_wt_to_p_value(wt_record,
                                                samples_wt_ranges,
                                                samples_p_value_grid)

        record_log_p_values = convert_record_log_p_value(record_p_values,
                                                         SAMPLE_NUM)
        arrays.append(record_log_p_values)

    dataset = np.stack(arrays, axis=0)
    print(dataset.shape)

    return dataset


def create_train_dataset(samples_wt_ranges, samples_p_value_grid):
    train_dataset = generate_dataset(TRAIN_SIZE,
                                     samples_wt_ranges,
                                     samples_p_value_grid)

    np.save(PATH_TRAIN, train_dataset)


def create_test_bgs_dataset(samples_wt_ranges, samples_p_value_grid):
    test_bgs_dataset = generate_dataset(TEST_BACKGROUND_SIZE,
                                        samples_wt_ranges,
                                        samples_p_value_grid)

    np.save(PATH_TEST_BACKGROUNDS, test_bgs_dataset)


def create_test_signals_datasets(samples_wt_ranges, samples_p_value_grid):

    for signal_id in range(1, SIGNALS_NUM + 1):

        test_signal_dataset = generate_dataset(TEST_SIGNALS_SIZE,
                                               samples_wt_ranges,
                                               samples_p_value_grid,
                                               signal_id=signal_id)

        np.save(PATH_TEST_SIGNALS + "_" + str(signal_id), test_signal_dataset)


def build():
    save_dataset_config({})
    logging.basicConfig(filename=PATH_LOG, level=logging.DEBUG)

    """ create samples """
    logging.info('time: %s | samples -> size: %s' % (now.strftime("%H-%M-%S"), SAMPLE_NUM))

    samples = build_samples(samples_num=SAMPLE_NUM,
                            rebined_shape=REBINED_SHAPE,
                            signal_id=0,
                            bg_id=0,
                            wavelet_id=0)

    np.save(PATH_SAMPLES, samples)

    """ create wt ranges and p_values grid """
    logging.info('time: %s | samples_wt_ranges, samples_p_value_grid' % (datetime.now().strftime("%H-%M-%S"), ))

    print(now.strftime("%H-%M-%S"), "samples_wt_ranges, samples_p_value_grid")

    samples_wt_ranges, samples_p_value_grid = build_samples_p_value_grid(samples, RANGE_RESOLUTION)

    np.save(PATH_TO_SAMPLES_WT_RANGES, samples_wt_ranges)
    np.save(PATH_TO_SAMPLES_P_VALUE_GRID, samples_p_value_grid)

    """ create backgrounds train dataset """

    logging.info('time: %s | train_dataset -> size: %s' % (datetime.now().strftime("%H-%M-%S"), TRAIN_SIZE))
    create_train_dataset(samples_wt_ranges, samples_p_value_grid)

    """ create backgrounds test dataset """
    logging.info('time: %s | test_bgs_dataset -> size: %s' % (datetime.now().strftime("%H-%M-%S"), TEST_BACKGROUND_SIZE))
    create_test_bgs_dataset(samples_wt_ranges, samples_p_value_grid)

    """ create signals test dataset """
    logging.info('time: %s | test_signal_dataset -> size: %s' % (datetime.now().strftime("%H-%M-%S"), TEST_SIGNALS_SIZE))
    create_test_signals_datasets(samples_wt_ranges, samples_p_value_grid)


def main():
    pass
    os.makedirs(BASEDIR, exist_ok=True)
    build()


if __name__ == '__main__':
    main()

import os
import json
import numpy as np

from datetime import datetime, date
from shutil import copy


def normalize(dataset, factor):
    return dataset / factor


def load_dataset(path_dataset):
    train_data = load_train_data(path_dataset)
    test_bgs_data = load_test_bgs_data(path_dataset)
    test_signal_data = load_test_signal_data(path_dataset)

    return train_data, test_bgs_data, test_signal_data


def load_train_data(path_dataset):
    path_train_data = path_dataset + '/train_backgrounds.npy'
    return np.load(path_train_data)


def load_test_bgs_data(path_dataset):
    path_test_bgs_data = path_dataset + '/test_backgrounds.npy'
    return np.load(path_test_bgs_data)


def load_test_signal_data(path_dataset, signal_id=1):
    path_test_signal_data = path_dataset + '/test_signals_' + signal_id + '.npy'
    return np.load(path_test_signal_data)


def get_ae_base_dir(name):
    today = date.today()
    now = datetime.now()
    current_day = today.strftime("%b-%d-%y")
    current_time = now.strftime("%H-%M-%S")

    base_dir = "data/models/" + name + "/%s_T_%s" % (current_day, current_time,)

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    return base_dir


def copy_dataset_config(path_dataset, dst):
    path_dataset_config = path_dataset + '/dataset_config.json'
    copy(path_dataset_config, dst)


def get_dataset_config(path_dataset):
    path_dataset_config = path_dataset + '/dataset_config.json'

    with open(path_dataset_config) as f:
        dataset_config = json.load(f)

    return dataset_config


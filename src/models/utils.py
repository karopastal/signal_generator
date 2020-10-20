import os
import json
import numpy as np
import tensorflow as tf

from shutil import copy
from datetime import datetime, date
from matplotlib import pyplot as plt


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
    path_test_signal_data = path_dataset + '/test_signals_' + str(signal_id) + '.npy'
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


def print_predictions_loss(losses):
    mse = tf.keras.losses.MeanSquaredError()
    loss_backgrounds = mse(losses['test_bgs_data'], losses['predict_bgs_test']).numpy()
    loss_signals = mse(losses['test_signal_data'], losses['predict_signal_test']).numpy()
    ratio = loss_signals / loss_backgrounds

    print("PREDICTIONS LOSS")
    print("--------------------------------------")
    print("loss backgrounds : ", loss_backgrounds)
    print("loss signals     : ", loss_signals)
    print("ratio: ", ratio)
    print("--------------------------------------")


def plot_progress(path_progress, title=''):
    progress = np.loadtxt(open(path_progress, "rb"), delimiter=",", skiprows=1)

    x = progress[:, 0]
    loss = progress[:, 1]
    val = progress[:, 2]

    plt.plot(x, loss)
    plt.plot(x, val)
    plt.title('%s model loss' % (title,))
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


def plot_prediction(autoencoder, x_test, shape):
    reconstructed = autoencoder.predict(x_test)

    n = 3  # how many digits we will display
    plt.figure(figsize=(20, 20))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape(shape), cmap='pink')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(reconstructed[i].reshape(shape), cmap='pink')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.show()


def loss_distribution(test_data, prediction_data):
    mse = tf.keras.losses.MSE

    return mse(test_data, prediction_data)


def model_efficiency_p_value(bg_losses, signal_losses):
    signal_median = np.median(signal_losses)
    count = 0

    for bg_loss in bg_losses:
        if bg_loss >= signal_median:
            count += 1

    p_value = count / len(bg_losses)

    return p_value


def plot_histogram(bgs, signal):
    # the histogram of the data
    p_value = model_efficiency_p_value(bgs, signal)

    plt.hist(bgs, bins=150, facecolor='red', alpha=0.5, label='background')
    plt.hist(signal, bins=150, facecolor='blue', alpha=0.5, label='background + signal')

    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('loss distribution, efficiency_p_value: %s' % (p_value, ))
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

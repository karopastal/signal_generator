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


def plot_progress(path_progress, title='', file_name=''):
    path = 'docs/output/' + file_name + '_model_loss.jpeg'

    progress = np.loadtxt(open(path_progress, "rb"), delimiter=",", skiprows=1)

    x = progress[:, 0]
    loss = progress[:, 1]
    val = progress[:, 2]

    fig, ax = plt.subplots(figsize=(9, 7))

    plt.plot(x, loss)
    plt.plot(x, val)
    plt.title('%s model loss' % (title,), fontsize=20)
    plt.ylabel('loss', fontsize=18)
    plt.xlabel('epoch', fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.legend(['train', 'validation'], loc='upper right', fontsize=18)
    plt.savefig(path)
    plt.close('all')


def plot_prediction(autoencoder, x_test, shape, title, file_name):
    reconstructed = autoencoder.predict(x_test)

    fig, ax = plt.subplots(figsize=(9, 7))

    img = ax.imshow(x_test[0].reshape(shape),
                    extent=(0, 64, 48, 0),
                    interpolation='sinc',
                    aspect='auto',
                    cmap='bwr')

    ax.set_ylim(0, 48)
    cbar = fig.colorbar(img, ax=ax)
    cbar.ax.tick_params(labelsize=18)

    plt.title('Input CWT of %s' % (title, ), fontsize=20)
    plt.ylabel('Scales', fontsize=18)
    plt.xlabel('Mass', fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    file_name_in = file_name[0] + '_input' + file_name[1]
    path_input = 'docs/output/' + file_name_in + '.jpeg'
    plt.savefig(path_input)
    plt.close('all')

    fig, ax = plt.subplots(figsize=(9, 7))

    img = ax.imshow(reconstructed[0].reshape(shape),
                    extent=(0, 64, 48, 0),
                    interpolation='sinc',
                    aspect='auto',
                    cmap='bwr')

    ax.set_ylim(0, 48)

    cbar = fig.colorbar(img, ax=ax)
    cbar.ax.tick_params(labelsize=18)

    plt.title('Output CWT %s' % (title,), fontsize=20)
    plt.ylabel('Scales', fontsize=18)
    plt.xlabel('Mass', fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    file_name_out = file_name[0] + '_output' + file_name[1]
    path_output = 'docs/output/' + file_name_out + '.jpeg'
    plt.savefig(path_output)
    plt.close('all')


def loss_distribution(test_data, prediction_data):
    mse = tf.keras.losses.mean_squared_error(
        test_data.reshape(len(test_data), 64*48),
        prediction_data.reshape(len(prediction_data), 48*64))

    return mse


def model_efficiency_p_value(bg_losses, signal_losses):
    signal_median = np.median(signal_losses)
    count = 0

    for bg_loss in bg_losses:
        if bg_loss >= signal_median:
            count += 1

    p_value = count / len(bg_losses)

    return p_value


def plot_histogram(bgs, signal, name, file_name=''):
    # the histogram of the data
    p_value = model_efficiency_p_value(bgs, signal)

    fig, ax = plt.subplots(figsize=(9, 7))

    plt.hist(bgs, bins=150, range=(min(signal), max(signal)), facecolor='red', alpha=0.5, label='background')
    plt.hist(signal, bins=150, range=(min(signal), max(signal)), facecolor='blue', alpha=0.5, label='background + signal')

    plt.xlabel('Value', fontsize=18)
    plt.ylabel('Count', fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.title('%s loss distribution, efficiency_p_value: %s' % (name, p_value, ), fontsize=20)
    plt.grid(True)
    plt.legend(loc='upper right', fontsize=18)

    path = 'docs/output/' + file_name + '_loss_dist.jpeg'
    plt.savefig(path)
    plt.close('all')

"""
SHAPE = 1560
dataset_1 = "/data/test_dataset_1/Sep-07-20T11-37-27$10000"
-----------------------------------------------------------
SHAPE = 24500
dataset_2 = "data/test_dataset_2/Sep-16-20T06-52-27$15000"
-----------------------------------------------------------
SHAPE = 4900
dataset_v1 = "data/dataset_v1/Sep-21-20T12-09-32$10000"
"""

import os
import tensorflow as tf
import numpy as np

from datetime import datetime, date
from keras.layers import Input, Dense
from keras.models import Model
from keras import utils

today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

NAME = 'deep_ae/'
BASE_DIR = "data/models/" + NAME + "%s_T_%s" % (current_day, current_time)

PATH_AUTOENCODER = BASE_DIR + '/autoencoder.h5'
PATH_ENCODER = BASE_DIR + '/encoder.h5'
PATH_DECODER = BASE_DIR + '/decoder.h5'

SHAPE = 4900
SIGNALS_NUM = 5

DATASET_PATH = 'data/dataset_v1_1/Sep-27-20T01-13-31$25000'
TRAIN_PATH = DATASET_PATH + '/train_backgrounds.npy'
TEST_SIGNALS = DATASET_PATH + '/test_signals_1.npy'
TEST_BACKGROUNDS = DATASET_PATH + '/test_backgrounds.npy'


def load_data():
    train_data = np.load(TRAIN_PATH)
    test_bg_data = np.load(TEST_BACKGROUNDS)
    test_signal_data = np.load(TEST_SIGNALS)

    train_data = utils.normalize(train_data, axis=1)
    test_bg_data = utils.normalize(test_bg_data, axis=1)
    test_signal_data = utils.normalize(test_signal_data, axis=1)

    train_data = train_data.reshape(len(train_data), np.prod(train_data.shape[1:]))
    test_bg_data = test_bg_data.reshape(len(test_bg_data), np.prod(test_bg_data.shape[1:]))
    test_signal_data = test_signal_data.reshape(len(test_signal_data), np.prod(test_signal_data.shape[1:]))

    return train_data, test_bg_data, test_signal_data


def load_model():
    encoding_dim = 64
    input_img = Input(shape=(SHAPE,))

    encoded = Dense(1024, activation='relu')(input_img)
    encoded = Dense(512, activation='relu')(encoded)
    encoded = Dense(128, activation='relu')(encoded)
    encoded = Dense(encoding_dim, activation='relu')(encoded)

    decoded = Dense(128, activation='relu')(encoded)
    decoded = Dense(512, activation='relu')(decoded)
    decoded = Dense(1024, activation='relu')(decoded)
    decoded = Dense(input_img, activation='sigmoid')(decoded)

    autoencoder = Model(input_img, decoded)
    encoded_input = Input(shape=(encoding_dim,))
    decoder_layer = autoencoder.layers[-1]
    decoder = Model(encoded_input, decoder_layer(encoded_input))
    encoder = Model(input_img, encoded)

    autoencoder.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError())

    return autoencoder, encoder, decoder


def train(autoencoder, train_data, test_bg_data):
    print(train_data.shape)
    autoencoder.fit(train_data, train_data,
                    epochs=100,
                    batch_size=256,
                    shuffle=True,
                    validation_data=(test_bg_data, test_bg_data))

    autoencoder.save(PATH_AUTOENCODER)


def main():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    train_data, test_bg_data, test_signal_data = load_data()
    print(train_data.shape, test_bg_data.shape, test_signal_data.shape)
    autoencoder, encoder, decoder = load_model()
    train(autoencoder, train_data, test_bg_data)

    encoder.save(PATH_ENCODER)
    decoder.save(PATH_DECODER)


if __name__ == '__main__':
    main()

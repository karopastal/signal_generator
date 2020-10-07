import os
import tensorflow as tf
import numpy as np

from datetime import datetime, date
from keras.models import Model
from keras.optimizers import Adam
from keras import utils, layers
import keras

today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

# DATASET_PATH = 'data/dataset_v1_1/Sep-27-20T01-42-06$15000'
DATASET_PATH = 'data/dataset_v1_1/Sep-27-20T01-13-31$25000'
TRAIN_PATH = DATASET_PATH + '/train_backgrounds.npy'
TEST_SIGNALS = DATASET_PATH + '/test_signals_1.npy'
TEST_BACKGROUNDS = DATASET_PATH + '/test_backgrounds.npy'
TRAIN_SIZE = DATASET_PATH.split('$')[1]

NAME = 'conv_ae_%s/' % (TRAIN_SIZE,)
BASE_DIR = "data/models/" + NAME + "%s_T_%s" % (current_day, current_time)

PATH_AUTOENCODER = BASE_DIR + '/autoencoder.h5'
PATH_ENCODER = BASE_DIR + '/encoder.h5'
PATH_DECODER = BASE_DIR + '/decoder.h5'
PATH_SUMMARY = BASE_DIR + '/summary.txt'

SHAPE = 4900
SIGNALS_NUM = 5


def load_data():
    train_data = np.load(TRAIN_PATH)
    test_bg_data = np.load(TEST_BACKGROUNDS)

    train_data = utils.normalize(train_data, axis=1)
    test_bg_data = utils.normalize(test_bg_data, axis=1)

    train_data = train_data.reshape(len(train_data), 49, 100, 1)
    test_bg_data = test_bg_data.reshape(len(test_bg_data), 49, 100, 1)

    train_data_marginal = np.zeros((len(train_data), 50, 100, 1))
    test_bg_data_marginal = np.zeros((len(test_bg_data), 50, 100, 1))

    train_data_marginal[:, :-1, :, :] = train_data
    test_bg_data_marginal[:, :-1, :, :] = test_bg_data

    return train_data_marginal, test_bg_data_marginal


def load_model():
    input_layer = layers.Input(shape=(50, 100, 1))

    # encoder
    h = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
    h = layers.MaxPooling2D((2, 2), padding='same')(h)

    # decoder
    h = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(h)
    h = layers.UpSampling2D((2, 2))(h)
    output_layer = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(h)

    autoencoder = keras.Model(input_layer, output_layer)
    autoencoder.compile(optimizer=Adam(learning_rate=0.01), loss='mse')

    # autoencoder.compile(optimizer=Adam(learning_rate=0.0001),
    #                     loss=tf.keras.losses.MeanSquaredError())

    print(autoencoder.summary())

    return autoencoder
    # autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
    #
    # autoencoder = Model(input_img, decoded)
    # encoder = Model(input_img, encoded)
    # encoded_input = keras.Input(shape=(encoding_dim,))
    #
    # decoder_layer = autoencoder.layers[-4](encoded_input)
    # decoder_layer = autoencoder.layers[-3](decoder_layer)
    # decoder_layer = autoencoder.layers[-2](decoder_layer)
    # decoder_layer = autoencoder.layers[-1](decoder_layer)
    #
    # decoder = Model(encoded_input, decoder_layer)

    # autoencoder.compile(optimizer=Adam(learning_rate=0.0001),
    #                     loss=tf.keras.losses.MeanSquaredError())
    #
    # return autoencoder, encoder, decoder


def train(autoencoder, train_data, test_bg_data):
    print(train_data.shape)
    autoencoder.fit(train_data, train_data,
                    epochs=50,
                    batch_size=64,
                    shuffle=True,
                    validation_data=(test_bg_data, test_bg_data))

    autoencoder.save(PATH_AUTOENCODER)

    with open('summary.txt', 'w') as fh:
        autoencoder.summary(print_fn=lambda x: fh.write(x + '\n'))

    print("model done training")


def main():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    train_data, test_bg_data = load_data()
    print(train_data.shape, test_bg_data.shape)
    # autoencoder, encoder, decoder = load_model()
    autoencoder = load_model()
    train(autoencoder, train_data, test_bg_data)

    # encoder.save(PATH_ENCODER)
    # decoder.save(PATH_DECODER)


if __name__ == '__main__':
    main()

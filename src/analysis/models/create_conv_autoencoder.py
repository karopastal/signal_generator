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
    # test_signal_data = np.load(TEST_SIGNALS)

    train_data = utils.normalize(train_data, axis=1)
    test_bg_data = utils.normalize(test_bg_data, axis=1)
    # test_signal_data = utils.normalize(test_signal_data, axis=1)

    # train_data = train_data.reshape(len(train_data), np.prod(train_data.shape[1:]))
    # test_bg_data = test_bg_data.reshape(len(test_bg_data), np.prod(test_bg_data.shape[1:]))
    # test_signal_data = test_signal_data.reshape(len(test_signal_data), np.prod(test_signal_data.shape[1:]))

    return train_data, test_bg_data


def load_model():
    input_img = keras.Input(shape=(49, 100, 1))
    encoding_dim = (7, 10)

    x = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    encoded = layers.MaxPooling2D((2, 2), padding='same')(x)

    # at this point the representation is (4, 4, 8) i.e. 128-dimensional

    x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
    x = layers.UpSampling2D((2, 2))(x)
    x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = layers.UpSampling2D((2, 2))(x)
    x = layers.Conv2D(16, (3, 3), activation='relu')(x)
    x = layers.UpSampling2D((2, 2))(x)
    decoded = layers.Conv2D(1, (3, 3), activation='relu', padding='same')(x)

    autoencoder = keras.Model(input_img, decoded)
    autoencoder.compile(optimizer=Adam(learning_rate=0.0001),
                        loss=tf.keras.losses.MeanSquaredError())

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
    train(autoencoder, train_data)

    # encoder.save(PATH_ENCODER)
    # decoder.save(PATH_DECODER)


if __name__ == '__main__':
    main()

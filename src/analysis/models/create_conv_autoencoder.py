import os
import tensorflow as tf
import numpy as np

from datetime import datetime, date
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import CSVLogger
from keras import utils
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D

today = date.today()
now = datetime.now()
current_day = today.strftime("%b-%d-%y")
current_time = now.strftime("%H-%M-%S")

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
PATH_CSV_LOGGER = BASE_DIR + '/training.log'

SHAPE = (49, 100)
SIGNALS_NUM = 5


def load_data():
    train_data = np.load(TRAIN_PATH)
    test_bg_data = np.load(TEST_BACKGROUNDS)

    train_data = train_data / -np.log(0.0001)
    test_bg_data = test_bg_data / -np.log(0.0001)

    train_data = train_data.reshape(len(train_data), 49, 100, 1)
    test_bg_data = test_bg_data.reshape(len(test_bg_data), 49, 100, 1)

    train_data_marginal = np.zeros((len(train_data), 50, 100, 1))
    test_bg_data_marginal = np.zeros((len(test_bg_data), 50, 100, 1))

    train_data_marginal[:, :-1, :, :] = train_data
    test_bg_data_marginal[:, :-1, :, :] = test_bg_data

    return train_data_marginal, test_bg_data_marginal


def load_model():
    input_layer = Input(shape=(50, 100, 1))

    # encoder
    h = Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
    h = MaxPooling2D((2, 2), padding='same')(h)

    # decoder
    h = Conv2D(64, (3, 3), activation='relu', padding='same')(h)
    h = UpSampling2D((2, 2))(h)
    output_layer = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(h)

    autoencoder = Model(input_layer, output_layer)
    autoencoder.compile(optimizer=Adam(learning_rate=0.0001), loss=tf.keras.losses.MeanSquaredError())
    # autoencoder.compile(optimizer='adam', loss='mse')

    print(autoencoder.summary())

    return autoencoder


def train(autoencoder, train_data, test_bg_data):
    print(train_data.shape)

    csv_logger = CSVLogger(PATH_CSV_LOGGER)

    autoencoder.fit(train_data, train_data,
                    epochs=100,
                    batch_size=64,
                    shuffle=True,
                    validation_data=(test_bg_data, test_bg_data),
                    callbacks=[csv_logger])

    autoencoder.save(PATH_AUTOENCODER)

    with open(PATH_SUMMARY, 'w') as fh:
        autoencoder.summary(print_fn=lambda x: fh.write(x + '\n'))

    print("model done training")


def main():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    train_data, test_bg_data = load_data()
    print(train_data.shape, test_bg_data.shape)
    autoencoder = load_model()
    train(autoencoder, train_data, test_bg_data)


if __name__ == '__main__':
    main()
    # pass

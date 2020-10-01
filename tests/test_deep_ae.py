import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Model, load_model
from keras import utils, regularizers

# DATASET_PATH = 'data/test_dataset_1/Sep-07-20T11-37-27$10000'
# TRAIN_PATH = DATASET_PATH + '/train_backgrounds.npy'
# TEST_SIGNALS = DATASET_PATH + '/test_signals_1.npy'
# TEST_BACKGROUNDS = DATASET_PATH + '/test_backgrounds.npy'
#
# PATH_AUTOENCODER = 'data/models/test_dataset_1/pca/autoencoder.h5'
# PATH_ENCODER = 'data/models/test_dataset_1/pca/encoder.h5'
# PATH_DECODER = 'data/models/test_dataset_1/pca/decoder.h5'

DATASET_PATH = 'data/test_data_v1_1_15000'
# TRAIN_PATH = DATASET_PATH + '/train_backgrounds.npy'
TEST_SIGNALS = DATASET_PATH + '/test_signals_1.npy'
TEST_BACKGROUNDS = DATASET_PATH + '/test_backgrounds.npy'

PATH_AUTOENCODER = 'data/models/deep_ae_25000/Sep-30-20_T_16-15-15/autoencoder.h5'
PATH_ENCODER = 'data/models/deep_ae_25000/Sep-30-20_T_16-15-15/encoder.h5'
PATH_DECODER = 'data/models/deep_ae_25000/Sep-30-20_T_16-15-15/decoder.h5'


def plot_prediction(x_test, encoder, decoder):
    encoded_imgs = encoder.predict(x_test)
    decoded_imgs = decoder.predict(encoded_imgs)

    print(encoded_imgs.shape)
    print(x_test.shape)

    n = 4  # how many digits we will display
    plt.figure(figsize=(20, 20))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape(49, 100), cmap='pink')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape(49, 100), cmap='pink')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.show()


def load_data():
    # train_data = np.load(TRAIN_PATH)
    test_bg_data = np.load(TEST_BACKGROUNDS)
    test_signal_data = np.load(TEST_SIGNALS)

    # train_data = utils.normalize(train_data, axis=1)
    test_bg_data = utils.normalize(test_bg_data, axis=1)
    test_signal_data = utils.normalize(test_signal_data, axis=1)

    # train_data = train_data.reshape(len(train_data), np.prod(train_data.shape[1:]))
    test_bg_data = test_bg_data.reshape(len(test_bg_data), np.prod(test_bg_data.shape[1:]))
    test_signal_data = test_signal_data.reshape(len(test_signal_data), np.prod(test_signal_data.shape[1:]))

    return [], test_bg_data, test_signal_data


# mse = tf.keras.losses.MeanSquaredError()
# train_data, test_bg_data, test_signal_data = load_data()
# autoencoder = load_model(PATH_AUTOENCODER)
# encoder = load_model(PATH_ENCODER)
# decoder = load_model(PATH_DECODER)


# predict_bgs_test = autoencoder.predict(test_bg_data)
# predict_signal1_test = autoencoder.predict(test_signal_data)

# mse(test_bg_data, predict_bgs_test)
# mse(test_signal_data, predict_signal1_test)


def main():
    autoencoder = load_model(PATH_AUTOENCODER)
    encoder = load_model(PATH_ENCODER)
    decoder = load_model(PATH_DECODER)

    train_data, test_bg_data, test_signal_data = load_data()
    plot_prediction(np.array(test_bg_data[0:3]), encoder, decoder)
    # plot_prediction(train_data[0:4])


if __name__ == '__main__':
    main()

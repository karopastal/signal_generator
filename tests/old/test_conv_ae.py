import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Model, load_model
from keras import utils, regularizers

""" conv ae """
############################################################################
"""
activation = sigmoid
normalization = utils.normalize()
--------------------------------------
PREDICTIONS LOSS
--------------------------------------
loss backgrounds :  0.0001261545
loss signals     :  9.004219e-05
-------------------------------------
"""
BASE_DIR_MODELS = 'data/models/conv_ae_25000/Oct-07-20_T_18-02-20'

"""
activation = sigmoid
normalization = -np.log(0.001)
--------------------------------------
PREDICTIONS LOSS
--------------------------------------
loss backgrounds :  ?
loss signals     :  ?
-------------------------------------
"""
# BASE_DIR_MODELS = data/models/conv_ae_25000/Oct-08-20_T_11-48-28/

"""
activation = linear
normalization = -np.log(0.001)
--------------------------------------
PREDICTIONS LOSS
--------------------------------------
loss backgrounds :  ?
loss signals     :  ?
-------------------------------------
"""
# BASE_DIR_MODELS = 'data/models/conv_ae_25000/Oct-08-20_T_12-49-13'

"""
activation = relu
normalization = -np.log(0.001)
--------------------------------------
PREDICTIONS LOSS
--------------------------------------
loss backgrounds :  ?
loss signals     :  ?
-------------------------------------
"""
# BASE_DIR_MODELS = 'data/models/conv_ae_25000/Oct-08-20_T_12-49-13'
#########################################################################


DATASET_PATH = 'data/dataset_v1_1/Sep-27-20T01-13-31$25000'
TEST_SIGNALS = DATASET_PATH + '/test_signals_2.npy'
TEST_BACKGROUNDS = DATASET_PATH + '/test_backgrounds.npy'

# BASE_DIR_MODELS = 'data/models/conv_ae_25000/Oct-07-20_T_18-02-20'
PATH_AUTOENCODER = BASE_DIR_MODELS + '/autoencoder.h5'


def plot_prediction(x_test, autoencoder):
    decoded_imgs = autoencoder.predict(x_test)

    print(decoded_imgs.shape)
    print(x_test.shape)

    n = 2  # how many digits we will display
    plt.figure(figsize=(20, 20))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape((50, 100)), cmap='pink')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape((50, 100)), cmap='pink')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.show()


def load_data():
    test_signals_data = np.load(TEST_SIGNALS)
    test_bg_data = np.load(TEST_BACKGROUNDS)

    # test_signals_data = utils.normalize(test_signals_data, axis=1)
    # test_bg_data = utils.normalize(test_bg_data, axis=1)

    test_signals_data = test_signals_data.reshape(len(test_signals_data), 49, 100, 1)
    test_bg_data = test_bg_data.reshape(len(test_bg_data), 49, 100, 1)

    test_signals_data_marginal = np.zeros((len(test_signals_data), 50, 100, 1))
    test_bg_data_marginal = np.zeros((len(test_bg_data), 50, 100, 1))

    test_signals_data_marginal[:, :-1, :, :] = test_signals_data
    test_bg_data_marginal[:, :-1, :, :] = test_bg_data

    return test_bg_data_marginal, test_signals_data_marginal


def test_predictions_loss(mse, autoencoder, test_bg_data, test_signal_data):
    predict_bgs_test = autoencoder.predict(test_bg_data)
    predict_signal_test = autoencoder.predict(test_signal_data)

    print("PREDICTIONS LOSS")
    print("--------------------------------------")
    print("loss backgrounds : ", mse(test_bg_data, predict_bgs_test).numpy())
    print("loss signals     : ", mse(test_signal_data, predict_signal_test).numpy())
    print("--------------------------------------")


def main():
    mse = tf.keras.losses.MeanSquaredError()
    autoencoder = load_model(PATH_AUTOENCODER)

    test_bg_data, test_signal_data = load_data()

    plot_prediction(np.array(test_bg_data[0:2]), autoencoder)
    plot_prediction(np.array(test_signal_data[0:2]), autoencoder)
    test_predictions_loss(mse, autoencoder, test_bg_data, test_signal_data)


if __name__ == '__main__':
    # pass
    main()

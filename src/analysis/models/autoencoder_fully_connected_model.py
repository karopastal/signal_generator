# import numpy as np
# from keras.layers import Input, Dense
# from keras.models import Model, load_model
# from keras import utils, regularizers
# import matplotlib.pyplot as plt


PATH_AUTOENCODER_TOY_TRAIN_DATASET = 'data/autoencoder_toy_train_dataset.npy'
PATH_AUTOENCODER_TOY_TEST_SIGNALS_DATASET = 'data/autoencoder_toy_test_signals_dataset.npy'
PATH_AUTOENCODER_TOY_TEST_BACKGROUNDS_DATASET = 'data/autoencoder_toy_backgrounds_test_dataset.npy'

PATH_AUTOENCODER = 'data/models/f_c_autoencoder.h5'
PATH_ENCODER = 'data/models/f_c_encoder.h5'
PATH_DECODER = 'data/models/f_c_decoder.h5'


def normalize_and_reshape(data):
    data = utils.normalize(data, axis=1)
    data = data.reshape((len(data)), np.prod(data.shape[1:]))

    return data


def load_data():
    x_train_backgrounds = normalize_and_reshape(np.load(PATH_AUTOENCODER_TOY_TRAIN_DATASET))
    x_test_signals = normalize_and_reshape(np.load(PATH_AUTOENCODER_TOY_TEST_SIGNALS_DATASET))
    x_test_backgrounds = normalize_and_reshape(np.load(PATH_AUTOENCODER_TOY_TEST_BACKGROUNDS_DATASET))

    return x_train_backgrounds, x_test_signals, x_test_backgrounds


def load_autoencoder_fully_connected_model(img_shape):
    encoding_dim = 128
    input_img = Input(shape=(63*500,))

    encoded = Dense(728, activation='relu')(input_img)
    encoded = Dense(256, activation='relu')(encoded)
    encoded = Dense(encoding_dim, activation='relu')(encoded)

    decoded = Dense(256, activation='relu')(encoded)
    decoded = Dense(728, activation='relu')(decoded)
    decoded = Dense(63*500, activation='sigmoid')(decoded)

    # this model maps an input to its reconstruction
    autoencoder = Model(input_img, decoded)

    # this model maps an input to its encoded representation
    encoder = Model(input_img, encoded)

    encoded_input = Input(shape=(encoding_dim,))
    decoder_layer = autoencoder.layers[-3]
    # create the decoder model

    decoder = Model(encoded_input, decoder_layer(encoded_input))

    autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

    return encoder, decoder, autoencoder


def train_model(model, x_train, x_test):
    model.fit(x_train,
              x_train,
              epochs=5,
              batch_size=25,
              shuffle=True,
              validation_data=(x_test, x_test))

    model.save(PATH_AUTOENCODER)


def test_model(model, x_test_signals, x_test_backgrounds):
    pass


def main():
    x_train_backgrounds, x_test_signals, x_test_backgrounds = load_data()

    print(x_train_backgrounds[0].shape)

    img_shape = x_train_backgrounds[0].shape
    encoder, decoder, autoencoder = load_autoencoder_fully_connected_model(img_shape)

    train_model(autoencoder, x_train_backgrounds, x_test_backgrounds[:500])

    encoder.save(PATH_ENCODER)
    decoder.save(PATH_DECODER)

    # encoder = load_model(PATH_ENCODER)
    # decoder = load_model(PATH_DECODER)
    # autoencoder = load_model(PATH_AUTOENCODER)

    # test_model(model, x_test_signals, x_test_backgrounds[501:1000])

    # encoded_imgs = encoder.predict(x_test_signals[600:611])
    # decoded_imgs = decoder.predict(encoded_imgs)
    #
    # plt.imshow(x_test_backgrounds[600:611][0].reshape(63, 500))
    # plt.show()
    #
    # plt.imshow(decoded_imgs[0].reshape(63, 500))
    # plt.show()


if __name__ == '__main__':
    # main()
    print("autoencoder too expirimental at this stage")

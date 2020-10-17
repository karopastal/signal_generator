import numpy as np
import src.models.utils as model_utils

from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import CSVLogger


name = 'deep_ae'


class DeepAutoencoder:
    def __init__(self, path_model='', path_dataset='', encoding_dim=8):

        self.path_model = path_model
        self.trained_autoencoder = None

        self.path_dataset = path_dataset
        self.base_dir = model_utils.get_ae_base_dir(name)
        self.path_autoencoder = self.base_dir + '/autoencoder.h5'
        self.path_summary = self.base_dir + '/summary.txt'
        self.path_csv_logger = self.base_dir + '/training.log'

        self.dataset_config = model_utils.get_dataset_config(self.path_dataset)
        model_utils.copy_dataset_config(self.path_dataset, self.base_dir)

        self.original_shape = self.dataset_config['ORIGINAL_SHAPE']
        self.shape = np.prod(self.original_shape)
        self.encoding_dim = encoding_dim

        optimizer = Adam(lr=0.0001)

        self.autoencoder_model = self.build_model()
        self.autoencoder_model.compile(loss='mse', optimizer=optimizer)

    def build_model(self):
        input_layer = Input(shape=(self.shape,))

        encoded = Dense(512, activation='relu')(input_layer)
        encoded = Dense(128, activation='relu')(encoded)
        encoded = Dense(64, activation='relu')(encoded)
        encoded = Dense(self.encoding_dim, activation='relu')(encoded)

        decoded = Dense(64, activation='relu')(encoded)
        decoded = Dense(128, activation='relu')(decoded)
        decoded = Dense(512, activation='relu')(decoded)
        output_layer = Dense(self.shape, activation='relu')(decoded)

        return Model(input_layer, output_layer)

    def load_data(self):
        train_data = model_utils.load_train_data(self.path_dataset)
        test_bgs_data = model_utils.load_test_bgs_data(self.path_dataset)

        train_shape = (self.dataset_config['TRAIN_SIZE'], self.shape)
        test_bgs_shape = (self.dataset_config['TEST_BACKGROUND_SIZE'], self.shape)

        factor = -1 * np.log(0.01)
        norm_train_data = model_utils.normalize(train_data.reshape(train_shape), factor)
        norm_test_bgs_data = model_utils.normalize(test_bgs_data.reshape(test_bgs_shape), factor)

        return norm_train_data, norm_test_bgs_data

    def train_model(self, epochs=5, batch_size=64):
        train_data, test_bgs_data = self.load_data()

        csv_logger = CSVLogger(self.path_csv_logger)

        self.autoencoder_model.fit(train_data, train_data,
                                   epochs=epochs,
                                   batch_size=batch_size,
                                   shuffle=True,
                                   validation_data=(test_bgs_data, test_bgs_data),
                                   callbacks=[csv_logger])

        self.autoencoder_model.save(self.path_autoencoder)

        with open(self.path_summary, 'w') as fh:
            self.autoencoder_model.summary(print_fn=lambda x: fh.write(x + '\n'))

    def load_model(self):
        self.trained_autoencoder = np.load(self.path_model)

    def eval_model(self, x_test):
        self.load_model()

        predictions = self.trained_autoencoder.predict(x_test)

        return predictions

    def summary(self):
        return self.autoencoder_model.summary()

    def plot_things(self):
        # encoder =
        # decoder =

        # todo: plot comparison...
        return self.autoencoder_model.summary()

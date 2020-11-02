import numpy as np
import src.models.utils as model_utils

from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model, load_model
from keras.optimizers import Adam
from keras.callbacks import CSVLogger
# from keras.regularizers import l1
# use KL reg


class ConvAutoencoder:
    def __init__(self,
                 path_model='',
                 path_dataset='',
                 name='conv_ae'):

        self.name = name
        self.path_model = path_model

        if path_model != '':
            self.path_autoencoder = self.path_model + '/autoencoder.h5'
            self.path_summary = self.path_model + '/summary.txt'
            self.path_loss_progress = self.path_model + '/training.log'
            self.autoencoder_model = load_model(self.path_autoencoder)
            self.dataset_config = model_utils.get_dataset_config(self.path_model)
            self.path_dataset = self.dataset_config['PATH_DATASET']
            self.shape = self.dataset_config['ORIGINAL_SHAPE']

        else:
            self.path_dataset = path_dataset
            self.base_dir = model_utils.get_ae_base_dir(self.name)
            self.path_autoencoder = self.base_dir + '/autoencoder.h5'
            self.path_summary = self.base_dir + '/summary.txt'
            self.path_csv_logger = self.base_dir + '/training.log'

            self.dataset_config = model_utils.get_dataset_config(self.path_dataset)
            model_utils.copy_dataset_config(self.path_dataset, self.base_dir)

            self.shape = self.dataset_config['ORIGINAL_SHAPE']
            optimizer = Adam(lr=0.0001)

            self.autoencoder_model = self.build_model()
            self.autoencoder_model.compile(loss='mse', optimizer=optimizer)

    def build_model(self):
        input_layer = Input(shape=(self.shape[0], self.shape[1], 1))

        # encoder
        h = Conv2D(32, (3, 3), activation='relu', padding='same')(input_layer)
        h = MaxPooling2D((2, 2), padding='same')(h)
        h = Conv2D(64, (3, 3), activation='relu', padding='same')(h)
        h = MaxPooling2D((2, 2), padding='same')(h)
        h = Conv2D(128, (3, 3), activation='relu', padding='same')(h)
        h = MaxPooling2D((2, 2), padding='same')(h)

        # Dense()

        # decoder
        h = Conv2D(128, (3, 3), activation='relu', padding='same')(h)
        h = UpSampling2D((2, 2))(h)
        h = Conv2D(64, (3, 3), activation='relu', padding='same')(h)
        h = UpSampling2D((2, 2))(h)
        h = Conv2D(32, (3, 3), activation='relu', padding='same')(h)
        h = UpSampling2D((2, 2))(h)
        output_layer = Conv2D(1, (3, 3), activation='relu', padding='same')(h)

        return Model(input_layer, output_layer)

    def load_train_data(self):
        train_data = model_utils.load_train_data(self.path_dataset)
        test_bgs_data = model_utils.load_test_bgs_data(self.path_dataset)

        factor = -1 * np.log(0.01)
        norm_train_data = model_utils.normalize(train_data, factor)
        norm_test_bgs_data = model_utils.normalize(test_bgs_data, factor)

        return norm_train_data, norm_test_bgs_data

    def train_model(self, epochs=5, batch_size=64):
        train_data, test_bgs_data = self.load_train_data()

        csv_logger = CSVLogger(self.path_csv_logger)

        self.autoencoder_model.fit(train_data, train_data,
                                   epochs=epochs,
                                   batch_size=batch_size,
                                   shuffle=True,
                                   validation_data=(test_bgs_data, test_bgs_data),
                                   callbacks=[csv_logger])

        print(self.path_autoencoder)
        self.autoencoder_model.save(self.path_autoencoder)

        with open(self.path_summary, 'w') as fh:
            self.autoencoder_model.summary(print_fn=lambda x: fh.write(x + '\n'))

    def load_model(self):
        self.autoencoder_model = load_model(self.path_autoencoder)

    def load_test_data(self, signal_id=1):
        test_bgs_data = model_utils.load_test_bgs_data(self.path_dataset)
        test_signal_data = model_utils.load_test_signal_data(self.path_dataset, signal_id=signal_id)

        factor = -1 * np.log(0.01)
        norm_test_bgs_data = model_utils.normalize(test_bgs_data, factor)
        norm_test_signal_data = model_utils.normalize(test_signal_data, factor)

        return norm_test_bgs_data, norm_test_signal_data

    def predict(self, x_test):
        predictions = self.autoencoder_model.predict(x_test)

        return predictions

    def eval_model(self, signal_id=1):
        losses = {}
        test_bgs_data, test_signal_data = self.load_test_data(signal_id=signal_id)

        predict_bgs_test = self.predict(test_bgs_data)
        predict_signal_test = self.predict(test_signal_data)

        losses['test_bgs_data'] = test_bgs_data
        losses['test_signal_data'] = test_signal_data
        losses['predict_bgs_test'] = predict_bgs_test.reshape(losses['test_bgs_data'].shape)
        losses['predict_signal_test'] = predict_signal_test.reshape(losses['test_signal_data'].shape)

        model_utils.print_predictions_loss(losses=losses)

        model_utils.plot_prediction(self.autoencoder_model,
                                    test_bgs_data[0:3],
                                    self.shape)

        model_utils.plot_prediction(self.autoencoder_model,
                                    test_signal_data[0:3],
                                    self.shape)

    def create_loss_distribution(self, signal_id=1):
        test_bgs_data, test_signal_data = self.load_test_data(signal_id=signal_id)

        predict_bgs_test = self.predict(test_bgs_data)
        predict_signal_test = self.predict(test_signal_data)

        test_bgs_distribution = model_utils.loss_distribution(test_bgs_data,
                                                              predict_bgs_test.reshape(test_bgs_data.shape))

        test_signal_distribution = model_utils.loss_distribution(test_signal_data,
                                                                 predict_signal_test.reshape(test_signal_data.shape))
        model_utils.plot_histogram(test_bgs_distribution.numpy(), test_signal_distribution.numpy())

    def summary(self):
        return self.autoencoder_model.summary()

    def plot_progress(self, title=''):
        if self.path_model != '':
            model_utils.plot_progress(self.path_loss_progress, title=title)
        else:
            print('error, load model first')

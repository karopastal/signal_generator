import os
import json
import pickle
import numpy as np
import matplotlib.pyplot as plt

from src.models.deep_ae import DeepAutoencoder
from src.models.sparse_ae_v1 import SparseAutoencoderV1
from src.models.sparse_ae_v2 import SparseAutoencoderV2
from src.models.conv_ae import ConvAutoencoder
from src.models.conv_l1_ae import ConvL1Autoencoder
from src.models.conv_kl_ae import ConvKLAutoencoder
from src.models.utils import model_efficiency_p_value, loss_distribution

PATH_TEST_BACKGROUNDS = 'data/dataset/Oct-16-20T14-39-16$25000/test_backgrounds.npy'
PATH_TEST_SIGNALS = 'data/signals_dataset/Oct-29-20T14-49-21$5000'
PATH_SIGNALS_CONFIG = 'config/signals/sessions/test_dataset_2.json'

PATH_SAVE_RESULTS = 'tests/models/sensitivity_results'


def to_json(path):
    with open(path) as f:
        data = json.load(f)
    return data


def get_models():
    models = list()

    path_deep_ae_1 = 'data/models/deep_ae/Oct-17-20_T_21-13-37'
    models.append({'name': 'deep_ae',
                   'ae': DeepAutoencoder(path_model=path_deep_ae_1),
                   'shape': (5000, 3072),
                   'linestyle': '-'})

    path_sparse_ae_v1_2 = 'data/models/sparse_ae_v1/Oct-18-20_T_19-38-29'
    models.append({'name': 'sparse_ae_l1',
                   'ae': SparseAutoencoderV1(path_model=path_sparse_ae_v1_2),
                   'shape': (5000, 3072),
                   'linestyle': '-'})

    path_sparse_ae_v2_11 = 'data/models/sparse_kl_ae/Oct-26-20_T_15-15-38'
    models.append({'name': 'sparse_ae_kl',
                   'ae': SparseAutoencoderV2(path_model=path_sparse_ae_v2_11),
                   'shape': (5000, 3072),
                   'linestyle': '-'})

    path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08'
    models.append({'name': 'conv_ae',
                   'ae': ConvAutoencoder(path_model=path_conv_ae_1),
                   'shape': (5000, 48, 64),
                   'linestyle': '--'})

    path_conv_l1_ae_2 = 'data/models/conv_l1_ae/Nov-03-20_T_12-30-04'
    models.append({'name': 'conv_l1_ae',
                   'ae': ConvL1Autoencoder(path_model=path_conv_l1_ae_2),
                   'shape': (5000, 48, 64),
                   'linestyle': '--'})

    path_conv_kl_ae_2 = 'data/models/conv_kl_ae/Nov-03-20_T_12-35-50'
    models.append({'name': 'conv_kl_ae',
                   'ae': ConvKLAutoencoder(path_model=path_conv_kl_ae_2),
                   'shape': (5000, 48, 64),
                   'linestyle': '--'})

    return models


def get_path_signal(signal):
    return PATH_TEST_SIGNALS + '/test_signals_%s.npy' % (signal['id'],)


def plot_p_values_vs_signal_size(signal_size, results):

    fig, ax = plt.subplots()

    for model in results:
        ax.plot(signal_size,
                model['p_values'],
                linestyle=model['linestyle'],
                marker='.',
                markersize=10,
                label=model['name'])

    plt.yscale('log')
    plt.grid(True, which="both", linestyle='--')
    plt.title(r"p_value vs signal size", fontsize=18)
    plt.ylabel("p_value", fontsize=16)
    plt.xlabel("signal size", fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    ax.legend()
    plt.show()


def model_signal_sensitivity(models, signals):
    factor = -1 * np.log(0.01)
    results = list()
    signal_size = [int(signal['gaussian']['height']) for signal in signals]

    for model in models:
        model['p_values'] = list()
        print(model['name'])
        print('------------------------')

        test_bgs = np.load(PATH_TEST_BACKGROUNDS).reshape(model['shape'])/factor
        predict_bgs = model['ae'].predict(test_bgs)

        bgs_losses = loss_distribution(
            test_bgs,
            predict_bgs
        )

        for signal in signals:

            test_signal = np.load(get_path_signal(signal)).reshape(model['shape'])/factor
            predict_signal = model['ae'].predict(test_signal)

            signal_losses = loss_distribution(
                test_signal,
                predict_signal
            )

            p_value = model_efficiency_p_value(bgs_losses.numpy(),
                                               signal_losses.numpy())

            print(signal['id'], 'p_value: ', p_value)

            model['p_values'].append(p_value)

        results.append(model)

    return signal_size, results


def main():
    signals = to_json(PATH_SIGNALS_CONFIG)[4:]
    signals.sort(key=lambda x: x['gaussian']['height'])

    if not os.path.exists(PATH_SAVE_RESULTS):
        models = get_models()
        signal_size, results = model_signal_sensitivity(models, signals)

        copy_results = results.copy()

        for x in copy_results:
            x.pop('ae', None)

        out_result_file = open(PATH_SAVE_RESULTS, 'wb')
        pickle.dump(copy_results, out_result_file)
        out_result_file.close()

    else:
        signal_size = [int(signal['gaussian']['height']) for signal in signals]
        results = pickle.load(open(PATH_SAVE_RESULTS, 'rb'))

    plot_p_values_vs_signal_size(signal_size, results)


if __name__ == '__main__':
    main()

#!/bin/python3

import os

python_3_8_4 = '/gpfs0/kats/projects/Python-3.8.4/python'

train_pca_ae = python_3_8_4 + ' -m src.analysis.models.create_pca_autoencoder'
train_deep_ae = python_3_8_4 + ' -m src.analysis.models.create_deep_ae_autoencoder'
# train_conv_ae = python_3_8_4 + ' -m src.analysis.models.create_pca_autoencoder'
# train_sparse_ae = python_3_8_4 + ' -m src.analysis.models.create_pca_autoencoder'
# train_generative_ae = python_3_8_4 + ' -m src.analysis.models.create_pca_autoencoder'

os.system(train_deep_ae)

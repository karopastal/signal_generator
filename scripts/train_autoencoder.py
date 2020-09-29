#!/bin/python3

import os

python_3_8_4 = '/gpfs0/kats/projects/Python-3.8.4/python'

run_command = python_3_8_4 + ' -m src.analysis.models.create_pca_autoencoder'

os.system(run_command)

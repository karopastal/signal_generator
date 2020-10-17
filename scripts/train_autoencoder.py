#!/bin/python3

import os

python_3_8_4 = '/gpfs0/kats/projects/Python-3.8.4/python'

train_model = python_3_8_4 + ' -m src.models.train_model'

os.system(train_model)

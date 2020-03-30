#!/bin/bash

make load-session NAME=autoencoder_toy_dataset

#PYTHON3_PATH="/gpfs0/kats/projects/Python-3.4.5/python"
PYTHON3_PATH="/bin/python3"

#SCRIPT_PATH="/gpfs0/kats/users/talpas/signal_generator/src/analysis/"
SCRIPT_PATH="/gpfs0/kats/users/talpas/signal_generator/scripts/test.py"

qsub -cwd -q kats.q -S $PYTHON3_PATH $SCRIPT_PATH

#qsub -cwd -q kats.q -S python3 -m src.analysis.datasets_factory.autoencoder_dataset
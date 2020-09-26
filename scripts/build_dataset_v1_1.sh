#!/bin/bash

path_to_python="/gpfs0/kats/projects/Python-3.8.4/python"
script_path="/gpfs0/kats/users/talpas/workbench/signal_generator/scripts/build_dataset_v1_1.py"

qsub -cwd -q kats.q -S path_to_python $script_path

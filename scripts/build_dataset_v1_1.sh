#!/bin/bash

# export path_to_python="/gpfs0/kats/projects/Python-3.8.4/python"
export path_to_python="/bin/python3"
export script_path="/gpfs0/kats/users/talpas/projects/signal_generator/scripts/build_dataset_v1_1.py"

qsub -cwd -q kats.q -S $path_to_python $script_path

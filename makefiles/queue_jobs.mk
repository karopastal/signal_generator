queue-build-autoencoder-dataset:
        @PYTHON3_PATH="/bin/python3" && \
		 SCRIPT_PATH="/gpfs0/kats/users/talpas/signal_generator/scripts/build_autoencoder_dataset.py" && \
		 qsub -cwd -q kats.q -S $PYTHON3_PATH $SCRIPT_PATH


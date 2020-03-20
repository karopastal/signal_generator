vis-autoencoder-toy-dataset:
	@python3 -m src.visualizations.autoencoder_toy_dataset

#vis-autoencoder-toy-dataset:
#	@python3 -m src.visualizations.${NAME}

plot-background:
	@python3 -m src.default_background $(BG_ID)

plot-signal:
	@python3 -m src.default_signal $(SIGNAL_ID)

plot-clean:
	@python3 -m src.default_clean $(SIGNAL_ID) $(BG_ID)

plot-fluctuations:
	@python3 -m src.default_fluctuations $(SIGNAL_ID) $(BG_ID)

plot-cwt-clean:
	@python3 -m src.default_cwt_clean $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

plot-cwt-fluctuations:
	@python3 -m src.default_cwt_fluctuations $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

plot-p-value-clean:
	@python3 -m src.default_cwt_p_value_clean $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

plot-p-value-fluctuations:
	@python3 -m src.default_cwt_p_value_fluctuations $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)
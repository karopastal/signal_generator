classifier-toy-dataset:
	@make load-session NAME=classifier_toy_dataset && \
	python3 -m src.analysis.datasets_factory.classifier_toy_dataset

autoencoder-toy-dataset:
	@make load-session NAME=autoencoder_toy_dataset && \
	python3 -m src.analysis.datasets_factory.autoencoder_toy_dataset
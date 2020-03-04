classifier-toy-dataset:
	@make load-session NAME=classifier_toy_dataset && \
	python3 -m src.analysis.datasets_factory.classifier_toy_dataset

autoencoder-toy-dataset:
	@make load-session NAME=autoencoder_toy_dataset && \
	python3 -m src.analysis.datasets_factory.autoencoder_toy_dataset

p_value_test:
	@python3 -m src.analysis.datasets_factory.p_value_transformation

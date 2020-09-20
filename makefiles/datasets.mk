#classifier-toy-dataset:
#	@make load-session NAME=classifier_toy_dataset && \
#	python3 -m src.analysis.datasets_factory.classifier_toy_dataset
#
#autoencoder-dataset:
#	@make load-session NAME=autoencoder_toy_dataset && \
#	python3 -m src.analysis.datasets_factory.autoencoder_dataset
#
#p_value_test:
#	@python3 -m src.analysis.datasets_factory.p_value_transformation

create-test-dataset-1:
	@make load-session NAME=test_dataset_1 && \
	python3 -m src.analysis.datasets_factory.create_test_dataset_1

create-test-dataset-2:
	@make load-session NAME=test_dataset_2 && \
	python3 -m src.analysis.datasets_factory.create_test_dataset_2

create-test-dataset-2-p-value:
	@make load-session NAME=test_dataset_2 && \
	python3 -m src.analysis.datasets_factory.create_test_dataset_2_p_value
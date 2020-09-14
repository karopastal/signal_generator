#classifier-fully-connected-model:
#	@python3 -m src.analysis.models.classifier_fully_connected_model
#
#classifier-convolutional-model:
#	@python3 -m src.analysis.models.classifier_convolutional_model
#
#autoencoder-fully-connected-model:
#		@python3 -m src.analysis.models.autoencoder_fully_connected_model


train-pca-autoencoter:
	@python3 -m src.analysis.models.create_pca_autoencoder

test-pca-autoencoter:
	@python3 -m src.analysis.models.test_pca_autoencoder

train-sparse-autoencoter:
	@python3 -m src.analysis.models.create_pca_autoencoder

test-sparse-autoencoter:
	@python3 -m src.analysis.models.test_sparse_autoencoder
from src.models.deep_ae import DeepAutoencoder

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=8)

deep_ae.train_model(epochs=5, batch_size=64)

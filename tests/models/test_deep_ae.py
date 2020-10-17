from src.models.deep_ae import DeepAutoencoder

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
deep_ae = DeepAutoencoder(path_dataset=path_dataset)

# print(deep_ae.summary)
# print(deep_ae.dataset_config)
print(deep_ae.shape)

train_data, test_data = deep_ae.load_data()
print(train_data.shape, test_data.shape)
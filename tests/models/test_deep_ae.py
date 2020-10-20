from src.models.deep_ae import DeepAutoencoder

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
# deep_ae = DeepAutoencoder(path_dataset=path_dataset)

# print(deep_ae.summary)
# print(deep_ae.dataset_config)
# print(deep_ae.shape)

# train_data, test_data = deep_ae.load_data()
# print(train_data.shape, test_data.shape)

path_deep_ae_1 = 'data/models/deep_ae/Oct-17-20_T_21-13-37'
deep_ae_1 = DeepAutoencoder(path_model=path_deep_ae_1)
deep_ae_1.plot_progress(title='deep_ae_1')
deep_ae_1.eval_model(signal_id=1)
deep_ae_1.create_loss_distribution(signal_id=1)
# deep_ae_1.plot_progress(title='deep_ae_1')

# path_deep_ae_2 = 'data/models/deep_ae/Oct-17-20_T_21-22-05'
# deep_ae_2 = DeepAutoencoder(path_model=path_deep_ae_2)
# deep_ae_2.eval_model(signal_id=1)
# deep_ae_2.plot_progress(title='deep_ae_2')

# path_deep_ae_3 = 'data/models/deep_ae/Oct-17-20_T_21-27-03'
# deep_ae_3 = DeepAutoencoder(path_model=path_deep_ae_1)
# deep_ae_3.eval_model(signal_id=1)

# deep_ae_3.plot_progress(title='deep_ae_3')

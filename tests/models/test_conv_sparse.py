from src.models.conv_sparse_ae import ConvSparseKLAutoencoder

"""
    path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08' 
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

path_conv_sparse_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08'
conv_ae_1 = ConvSparseKLAutoencoder(path_model=path_conv_ae_1)
conv_ae_1.plot_progress(title='conv_ae')
conv_ae_1.eval_model(signal_id=4)
conv_ae_1.create_loss_distribution(signal_id=4)



from src.models.conv_ae import ConvAutoencoder
# from src.models.conv_ae_v1 import ConvAutoencoderV1


"""
    path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08' 
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08'
conv_ae_1 = ConvAutoencoder(path_model=path_conv_ae_1)
# conv_ae_1.plot_progress(title='conv_ae_1')
# conv_ae_1.eval_model(signal_id=4)
conv_ae_1.create_loss_distribution(signal_id=4)

#
path_conv_ae_2 = 'data/models/conv_ae/Oct-26-20_T_15-53-55'
conv_ae_2 = ConvAutoencoder(path_model=path_conv_ae_2)
# conv_ae_2.plot_progress(title='conv_ae_2')
# conv_ae_2.eval_model(signal_id=4)
conv_ae_2.create_loss_distribution(signal_id=4)

path_conv_ae_3 = 'data/models/conv_ae/Oct-26-20_T_15-55-52'
conv_ae_3 = ConvAutoencoder(path_model=path_conv_ae_3)
# conv_ae_3.plot_progress(title='conv_ae_3')
# conv_ae_3.eval_model(signal_id=4)
conv_ae_3.create_loss_distribution(signal_id=4)

# ------------------------------------------------------------

path_conv_ae_v1_1 = 'data/models/conv_ae_v1/Oct-26-20_T_16-04-40'
conv_ae_v1_1 = ConvAutoencoderV1(path_model=path_conv_ae_v1_1)
# conv_ae_v1_1.plot_progress(title='conv_ae_v1_1')
# conv_ae_v1_1.eval_model(signal_id=4)
conv_ae_v1_1.create_loss_distribution(signal_id=4)

path_conv_ae_v1_2 = 'data/models/conv_ae_v1/Oct-26-20_T_16-05-54'
conv_ae_v1_2 = ConvAutoencoderV1(path_model=path_conv_ae_v1_2)
# conv_ae_v1_2.plot_progress(title='conv_ae_v1_2')
# conv_ae_v1_2.eval_model(signal_id=4)
conv_ae_v1_2.create_loss_distribution(signal_id=4)

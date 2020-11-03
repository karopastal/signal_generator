from src.models.conv_l1_ae import ConvL1Autoencoder
from src.models.conv_kl_ae import ConvKLAutoencoder

"""
    path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08' 
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

# path_conv_l1_ae_1 = 'data/models/conv_l1_ae/Nov-03-20_T_12-27-50'
# conv_l1_ae_1 = ConvL1Autoencoder(path_model=path_conv_l1_ae_1)
# conv_l1_ae_1.plot_progress(title='conv_l1_ae')
# conv_l1_ae_1.eval_model(signal_id=4)
# conv_l1_ae_1.create_loss_distribution(signal_id=4)

path_conv_l1_ae_2 = 'data/models/conv_l1_ae/Nov-03-20_T_12-30-04'
conv_l1_ae_2 = ConvL1Autoencoder(path_model=path_conv_l1_ae_2)
conv_l1_ae_2.plot_progress(title='conv_l1_ae')
conv_l1_ae_2.eval_model(signal_id=4)
conv_l1_ae_2.create_loss_distribution(signal_id=4)

# path_conv_l1_ae_3 = 'data/models/conv_l1_ae/Nov-03-20_T_12-31-02'
# conv_l1_ae_3 = ConvL1Autoencoder(path_model=path_conv_l1_ae_3)
# conv_l1_ae_3.plot_progress(title='conv_l1_ae')
# conv_l1_ae_3.eval_model(signal_id=4)
# conv_l1_ae_3.create_loss_distribution(signal_id=4)

# path_conv_l1_ae_4 = 'data/models/conv_l1_ae/Nov-03-20_T_12-32-17'
# conv_l1_ae_4 = ConvL1Autoencoder(path_model=path_conv_l1_ae_4)
# conv_l1_ae_4.plot_progress(title='conv_l1_ae')
# conv_l1_ae_4.eval_model(signal_id=4)
# conv_l1_ae_4.create_loss_distribution(signal_id=4)

# --------------------------------------------------------------
#
# path_conv_kl_ae_1 = 'data/models/conv_kl_ae/Nov-03-20_T_12-34-05'
# conv_kl_ae_1 = ConvKLAutoencoder(path_model=path_conv_kl_ae_1)
# conv_kl_ae_1.plot_progress(title='conv_kl_ae')
# conv_kl_ae_1.eval_model(signal_id=4)
# conv_kl_ae_1.create_loss_distribution(signal_id=4)

path_conv_kl_ae_2 = 'data/models/conv_kl_ae/Nov-03-20_T_12-35-50'
conv_kl_ae_2 = ConvKLAutoencoder(path_model=path_conv_kl_ae_2)
conv_kl_ae_2.plot_progress(title='conv_kl_ae')
conv_kl_ae_2.eval_model(signal_id=4)
conv_kl_ae_2.create_loss_distribution(signal_id=4)

# path_conv_kl_ae_3 = 'data/models/conv_kl_ae/Nov-03-20_T_12-37-06'
# conv_kl_ae_3 = ConvKLAutoencoder(path_model=path_conv_kl_ae_3)
# conv_kl_ae_3.plot_progress(title='conv_kl_ae')
# conv_kl_ae_3.eval_model(signal_id=4)
# conv_kl_ae_3.create_loss_distribution(signal_id=4)
#
# path_conv_kl_ae_4 = 'data/models/conv_kl_ae/Nov-03-20_T_12-39-37'
# conv_kl_ae_4 = ConvKLAutoencoder(path_model=path_conv_kl_ae_4)
# conv_kl_ae_4.plot_progress(title='conv_kl_ae')
# conv_kl_ae_4.eval_model(signal_id=4)
# conv_kl_ae_4.create_loss_distribution(signal_id=4)


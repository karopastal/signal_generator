from src.models.deep_ae import DeepAutoencoder
from src.models.sparse_ae_v1 import SparseAutoencoderV1
from src.models.sparse_ae_v2 import SparseAutoencoderV2
from src.models.conv_ae import ConvAutoencoder
from src.models.conv_l1_ae import ConvL1Autoencoder
from src.models.conv_kl_ae import ConvKLAutoencoder


def evaluate_ae(ae, signal_id, name):
    ae.plot_progress(title=name)
    ae.eval_model(signal_id=signal_id, name=name)
    ae.create_loss_distribution(signal_id=signal_id, name=name)


for i in range(4, 5):
    # deep ae #1
    path_deep_ae_1 = 'data/models/deep_ae/Oct-17-20_T_21-13-37'

    evaluate_ae(
        DeepAutoencoder(path_model=path_deep_ae_1),
        signal_id=i,
        name='DAE')

    # sparse ae v1 #2 L1
    path_sparse_ae_v1_2 = 'data/models/sparse_ae_v1/Oct-18-20_T_19-38-29'

    evaluate_ae(
        SparseAutoencoderV1(path_model=path_sparse_ae_v1_2),
        signal_id=i,
        name='SAE L1')

    # sparse ae v2 #2 KL
    path_sparse_ae_v2_11 = 'data/models/sparse_kl_ae/Oct-26-20_T_15-15-38'

    evaluate_ae(
        SparseAutoencoderV2(path_model=path_sparse_ae_v2_11),
        signal_id=i,
        name='SAE KL')

    # conv ae #1
    path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08'

    evaluate_ae(
        ConvAutoencoder(path_model=path_conv_ae_1),
        signal_id=i,
        name='CAE'
    )

    # conv l1 ae #2
    path_conv_l1_ae_2 = 'data/models/conv_l1_ae/Nov-03-20_T_12-30-04'

    evaluate_ae(
        ConvL1Autoencoder(path_model=path_conv_l1_ae_2),
        signal_id=i,
        name='CAE L1'
    )

    # conv kl ae #2
    path_conv_kl_ae_2 = 'data/models/conv_kl_ae/Nov-03-20_T_12-35-50'

    evaluate_ae(
        ConvKLAutoencoder(path_model=path_conv_kl_ae_2),
        signal_id=i,
        name='CAE KL regularization'
    )

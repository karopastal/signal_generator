from src.models.deep_ae import DeepAutoencoder
from src.models.sparse_ae import SparseAutoencoder
from src.models.sparse_ae_v1 import SparseAutoencoderV1
from src.models.sparse_ae_v2 import SparseAutoencoderV2


def evaluate_ae(ae, signal_id, name):
    ae.plot_progress(title=name)
    # ae.eval_model(signal_id=signal_id)
    ae.create_loss_distribution(signal_id=signal_id)


for i in range(4, 5):
    # deep ae #1
    path_deep_ae_1 = 'data/models/deep_ae/Oct-17-20_T_21-13-37'

    evaluate_ae(
        DeepAutoencoder(path_model=path_deep_ae_1),
        signal_id=i,
        name='deep_ae_1')

    # sparse ae #1
    path_sparse_ae_1 = 'data/models/sparse_ae/Oct-18-20_T_19-13-04'

    evaluate_ae(
        SparseAutoencoder(path_model=path_deep_ae_1),
        signal_id=i,
        name='sparse_ae_1')

    # sparse ae v1 #2
    path_sparse_ae_v1_2 = 'data/models/sparse_ae_v1/Oct-18-20_T_19-38-29'

    evaluate_ae(
        SparseAutoencoderV1(path_model=path_sparse_ae_v1_2),
        signal_id=i,
        name='sparse_ae_1')

    # sparse ae v2 #2
    path_sparse_ae_v2_2 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-50-28'

    evaluate_ae(
        SparseAutoencoderV2(path_model=path_sparse_ae_v2_2),
        signal_id=i,
        name='path_sparse_ae_v2_2')



from src.models.sparse_ae_v1 import SparseAutoencoderV1

"""
    # sparse_ae_v1_1()  # path = 'data/models/sparse_ae_v1/Oct-18-20_T_19-36-45'
    # sparse_ae_v1_2()  # path = 'data/models/sparse_ae_v1/Oct-18-20_T_19-38-29'
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

path_sparse_ae_v1_1 = 'data/models/sparse_ae_v1/Oct-18-20_T_19-36-45'
sparse_ae_v1_1 = SparseAutoencoderV1(path_model=path_sparse_ae_v1_1)
sparse_ae_v1_1.plot_progress(title='sparse_ae_1')
sparse_ae_v1_1.eval_model(signal_id=4)
sparse_ae_v1_1.create_loss_distribution(signal_id=4)

path_sparse_ae_v1_2 = 'data/models/sparse_ae_v1/Oct-18-20_T_19-38-29'
sparse_ae_v1_2 = SparseAutoencoderV1(path_model=path_sparse_ae_v1_2)
sparse_ae_v1_2.plot_progress(title='sparse_ae_2')
sparse_ae_v1_2.eval_model(signal_id=4)
sparse_ae_v1_2.create_loss_distribution(signal_id=4)

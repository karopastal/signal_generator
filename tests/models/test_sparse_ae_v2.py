from src.models.sparse_ae_v2 import SparseAutoencoderV2

"""
    # sparse_ae_v2_1()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_22-16-21'
    # sparse_ae_v2_2()  # path = 'data/models/sparse_ae_v2/'
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

path_sparse_ae_v2_1 = 'data/models/sparse_ae_v2/Oct-19-20_T_22-16-21'
sparse_ae_v2_1 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_1)
sparse_ae_v2_1.plot_progress(title='sparse_ae_v2_1')
sparse_ae_v2_1.eval_model(signal_id=1)
# sparse_ae_v1_1.create_loss_distribution(signal_id=3)

# path_sparse_ae_v2_2 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-05-14'
# sparse_ae_v2_2 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_2)
# sparse_ae_v2_2.plot_progress(title='sparse_ae_v2_2')
# sparse_ae_v2_2.eval_model(signal_id=5)

# sparse_ae_v1_1.create_loss_distribution(signal_id=3)
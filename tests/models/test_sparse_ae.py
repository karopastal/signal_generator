from src.models.sparse_ae import SparseAutoencoder

"""
    # sparse_ae_1()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-13-04'
    # sparse_ae_2()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-15-47'
    # sparse_ae_3()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-17-01'
    # sparse_ae_4()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-26-00'
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

# path_sparse_ae_1 = 'data/models/sparse_ae/Oct-18-20_T_19-13-04'
# sparse_ae_1 = SparseAutoencoder(path_model=path_sparse_ae_1)
# # sparse_ae_1.plot_progress(title='sparse_ae_1')
# sparse_ae_1.eval_model(signal_id=1)
# # sparse_ae_1.create_loss_distribution(signal_id=3)
#
# path_sparse_ae_2 = 'data/models/sparse_ae/Oct-18-20_T_19-15-47'
# sparse_ae_2 = SparseAutoencoder(path_model=path_sparse_ae_2)
# # sparse_ae_2.plot_progress(title='sparse_ae_2')
# sparse_ae_2.eval_model(signal_id=1)
# # sparse_ae_2.create_loss_distribution(signal_id=3)
#
# path_sparse_ae_3 = 'data/models/sparse_ae/Oct-18-20_T_19-17-01'
# sparse_ae_3 = SparseAutoencoder(path_model=path_sparse_ae_3)
# # sparse_ae_3.plot_progress(title='sparse_ae_3')
# sparse_ae_3.eval_model(signal_id=1)
# # sparse_ae_1.create_loss_distribution(signal_id=3)
#
# path_sparse_ae_4 = 'data/models/sparse_ae/Oct-18-20_T_19-26-00'
# sparse_ae_4 = SparseAutoencoder(path_model=path_sparse_ae_4)
# # sparse_ae_4.plot_progress(title='sparse_ae_4')
# sparse_ae_4.eval_model(signal_id=1)
# # sparse_ae_1.create_loss_distribution(signal_id=3)

path_sparse_ae_1 = 'data/models/sparse_ae/Oct-18-20_T_19-13-04'
sparse_ae_1 = SparseAutoencoder(path_model=path_sparse_ae_1)
sparse_ae_1.plot_progress(title='sparse_ae_1')
sparse_ae_1.eval_model(signal_id=1)
sparse_ae_1.create_loss_distribution(signal_id=1)

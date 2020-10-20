from src.models.sparse_ae_v2 import SparseAutoencoderV2

"""
    # sparse_ae_v2_1()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-14-07'
        # sparse_ae_v2_2()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-50-28'
    # sparse_ae_v2_3()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-53-00'
    # sparse_ae_v2_4()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-54-47'
    # sparse_ae_v2_5()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-59-17'
    
        # sparse_ae_v2_6()  # path = 'data/models/sparse_ae_v2/Oct-20-20_T_00-39-30'
        # sparse_ae_v2_7()  # path = 'data/models/sparse_ae_v2/Oct-20-20_T_00-40-27'
        # sparse_ae_v2_8()  # path = 'data/models/sparse_ae_v2/Oct-20-20_T_00-42-28'
"""

path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

# path_sparse_ae_v2_1 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-14-07'
# sparse_ae_v2_1 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_1)
# sparse_ae_v2_1.plot_progress(title='sparse_ae_v2_1')
# sparse_ae_v2_1.eval_model(signal_id=1)
# # sparse_ae_v2_1.create_loss_distribution(signal_id=3)
#
path_sparse_ae_v2_2 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-50-28'
sparse_ae_v2_2 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_2)
sparse_ae_v2_2.plot_progress(title='sparse_ae_v2_2')
sparse_ae_v2_2.eval_model(signal_id=5)
sparse_ae_v2_2.create_loss_distribution(signal_id=5)

#
# path_sparse_ae_v2_3 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-53-00'
# sparse_ae_v2_3 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_3)
# sparse_ae_v2_3.plot_progress(title='sparse_ae_v2_3')
# sparse_ae_v2_3.eval_model(signal_id=1)
#
# path_sparse_ae_v2_4 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-54-47'
# sparse_ae_v2_4 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_4)
# sparse_ae_v2_4.plot_progress(title='sparse_ae_v2_4')
# sparse_ae_v2_4.eval_model(signal_id=1)
#
# path_sparse_ae_v2_5 = 'data/models/sparse_ae_v2/Oct-19-20_T_23-59-17'
# sparse_ae_v2_5 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_5)
# sparse_ae_v2_5.plot_progress(title='sparse_ae_v2_5')
# sparse_ae_v2_5.eval_model(signal_id=1)
# # sparse_ae_v1_1.create_loss_distribution(signal_id=3)

# path_sparse_ae_v2_6 = 'data/models/sparse_ae_v2/Oct-20-20_T_00-40-27'
# sparse_ae_v2_6 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_6)
# sparse_ae_v2_6.plot_progress(title='sparse_ae_v2_6')
# sparse_ae_v2_6.eval_model(signal_id=1)
#
# path_sparse_ae_v2_7 = 'data/models/sparse_ae_v2/Oct-20-20_T_00-40-27'
# sparse_ae_v2_7 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_7)
# sparse_ae_v2_7.plot_progress(title='sparse_ae_v2_7')
# sparse_ae_v2_7.eval_model(signal_id=1)
#
# path_sparse_ae_v2_8 = 'data/models/sparse_ae_v2/Oct-20-20_T_00-42-28'
# sparse_ae_v2_8 = SparseAutoencoderV2(path_model=path_sparse_ae_v2_8)
# sparse_ae_v2_8.plot_progress(title='sparse_ae_v2_8')
# sparse_ae_v2_8.eval_model(signal_id=1)
# # sparse_ae_v1_1.create_loss_distribution(signal_id=3)

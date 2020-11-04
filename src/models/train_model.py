from keras import regularizers

from src.models.deep_ae import DeepAutoencoder
from src.models.sparse_ae_v1 import SparseAutoencoderV1
from src.models.sparse_ae_v2 import SparseAutoencoderV2
from src.models.conv_ae import ConvAutoencoder
from src.models.conv_l1_ae import ConvL1Autoencoder
from src.models.conv_kl_ae import ConvKLAutoencoder


# ################################# Deep AE ###################################


def deep_ae_1():
    encoding_dim = 8
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=encoding_dim)
    deep_ae.train_model(epochs=200, batch_size=64)


# def deep_ae_2():
#     encoding_dim = 16
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=encoding_dim)
#     deep_ae.train_model(epochs=200, batch_size=64)
#
#
# def deep_ae_3():
#     encoding_dim = 32
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=encoding_dim)
#     deep_ae.train_model(epochs=200, batch_size=64)


# ################################# Sparse AE ###################################

# def sparse_ae_1():
#     rho = 0.0001
#     encoding_dim = 8
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
#     sparse_ae.train_model(epochs=200, batch_size=64)
#
#
# def sparse_ae_2():
#     rho = 0.0001
#     encoding_dim = 16
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
#     sparse_ae.train_model(epochs=200, batch_size=64)
#
#
# def sparse_ae_3():
#     rho = 0.0001
#     encoding_dim = 32
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
#     sparse_ae.train_model(epochs=200, batch_size=64)
#
#
# def sparse_ae_4():
#     rho = 0.0001
#     encoding_dim = 32
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
#     sparse_ae.train_model(epochs=5000, batch_size=64)
#
#
# def sparse_ae_5():
#     rho = 0.00001
#     encoding_dim = 8
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset,
#                                   activity_regularizer=regularizers.l1,
#                                   rho=rho,
#                                   encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=200, batch_size=64)
#
#
# def sparse_ae_6():
#     rho = 0.00001
#     encoding_dim = 8
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset,
#                                   activity_regularizer=regularizers.l2,
#                                   rho=rho,
#                                   encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=200, batch_size=64)
#
#
# def sparse_ae_7():
#     rho = 0.00001
#     encoding_dim = 8
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoder(path_dataset=path_dataset,
#                                   activity_regularizer=regularizers.l1_l2,
#                                   rho=rho,
#                                   encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=200, batch_size=64)


# ################################# Sparse AE V1 ###################################


# def sparse_ae_v1_1():
#     rho = 0.0001
#     encoding_dim = 128
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV1(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
#     sparse_ae.train_model(epochs=5000, batch_size=64)

# ################################# Deep AE ###################################

def sparse_ae_v1_2():
    rho = 0.0001
    encoding_dim = 256
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV1(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=5000, batch_size=64)

# ################################# Sparse AE V2 ###################################


# def sparse_ae_v2_1():
    # rho = 0.9
    # beta = 5
    # encoding_dim = 128
    # path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    # sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
    #                                 rho=rho,
    #                                 beta=beta,
    #                                 encoding_dim=encoding_dim)
    #
    # sparse_ae.train_model(epochs=100, batch_size=64)


def sparse_ae_v2_2():
    rho = 0.09
    beta = 3
    encoding_dim = 128
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=100, batch_size=64)


# def sparse_ae_v2_3():
#     rho = 0.9
#     beta = 3
#     encoding_dim = 256
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=100, batch_size=64)
#
#
# def sparse_ae_v2_4():
#     rho = 0.9
#     beta = 0.3
#     encoding_dim = 128
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=100, batch_size=64)
#
#
# def sparse_ae_v2_5():
#     rho = 0.02
#     beta = 0.3
#     encoding_dim = 256
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=100, batch_size=64)

# ############# like v2_2 ############


# def sparse_ae_v2_6():
#     rho = 0.009
#     beta = 3
#     encoding_dim = 128
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=100, batch_size=64)
#
#
# def sparse_ae_v2_7():
#     rho = 0.09
#     beta = 5
#     encoding_dim = 128
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=100, batch_size=64)
#
#
# def sparse_ae_v2_8():
#     rho = 0.09
#     beta = 3
#     encoding_dim = 64
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=100, batch_size=64)

############################################################

# -------------------------------------------------------------------

# ----------------------------------------------------------------------------------------

# def sparse_ae_v2_9():
#     rho = 0.3
#     beta = 3
#     encoding_dim = 128
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=500, batch_size=64)
#
#
# def sparse_ae_v2_10():
#     rho = 0.09
#     beta = 2.5
#     encoding_dim = 128
#     path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
#     sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
#                                     rho=rho,
#                                     beta=beta,
#                                     encoding_dim=encoding_dim)
#
#     sparse_ae.train_model(epochs=500, batch_size=64)


def sparse_ae_v2_11():
    rho = 0.05
    beta = 3
    encoding_dim = 128
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=200, batch_size=64)


def sparse_ae_v2_12():
    rho = 0.05
    beta = 3
    encoding_dim = 128
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=400, batch_size=64)

# -------------------------------------------------------------------------

# ####### conv ae #########


def conv_ae_1():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvAutoencoder(path_dataset=path_dataset)
    conv_ae.train_model(epochs=200, batch_size=64)


def conv_ae_2():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvAutoencoder(path_dataset=path_dataset)
    conv_ae.train_model(epochs=100, batch_size=64)


def conv_ae_3():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvAutoencoder(path_dataset=path_dataset)
    conv_ae.train_model(epochs=50, batch_size=64)

# #### conv_l1_ae #####


def conv_l1_ae_1():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvL1Autoencoder(path_dataset=path_dataset, lam=0.00001)
    conv_ae.train_model(epochs=200, batch_size=64)


def conv_l1_ae_2():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvL1Autoencoder(path_dataset=path_dataset, lam=0.0001)
    conv_ae.train_model(epochs=200, batch_size=64)


def conv_l1_ae_3():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvL1Autoencoder(path_dataset=path_dataset, lam=0.001)
    conv_ae.train_model(epochs=200, batch_size=64)


def conv_l1_ae_4():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvL1Autoencoder(path_dataset=path_dataset, lam=0.01)
    conv_ae.train_model(epochs=200, batch_size=64)


# #### conv_kl_ae #####

def conv_kl_ae_1():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvKLAutoencoder(path_dataset=path_dataset,
                                beta=0.0003,
                                rho=0.05)

    conv_ae.train_model(epochs=200, batch_size=64)


def conv_kl_ae_2():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvKLAutoencoder(path_dataset=path_dataset,
                                beta=0.00003,
                                rho=0.05)

    conv_ae.train_model(epochs=200, batch_size=64)


def conv_kl_ae_3():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvKLAutoencoder(path_dataset=path_dataset,
                                beta=0.00005,
                                rho=0.05)
    conv_ae.train_model(epochs=200, batch_size=64)


def conv_kl_ae_4():
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'

    conv_ae = ConvKLAutoencoder(path_dataset=path_dataset,
                                beta=0.005,
                                rho=0.05)

    conv_ae.train_model(epochs=200, batch_size=64)


def main():
    """ deep ae """
    # deep_ae_1()  # path = 'data/models/deep_ae/Oct-17-20_T_21-13-37'
    # deep_ae_2()  # path = 'data/models/deep_ae/Oct-17-20_T_21-22-05'
    # deep_ae_3()  # path = 'data/models/deep_ae/Oct-17-20_T_21-27-03'

    """ sparse ae """
    # sparse_ae_1()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-13-04'
    # sparse_ae_2()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-15-47'
    # sparse_ae_3()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-17-01'
    # sparse_ae_4()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-26-00'

    # sparse_ae_5()  # path = 'data/models/sparse_ae/Oct-19-20_T_10-14-43'
    # sparse_ae_6()  # path = 'data/models/sparse_ae/Oct-19-20_T_10-16-11'
    # sparse_ae_7()  # path = 'data/models/sparse_ae/Oct-19-20_T_10-18-27/'

    """ sparse ae v1 """
    # sparse_ae_v1_1()  # path = 'data/models/sparse_ae_v1/Oct-18-20_T_19-36-45'
    # sparse_ae_v1_2()  # path = 'data/models/sparse_ae_v1/Oct-18-20_T_19-38-29'

    """ sparse ae v2 """
    # sparse_ae_v2_1()  # path = 'thereisapath'
    # sparse_ae_v2_2()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-50-28'
    # sparse_ae_v2_3()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-53-00'
    # sparse_ae_v2_4()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-54-47'
    # sparse_ae_v2_5()  # path = 'data/models/sparse_ae_v2/Oct-19-20_T_23-59-17'

    # sparse_ae_v2_6()  # path = 'data/models/sparse_ae_v2/Oct-20-20_T_00-39-30'
    # sparse_ae_v2_7()  # path = 'data/models/sparse_ae_v2/Oct-20-20_T_00-40-27'
    # sparse_ae_v2_8()  # path = 'data/models/sparse_ae_v2/Oct-20-20_T_00-42-28'

    # sparse_ae_v2_9()  # path_sparse_ae_v2_9 =  'data/models/sparse_kl_ae/Oct-26-20_T_15-09-43'
    # sparse_ae_v2_10()  # path_sparse_ae_v2_10 = 'data/models/sparse_kl_ae/Oct-26-20_T_15-13-43'
    # sparse_ae_v2_11()  # path_sparse_ae_v2_11 = 'data/models/sparse_kl_ae/Oct-26-20_T_15-15-38'

    # sparse_ae_v2_11()  # path_sparse_ae_v2_11 = 'data/models/sparse_kl_ae/Oct-26-20_T_15-15-38'

    """ conv ae """
    # conv_ae_1()  # path_conv_ae_1 = 'data/models/conv_ae/Oct-26-20_T_15-19-08'
    # conv_ae_2()  # path_conv_ae_2 = 'data/models/conv_ae/Oct-26-20_T_15-53-55'
    # conv_ae_3()  # path_conv_ae_3 = 'data/models/conv_ae/Oct-26-20_T_15-55-52'

    """ conv ae v1"""

    # conv_ae_v1_1()  # path_conv_ae_v1_1 = 'data/models/conv_ae_v1/Oct-26-20_T_16-04-40'
    # conv_ae_v1_2()  # path_conv_ae_v1_2 = 'data/models/conv_ae_v1/Oct-26-20_T_16-05-54'

    """ conv sparse l1 ae """
    # conv_l1_ae_1()  # path_conv_l1_ae_1 = 'data/models/conv_l1_ae/Nov-03-20_T_12-27-50'
    # conv_l1_ae_2()  # path_conv_l1_ae_2 = 'data/models/conv_l1_ae/Nov-03-20_T_12-30-04'
    # conv_l1_ae_3()  # path_conv_l1_ae_3 = 'data/models/conv_l1_ae/Nov-03-20_T_12-31-02'
    # conv_l1_ae_4()  # path_conv_l1_ae_4 = 'data/models/conv_l1_ae/Nov-03-20_T_12-32-17'

    # conv_kl_ae_1()  # path_conv_kl_ae_1 = 'data/models/conv_kl_ae/Nov-03-20_T_12-34-05'
    # conv_kl_ae_2()  # path_conv_kl_ae_2 = 'data/models/conv_kl_ae/Nov-03-20_T_12-35-50'
    # conv_kl_ae_3()  # path_conv_kl_ae_3 = 'data/models/conv_kl_ae/Nov-03-20_T_12-37-06'
    # conv_kl_ae_4()  # path_conv_kl_ae_4 = 'data/models/conv_kl_ae/Nov-03-20_T_12-39-37'


if __name__ == "__main__":
    main()

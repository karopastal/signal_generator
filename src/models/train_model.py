from keras import regularizers

from src.models.deep_ae import DeepAutoencoder
from src.models.sparse_ae import SparseAutoencoder
from src.models.sparse_ae_v1 import SparseAutoencoderV1
from src.models.sparse_ae_v2 import SparseAutoencoderV2


# ################################# Deep AE ###################################


def deep_ae_1():
    encoding_dim = 8
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=encoding_dim)
    deep_ae.train_model(epochs=200, batch_size=64)


def deep_ae_2():
    encoding_dim = 16
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=encoding_dim)
    deep_ae.train_model(epochs=200, batch_size=64)


def deep_ae_3():
    encoding_dim = 32
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    deep_ae = DeepAutoencoder(path_dataset=path_dataset, encoding_dim=encoding_dim)
    deep_ae.train_model(epochs=200, batch_size=64)


# ################################# Sparse AE ###################################

def sparse_ae_1():
    rho = 0.0001
    encoding_dim = 8
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=200, batch_size=64)


def sparse_ae_2():
    rho = 0.0001
    encoding_dim = 16
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=200, batch_size=64)


def sparse_ae_3():
    rho = 0.0001
    encoding_dim = 32
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=200, batch_size=64)


def sparse_ae_4():
    rho = 0.0001
    encoding_dim = 32
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=5000, batch_size=64)


def sparse_ae_5():
    rho = 0.00001
    encoding_dim = 8
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset,
                                  activity_regularizer=regularizers.l1,
                                  rho=rho,
                                  encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=200, batch_size=64)


def sparse_ae_6():
    rho = 0.00001
    encoding_dim = 8
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset,
                                  activity_regularizer=regularizers.l2,
                                  rho=rho,
                                  encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=200, batch_size=64)


def sparse_ae_7():
    rho = 0.00001
    encoding_dim = 8
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoder(path_dataset=path_dataset,
                                  activity_regularizer=regularizers.l1_l2,
                                  rho=rho,
                                  encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=200, batch_size=64)


# ################################# Sparse AE V1 ###################################


def sparse_ae_v1_1():
    rho = 0.0001
    encoding_dim = 128
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV1(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=5000, batch_size=64)


def sparse_ae_v1_2():
    rho = 0.0001
    encoding_dim = 256
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV1(path_dataset=path_dataset, rho=rho, encoding_dim=encoding_dim)
    sparse_ae.train_model(epochs=5000, batch_size=64)

# ################################# Sparse AE V2 ###################################


def sparse_ae_v2_1():
    rho = 0.9
    beta = 5
    encoding_dim = 128
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=100, batch_size=64)


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


def sparse_ae_v2_3():
    rho = 0.9
    beta = 3
    encoding_dim = 256
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=100, batch_size=64)


def sparse_ae_v2_4():
    rho = 0.9
    beta = 0.3
    encoding_dim = 128
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=100, batch_size=64)


def sparse_ae_v2_5():
    rho = -0.9
    beta = 0.3
    encoding_dim = 256
    path_dataset = 'data/dataset/Oct-16-20T14-39-16$25000'
    sparse_ae = SparseAutoencoderV2(path_dataset=path_dataset,
                                    rho=rho,
                                    beta=beta,
                                    encoding_dim=encoding_dim)

    sparse_ae.train_model(epochs=100, batch_size=64)


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
    sparse_ae_v2_3()  # path = ''
    # sparse_ae_v2_4()  # path = ''
    # sparse_ae_v2_5()  # path = ''


if __name__ == "__main__":
    main()

from src.models.deep_ae import DeepAutoencoder
from src.models.sparse_ae import SparseAutoencoder

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


def main():
    """ deep ae """
    # deep_ae_1()  # path = data/models/deep_ae/Oct-17-20_T_21-13-37
    # deep_ae_2()  # path = data/models/deep_ae/Oct-17-20_T_21-22-05
    # deep_ae_3()  # path = data/models/deep_ae/Oct-17-20_T_21-27-03

    """ sparse ae """
    # sparse_ae_1()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-13-04'
    # sparse_ae_2()  # path = 'data/models/sparse_ae/Oct-18-20_T_19-15-47'
    sparse_ae_3()  # path =


if __name__ == "__main__":
    # execute only if run as a script
    main()

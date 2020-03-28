import unittest


class TestAutoencoder(unittest.TestCase):
    """
    test that the signal behave as expected
    """
    def test1(self):
        pass
        # encoder = load_model(PATH_ENCODER)
        # decoder = load_model(PATH_DECODER)
        # autoencoder = load_model(PATH_AUTOENCODER)
        #
        # test_model(model, x_test_signals, x_test_backgrounds[501:1000])
        #
        # encoded_imgs = encoder.predict(x_test_signals[600:611])
        # decoded_imgs = decoder.predict(encoded_imgs)
        #
        # # plt.imshow(x_test_backgrounds[600:611][0].reshape(63, 500))
        # # plt.show()
        # #
        # # plt.imshow(decoded_imgs[0].reshape(63, 500))
        # # plt.show()


if __name__ == '__main__':
    unittest.main()

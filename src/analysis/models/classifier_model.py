import numpy as np
# from keras import models
# from keras import layers

""" stages:
1. naive sequential neural network, lets try to classify signals (tagging)
2. convolutional neural network, lets try to classify signals (tagging)
3. naive autoencoder (sequential) (annomaly detection) train with backgrounds
4. convolutional autoencoder (annomaly detection) train with backgrounds
5. ways to fine tune conv-autoencoder for better reconstruction results. 
"""

PATH_CLASSIFIER_TOY_DATASET='data/classifier_toy_dataset.npy'

classifier_toy_data = np.load(PATH_CLASSIFIER_TOY_DATASET)
print(classifier_toy_data.shape)


# model = models.Sequential()
#
# model.add(layers.Dense(46, activation='relu', input_shape=(10000,)))
# model.add(layers.Dense(46, activation='relu'))
# model.add(layers.Dense(46, activation='softmax'))
#
# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
# print(model.summary())

""" model.fit() """

# x_val = x_train[:1000]
# partial_x_train = x_train[1000:]
#
# y_val = one_hot_train_labels[:1000]
# partial_y_train = one_hot_train_labels[1000:]
#
# history = model.fit(partial_x_train,
#                     partial_y_train,
#                     epochs=20,
#                     batch_size=516,
#                     validation_data=(x_val, y_val))


# def train():
#     pass
#
#
# def validate():
#     pass

def main():
    pass


if __name__ == '__main__':
    main()
    print("classifier_model entry point")
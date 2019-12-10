import numpy as np
from keras import models
from keras import layers
from keras import utils

""" stages:
1. naive sequential neural network, lets try to classify signals (tagging)
2. convolutional neural network, lets try to classify signals (tagging)
3. naive autoencoder (sequential) (annomaly detection) train with backgrounds
4. convolutional autoencoder (annomaly detection) train with backgrounds
5. ways to fine tune conv-autoencoder for better reconstruction results. 
"""

PATH_CLASSIFIER_TOY_DATASET='data/classifier_toy_dataset.npy'
PATH_CLASSIFIER_TOY_LABELS = 'data/classifier_toy_labels.npy'


def to_one_hot(labels, dimension=3):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results


X = np.load(PATH_CLASSIFIER_TOY_DATASET)
y = np.load(PATH_CLASSIFIER_TOY_LABELS)

X_train = utils.normalize(X[:1000], axis=1)
y_train = to_one_hot(y[:1000])

X_test = utils.normalize(X[1001:1800], axis=1)
y_test = to_one_hot(y[1001:1800])

X_validate = utils.normalize(X[1801:2000], axis=1)
y_validate = to_one_hot(y[1801:2000])

model = models.Sequential()

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train,
                    y_train,
                    epochs=5,
                    validation_data=(X_validate, y_validate))


def main():
    pass


if __name__ == '__main__':
    main()
    print("classifier_model entry point")
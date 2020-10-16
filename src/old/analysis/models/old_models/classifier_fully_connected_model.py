import numpy as np
from keras import models
from keras import layers
from keras import utils

"""
300 training examples with 10 epochs
400 training examples with 8 epochs, bad for 10 epochs
"""

PATH_CLASSIFIER_TOY_DATASET='data/classifier_toy_dataset.npy'
PATH_CLASSIFIER_TOY_LABELS = 'data/classifier_toy_labels.npy'


def to_one_hot(labels, dimension=3):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results


def load_data():
    classifier_toy_dataset = np.load(PATH_CLASSIFIER_TOY_DATASET)
    classifier_toy_labels = np.load(PATH_CLASSIFIER_TOY_LABELS)

    x_train = utils.normalize(classifier_toy_dataset[:450], axis=1)
    y_train = to_one_hot(classifier_toy_labels[:450])

    x_test = utils.normalize(classifier_toy_dataset[801:1800], axis=1)
    y_test = to_one_hot(classifier_toy_labels[801:1800])

    x_validate = utils.normalize(classifier_toy_dataset[1801:2000], axis=1)
    y_validate = to_one_hot(classifier_toy_labels[1801:2000])

    return x_train, y_train, x_test, y_test, x_validate, y_validate


def load_classifier_fully_connected_model():
    model = models.Sequential()

    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(3, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model


def train_model(model, x_train, y_train, x_validate, y_validate, epochs=5):
    print("training classifier_fully_connected model: ")

    model.fit(x_train,
              y_train,
              epochs=epochs,
              validation_data=(x_validate, y_validate))


def test_model(model, x_test, y_test):
    print("testing classifier_fully_connected model: ")

    val_loss, val_acc = model.evaluate(x_test, y_test)

    print(val_loss, val_acc)


def main():
    x_train, y_train, x_test, y_test, x_validate, y_validate = load_data()
    model = load_classifier_fully_connected_model()
    train_model(model, x_train, y_train, x_validate, y_validate, epochs=4)
    test_model(model, x_test, y_test)


if __name__ == '__main__':
    main()

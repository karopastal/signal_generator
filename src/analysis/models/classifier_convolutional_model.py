import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras import utils

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

    x_train = utils.normalize(classifier_toy_dataset[:400], axis=1)
    y_train = to_one_hot(classifier_toy_labels[:400])

    x_test = utils.normalize(classifier_toy_dataset[801:2000], axis=1)
    y_test = to_one_hot(classifier_toy_labels[801:2000])

    return x_train, y_train, x_test, y_test


def load_classifier_convolutional_model(input_shape):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(32))
    model.add(Activation('relu'))

    model.add(Dense(3))
    model.add(Activation('softmax'))

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model


def train_model(model, x_train, y_train, validation_split=0.1, epochs=5, batch_size=10):
    print("training classifier_fully_connected model: ")

    model.fit(x_train,
              y_train,
              epochs=epochs,
              validation_split=validation_split,
              batch_size=batch_size)


def test_model(model, x_test, y_test):
    print("testing classifier_fully_connected model: ")

    val_loss, val_acc = model.evaluate(x_test, y_test)

    print(val_loss, val_acc)


def main():
    x_train, y_train, x_test, y_test = load_data()

    x_train = x_train.reshape(-1, x_train.shape[1], x_train.shape[2], 1)
    x_test = x_test.reshape(-1, x_test.shape[1], x_test.shape[2], 1)

    input_shape = x_train.shape[1:]
    print(input_shape)

    model = load_classifier_convolutional_model(input_shape)
    train_model(model, x_train, y_train, validation_split=0.1, epochs=4, batch_size=10)
    test_model(model, x_test, y_test)


if __name__ == '__main__':
    main()

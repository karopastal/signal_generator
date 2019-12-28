import numpy as np
import matplotlib.pyplot as plt

test_dataset = np.load('data/autoencoder_toy_test_dataset.npy')
train_dataset = np.load('data/autoencoder_toy_train_dataset.npy')

fig = plt.figure(figsize=(100, 200))

for i in range(4):
    sub = fig.add_subplot(2, 2, i + 1)
    sub.imshow(train_dataset[i], interpolation='nearest')


plt.show()

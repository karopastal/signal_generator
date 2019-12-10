import numpy as np
import matplotlib.pyplot as plt

data = np.load('data/classifier_toy_dataset.npy')

fig = plt.figure(figsize=(200, 100))

for i in range(4):
    sub = fig.add_subplot(2, 2, i + 1)
    sub.imshow(data[i], interpolation='nearest')


plt.show()
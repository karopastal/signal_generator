import numpy as np
import matplotlib.pyplot as plt
import pywt
import fluctuations
import clean

SAMPLING_RATE = fluctuations.sampling_range()
SAMPLING_PERIOD = 1/SAMPLING_RATE

cmor_wavelet = pywt.ContinuousWavelet('cmor2.5-2.0)')

print(cmor_wavelet)

data_fluctuations = fluctuations.psi_fluctuations()

scales = np.arange(300, 800)

[coeffs, freqs] = pywt.cwt(data_fluctuations, scales, cmor_wavelet, SAMPLING_PERIOD)

amp = np.abs(coeffs)

fig, ax = plt.subplots(figsize=(12, 12))
ax.imshow(amp, interpolation='nearest', aspect='auto')
plt.show()

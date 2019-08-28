### Signal + Background Generator

python 3.7

```buildoutcfg
$ git clone https://github.com/karopastal/signal_generator.git
```
#### plot signal
```buildoutcfg
$ python mass_signal.py
```
![signal](https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/mass_signal.png)

#### plot clean signal + background
```buildoutcfg
$ python clean.py
```

![clean](https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/clean_signal_bg.png)

#### plot fluctuated signal + background
```buildoutcfg
$ python fluctuations.py
```

![fluctuated](https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/noise_signal_bg.png)


#### plot CWT using Morlet wavelet w/o fluctuations

As a sanity check we can see that the CWT preforming as expected by detecting the signal at the right translation
and getting a pattern for greater scales (lower frequencies) as the signal decays. 

```buildoutcfg
$ python cwt_morlet_clean.py
```

![cwt_clean](https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/clean_coeffs_300_800.png)


#### plot CWT using Morlet wavelet w/ fluctuations
```buildoutcfg
$ python cwt_morlet_fluctuations.py
```

![cwt_fluctuated](https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/fluc_coeffs_300_800.png)

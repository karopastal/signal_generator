## Signal + Background Generator

python 3.7

```buildoutcfg
$ git clone https://github.com/karopastal/signal_generator.git
```

All commands accept `id` (integers) as arguments according to the configurations at `src/signals`, `src/backgrounds`, `src/wavelets`
for example:
``` 
make plot-cwt-clean SIGNAL_ID=1 BG_ID=0 WAVELET_ID=0 
```

### Commands:

#### plot signal
```buildoutcfg
$ make plot-signal SIGNAL_ID={ 0, 1 ... }
```
#### plot background
```buildoutcfg
$ make plot-background BG_ID={ 0, 1 ... }
```
#### plot clean signal + background
```buildoutcfg
$ make plot-clean SIGNAL_ID={ 0, 1 ... } BG_ID={ 0, 1 ... }
```

#### plot fluctuated signal + background
```buildoutcfg
$ make plot-fluctuations SIGNAL_ID={ 0, 1 ... } BG_ID={ 0, 1 ... }
```

#### plot CWT using Morlet wavelet w/o fluctuations 

```buildoutcfg
$ make plot-cwt-clean SIGNAL_ID={ 0, 1 ... } BG_ID={ 0, 1 ... } WAVELET_ID={0, 1 ... }
```

#### plot CWT using Morlet wavelet w/ fluctuations
```buildoutcfg
$ make plot-cwt-fluctuations SIGNAL_ID={ 0, 1 ... } BG_ID={ 0, 1 ... } WAVELET_ID={0, 1 ... }
```
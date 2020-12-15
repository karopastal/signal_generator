# Physics beyond the Standard Model
## Signal over background discovery using CWT and autoencoders.

1. [Overview](#overview)
1. [Setup](#setup)   
2. [Signals, Backgrounds and Wavelets](#signals-backgrounds-and-wavelets)
   * [sessions](#sessions)
   * [commands](#commands)
3. [Analysis](#analysis)
    * [Dataset](#dataset)
    * [Autoencoders](#autoencoders)

<a name="overview"></a>
## Overview
This projects aim is to develop a tool for discovering signals in invariant mass 
distributions. We will take a model-agunostic approach and provide a system
for custom signal and background generation. In order to analyze the invariant
mass distribution we will perform a [Continuous Wavelet Transform](https://en.wikipedia.org/wiki/Continuous_wavelet_transform) 
(CWT) in order to get the mass intervals where the signal is present. In order to create
a tool for anomaly detection, meaning detecting when a signal is present, we will train 
different types and configurations of autoencoders (AE) on background. Thus 
we will reconstruct background with ease after learning the typical background 
fluctuations and reconstruct poorly background + signal.

### Results Example:
Comparing the AEs sensitivity to the signal size for a specific dataset:
 <div style="text-align:center">
    <img src="https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/output/pvalue_vs_signal_size.jpeg" width="620" height="360">
 </div>


### Flow Example:


| Type             |  Plot |
:-------------------------:|:-------------------------:
Signal + Background | <img src="https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/output/cwt/clean_bg_signal.jpeg" width="512" height="256">
Signal + Background + Fluctuations | <img src="https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/output/cwt/fluc_bg_signal.jpeg" width="512" height="256">
CWT | <img src="https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/output/cwt/cwt_bg_signal_fluc.jpeg" width="512" height="256">
Local p-value representation | <img src="https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/output/cwt/rebin_p_value.jpeg" width="512" height="256">
Example: Sparse AE with KL divergence reconstruction | <img src="https://raw.githubusercontent.com/karopastal/signal_generator/master/docs/output/sae_kl_output_bg_signal.jpeg" width="512" height="256">
<a name="setup"></a>


## Setup

python 3.8.6

```buildoutcfg
$ git clone https://github.com/karopastal/signal_generator.git
```

if repository already cloned, pull changes with:

```buildoutcfg
$ git pull
```

install dependencies:
 
```buildoutcfg
$ pip3 install -r requirements.txt
```

run the managment app: 
```buildoutcfg
$ make web
```

visit: http://127.0.0.1:5000/


<a name="signals-backgrounds-and-wavelets"></a>
## Signals, Backgrounds and Wavelets
In order to configure signals, background and wavelets use the managment app.
This is a basic summary of the commands and functionality, for the full tutorial visit [here](https://karopastal.github.io/post/2019/12/10/generating-signals-backgrounds-and-wavelets/) 

<a name="sessions"></a>
### sessions
After configuring the signals, backgrounds and wavelets via the [managment app](http://localhost:5000), the session
of a particular configuration can be saved manually or from the app.

Save session:
```shell script
  $ make save-session NAME={sessions_name}
```

Load a saved session:
```shell script
  $ make load-session NAME={sessions_name}
```

Delete a saved session:
```shell script
  $ make delete-session NAME={sessions_name}
```

List the saved sessions:
```shell script
  $ make list-sessions
```

<a name="commands"></a>
### commands
All commands accept `ids` (integers) as arguments according to the configurations at `src/signals`, `src/backgrounds`, `src/wavelets`
for example:

``` 
make plot-cwt-clean SIGNAL_ID=1 BG_ID=0 WAVELET_ID=0 
```

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

<a name="analysis"></a>
## Analysis
The analysis consists of training different models and test their performance.

<a name="dataset"></a>
```buildoutcfg
$ ./scripts/build_dataset.sh
```

<a name="autoencoders"></a>
### Autoencoders

```buildoutcfg
$ ./scripts/train_autoencoder.sh
```

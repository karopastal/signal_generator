# Physics beyond Standard Model - signal discovery using CWT and Autoencoders

Applying continuous wavelet transforms with autoencoder neural networks for signals over background discovery

<img src="https://media.giphy.com/media/IvrumpcMNOhrO/giphy.gif" width="240" height="120" />

1. [Setup](#setup)   
2. [Signals, Backgrounds and Wavelets](#signals-backgrounds-and-wavelets)
   * [sessions](#sessions)
   * [commands](#commands)
3. [Analysis](#analysis)
    * [classifiers (fully connected, convolutional)](#classifiers)
    * [autoencoders (fully connected, convolutional)](#autoencoders)

<a name="setup"></a>
## Setup

python 3.7

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


old readme at: `docs/examples/README.old.md`

<a name="signals-backgrounds-and-wavelets"></a>
## Signals, Backgrounds and Wavelets

This is a basic summary of the commands and functionality, for the full tutorial visit [here](https://karopastal.github.io/post/2019/12/10/generating-signals-backgrounds-and-wavelets/) 

<a name="sessions"></a>
### sessions
After configuring the signals, backgrounds and wavelets via the [managment app](http://localhost:5000), the session
of a particular configuration can be saved.

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
At this stage we shall generate a local toy dataset to get quickly up and running
with the training and testing of the models.

<a name="classifiers"></a>
### Classifiers
Deep neural networks.

#### Build the local toy dataset:
```shell script
    $ make classifier-toy-dataset
```

#### fully-connected
Train and test the fully-connected model:
```shell script
    $ make classifier-fully-connected-model
```

#### convolutional
Train and test the convolutional model:

```shell script
    $ make classifier-convolutional-model
```    

<a name="autoencoders"></a>
### Autoencoders
   coming soon
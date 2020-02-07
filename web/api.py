import json

PATH_SIGNALS = 'config/signals/default_signal.json'
PATH_BACKGROUNDS = 'config/backgrounds/default_background.json'
PATH_WAVELETS = 'config/wavelets/default_wavelet.json'


def write_json_to_path(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def to_json(path):
    with open(path) as f:
        data = json.load(f)

    return data


def all_signals():
    return to_json(PATH_SIGNALS)


def all_backgrounds():
    return to_json(PATH_BACKGROUNDS)


def all_wavelets():
    return to_json(PATH_WAVELETS)


def update_signals(data):
    signals = all_signals()
    signals[data['id']] = data

    write_json_to_path(PATH_SIGNALS, signals)


def new_signals(data):
    signals = all_signals()
    data['id'] = len(signals)
    signals.append(data)

    write_json_to_path(PATH_SIGNALS, signals)


def delete_signals(id):
    signals = all_signals()
    del signals[int(id)]
    for i, signal in enumerate(signals):
        signal['id'] = i

    write_json_to_path(PATH_SIGNALS, signals)


def update_backgrounds(data):
    backgrounds = all_backgrounds()
    backgrounds[data['id']] = data

    write_json_to_path(PATH_BACKGROUNDS, backgrounds)


def new_backgrounds(data):
    backgrounds = all_backgrounds()
    data['id'] = len(backgrounds)
    backgrounds.append(data)

    write_json_to_path(PATH_BACKGROUNDS, backgrounds)


def delete_backgrounds(id):
    backgrounds = all_backgrounds()
    del backgrounds[int(id)]
    for i, background in enumerate(backgrounds):
        background['id'] = i

    write_json_to_path(PATH_BACKGROUNDS, backgrounds)


def update_wavelets(data):
    wavelets = all_wavelets()
    wavelets[data['id']] = data

    write_json_to_path(PATH_WAVELETS, wavelets)


def new_wavelets(data):
    wavelets = all_wavelets()
    data['id'] = len(wavelets)
    wavelets.append(data)

    write_json_to_path(PATH_WAVELETS, wavelets)


def delete_wavelets(id):
    wavelets = all_wavelets()
    del wavelets[int(id)]
    for i, wavelet in enumerate(wavelets):
        wavelet['id'] = i

    write_json_to_path(PATH_WAVELETS, wavelets)

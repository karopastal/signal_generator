import json
import os
from pathlib import Path
from src.default_clean import save_clean_plot

PATH_SIGNALS = 'config/signals/default_signal.json'
PATH_BACKGROUNDS = 'config/backgrounds/default_background.json'
PATH_WAVELETS = 'config/wavelets/default_wavelet.json'
PATH_ALL_SESSIONS = 'config/sessions/all.json'
PATH_CURRENT_SESSION = 'config/sessions/current.json'
PATH_BASEDIR_PLOTS = "web/static/vue-material-dashboard-master/dist/plots"


def write_json_to_path(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=False)


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


def all_sessions():
    return to_json(PATH_ALL_SESSIONS)


def current_session():
    return to_json(PATH_CURRENT_SESSION)


def new_session(data):
    os.system('make new-session NAME=%s' % (data['basename'], ))

    sessions = all_sessions()
    data['id'] = len(sessions)
    sessions.append(data)

    write_json_to_path(PATH_ALL_SESSIONS, sessions)


def save_current_session_changes():
    current = current_session()

    if current['id'] != -9999:
        os.system('make save-session NAME=%s' % (current['basename'], ))


def load_sessions(data):
    os.system('make load-session NAME=%s' % (data['basename'], ))

    write_json_to_path(PATH_CURRENT_SESSION, data)


def delete_sessions(data):
    sessions = all_sessions()
    current = current_session()

    if current['basename'] == data['basename'] and current['id'] == data['id']:
        empty_session = {
            "id": -9999,
            "name": "session is empty, load from the list."
        }

        write_json_to_path(PATH_CURRENT_SESSION, empty_session)
        os.system('make delete-current-session NAME=%s' % (data['basename'],))
    else:
        os.system('make delete-session NAME=%s' % (data['basename'],))

    del sessions[int(data['id'])]
    for i, signal in enumerate(sessions):
        signal['id'] = i

    write_json_to_path(PATH_ALL_SESSIONS, sessions)


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


def plots_signal_bg(data):
    current = current_session()
    path = PATH_BASEDIR_PLOTS + "/" + current['basename']

    Path(path).mkdir(parents=True, exist_ok=True)

    if data['fluctuations']:
        fluc = "fluctuations"
    else:
        fluc = "clean"

    plot_name = "signal_bg_%s_s%s_b%s" % (fluc, data['signal'], data['background'])
    path = path + "/" + plot_name

    save_clean_plot(path, data['signal'], data['background'])

    return current['basename'] + "/" + plot_name + ".png"


def plots_cwt(data):
    print(data)

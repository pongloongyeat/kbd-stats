import json
import os
import pynput
from datetime import datetime


session = {}
keystat = {
    'pressed_count': 0,
    'released_count': 0
}


def on_press(key: pynput.keyboard.Key) -> None:
    key_name = ""

    try:
        # Alphanumeric key
        key_name = key.char
    except AttributeError:
        # Special key
        key_name = key.name

    try:
        session[key_name]["pressed_count"]
    except KeyError:
        session[key_name] = keystat.copy()

    session[key_name]["pressed_count"] += 1


def on_release(key: pynput.keyboard.Key) -> None:
    key_name = ""

    try:
        # Alphanumeric key
        key_name = key.char
    except AttributeError:
        # Special key
        key_name = key.name

    try:
        session[key_name]["released_count"]
    except KeyError:
        session[key_name] = keystat.copy()

    session[key_name]["released_count"] += 1


def remove_terminate_session_key(key: str) -> None:
    try:
        session[key]['pressed_count'] -= 1

        if session[key]['pressed_count'] == 0:
            dict.pop(session, key)
    except KeyError:
        pass


def write_to_output() -> None:
    print('Session ended')

    # Remove CTRL+C
    remove_terminate_session_key('ctrl')
    remove_terminate_session_key('c')

    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    with open(os.path.join('outputs', f'output-log-{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt'), 'w') as f:
        f.write(json.dumps(session))

    print(f'Wrote to outputs/output-log-{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt')


def main() -> None:
    print('Session started')

    try:
        with pynput.keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        write_to_output()


if __name__ == "__main__":
    main()

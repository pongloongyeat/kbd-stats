import keyboard
import os
from datetime import datetime


session = {}
keystat = {
    'down_count': 0,
    'up_count': 0
}


def log_event(event: keyboard.KeyboardEvent) -> None:
    key_name = event.name.lower() + ('_keypad' if event.is_keypad else '')

    try:
        session[key_name]['down_count']
    except KeyError:
        session[key_name] = keystat.copy()

    if event.event_type == keyboard.KEY_DOWN:
        session[key_name]['down_count'] += 1
    else:
        session[key_name]['up_count'] += 1


def remove_terminate_session_key(key: str):
    try:
        session[key]['down_count'] -= 1

        if session[key]['down_count'] == 0:
            dict.pop(session, key)
    except KeyError:
        pass


def write_to_output():
    print('Session ended')

    # Remove CTRL+C
    remove_terminate_session_key('ctrl')
    remove_terminate_session_key('c')

    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    with open(os.path.join('outputs', f'output-log-{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt'), 'w') as f:
        f.write(str(session))

    print(f'Wrote to outputs/output-log-{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt')


def main() -> None:
    keyboard.hook(log_event)

    print('Session started')

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        write_to_output()


if __name__ == "__main__":
    main()

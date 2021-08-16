# kbd-stats

A simple tool to record keypresses and how often you use certain keys.

## Usage

```bash
git clone https://github.com/pongloongyeat/kbd-stats.git && cd kbd-stats
python3 -m venv .venv
source .venv/bin/active     # macOS, Linux
# .\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python kbd-stats.py         # Use sudo for macOS and Linux
```

When the `Session started` pops up, you can go about your day/workday and end the session via <kbd>control</kbd> + <kbd>c</kbd>.

## Data structure

The output logfile holds the following data structure, formatted as a JSON dictionary.

```python
{
    "a": {
        "down_count": 240,
        "up_count": 240,
    },
    "right ctrl": {
        "down_count": 6,
        "up_count": 6,
    },
    "KEY_NAME": {
        "down_count": NUMBER_OF_TIMES_YOU_PRESSED_THE_KEY,
        "up_count": NUMBER_OF_TIMES_YOU_LIFTED_UP_THE_KEY,
    }
}
```

Looking at the raw data, this doesn't play nicely with the human brain, so take this file and parse it however you want. There are plans to make a report generator that displays a heatmap of the keypresses as a simple web page but that's a future plan.

### About

I made this to determine what keyboard layout to get for a new mechanical keyboard lol.

# Modding

## Overview

The Infinite Hallway supports mods! This makes the game *truly infinite*. (continue rest of modding overview here)

## Documentation

When developing a mod for The Infinite Hallway, you'll most likely use the following included functions.

- `functions/choices.py`
    - `two_options()` displays text, along with two options to the user. [Usage]()
    - `three_options()` displays text, along with three options to the user.
    - `four_options()` displays text, along with four options to the user.
- `functions/save.py`
    - `save()` saves provided data to save.json
    - `load()` loads required data from save.json
### Disclaimer
`save.display_stats()` has <u>**no**</u> modding support!
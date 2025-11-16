# Modding

## Overview

The Infinite Hallway supports mods! This makes the game *truly infinite*. (continue rest of modding overview here)

## Documentation

When developing a mod for The Infinite Hallway, you'll most likely use the following included functions.
- `functions/`
    - `choices.py`
        - `two_options()` displays text, along with two options to the user.
        - `three_options()` displays text, along with three options to the user.
        - `four_options()` displays text, along with four options to the user.
    - `save.py`
        - `save()` saves provided data to save.json
        - `load()` loads required data from save.json
    - `terminal.py`
        - `clear()` - clears the terminal with the respective command for each OS
        - `run()` - runs a command in the user's terminal (just os.system)
        - `printTraceback()` - generates a real traceback with a message of your choice, doesn't stop execution
        - `logTraceback()` - generates a real traceback with a message of your choice and writes it to `traceback.txt`, doesn't stop execution
        - `generateTraceback()` - generates a real traceback with a message of your choice, stops execution

### Disclaimer
`save.display_stats()` has <u>**no**</u> modding support!

### Usage
Each function has their own usage. If you're confused, see the example mod left in `/mods`

#### choices.py

`two_options()`:

```python
import functions.choices as cho

choice = cho.two_options("Question", "Answer One", "Answer Two")

if choice == "Answer One":
    print("You picked option one!")
elif choice == "Answer Two":
    print("You picked option two!")
```

`three_options()`:

```python
import functions.choices as cho

choice = cho.two_options("Question", "Answer One", "Answer Two", "Answer Three")

if choice == "Answer One":
    print("You picked option one!")
elif choice == "Answer Two":
    print("You picked option two!")
elif choice == "Answer Three":
    print("You picked option three!")
```

`four_options()`:

```python
import functions.choices as cho

choice = cho.two_options("Question", "Answer One", "Answer Two", "Answer Three", "Answer four")

if choice == "Answer One":
    print("You picked option one!")
elif choice == "Answer Two":
    print("You picked option two!")
elif choice == "Answer Three":
    print("You picked option three!")
elif choice == "Answer Four":
    print("You picked option four!")
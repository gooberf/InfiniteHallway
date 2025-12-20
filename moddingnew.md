# Modding

## Overview

The Infinite Hallway supports mods! This makes the game *truly infinite*. Mods allow you to create custom game experiences, new floors, alternative storylines, or completely different adventures using the same game engine and helper functions.

## File structure

- `/mods`
    - `/[modID]` (where [modID] is the ID of your mod, up to you to decide)
        - `main.py`
        - `info.json`
        - `splashes.txt` (optional)

## Pre-made Functions
The following list will contain a list of functions, as well as a short description of what they do.

- `/functions`
    - `choices.py` - all functions ask the user a question, the first question being the prompt, and the remainder being the answer choices
        - `choose_two()`
        - `choose_three()`
        - `choose_four()`
        - `list_options()` - same as the others, but takes a list for answer choices instead of strings for custom answer quantities, or dynamic choices.
    - `terminal.py`
        - `clear()` - clears the terminal
        - `run()` - runs a console command, which is a string passed in the arguments
        - `print_traceback()` - takes one argument, which is a string. A traceback message will be generated, this message being at the end. Execution isn't interrupted
        - `log_traceback()` - does the same as `print_traceback()`, but instead of printing, it puts the traceback in `traceback.txt`
    - `save.py`
       - `save()` - saves a Python dictionary as a JSON file
       - `load()` - loads `saves/save.json`, allowing you to put those values in variables or dictionaries

## Creaing a mod

Your mod requires **2** files to function. These files being:
- `main.py`
- `info.json`.

`main.py` will contain all code for your mod, using Python code and the functions provided above. `info.json` will contain information about your mod. **Both** of these files are required for your mod to function.
# Modding

## Overview

The Infinite Hallway supports mods! This makes the game *truly infinite*. Mods allow you to create custom game experiences, new floors, alternative storylines, or completely different adventures using the same game engine and helper functions.

Mods are Python files placed in the `/mods` directory. When you select "load mod" from the main menu, the game will scan the mods folder and let you choose which mod to run. Each mod must have a `main()` function that serves as the entry point for your mod.

## Documentation

When developing a mod for The Infinite Hallway, you'll most likely use the following included functions.
- `functions/`
    - `choices.py`
        - `two_options()` displays text, along with two options to the user.
        - `three_options()` displays text, along with three options to the user.
        - `four_options()` displays text, along with four options to the user.
        - `list_options()` displays text, along with a list of options from a Python list.
    - `save.py`
        - `save()` saves provided data to save.json
        - `load()` loads required data from save.json
    - `terminal.py`
        - `clear()` - clears the terminal with the respective command for each OS
        - `run()` - runs a command in the user's terminal (just os.system)
        - `print_traceback()` - generates a real traceback with a message of your choice, doesn't stop execution
        - `log_traceback()` - generates a real traceback with a message of your choice and writes it to `traceback.txt`, doesn't stop execution
    - `splash.py`
        - `displaySplash()` - displays a random splash text or a custom list of splash texts

## Creating a Mod

To create a mod for The Infinite Hallway:

1. **Create a Python file** in the `/mods` directory (e.g., `my_mod.py`)
2. **Define a `main()` function** - This is the entry point that will be called when your mod is loaded
3. **Import the functions you need** from the `functions/` directory
4. **Write your mod logic** using the available helper functions

### Basic Mod Structure

```python
import functions.choices as cho
import functions.terminal as term
import functions.save as save

def main():
    term.clear()
    print("Welcome to my mod!")
    
    choice = cho.two_options("What would you like to do?", "Explore", "Leave")
    
    if choice == "Explore":
        print("You begin exploring...")
        # Your mod logic here
    elif choice == "Leave":
        print("You decide to leave.")
```

### Mod Requirements

- **File location**: Must be placed in the `/mods` directory
- **File format**: Must be a `.py` file
- **Entry point**: Must have a `main()` function (no parameters)
- **Naming**: The filename (without `.py`) will be used as the mod name in the selection menu

### How Mods are Loaded

1. When you select "load mod" from the main menu, the game scans the `/mods` directory
2. All `.py` files in the directory are detected as potential mods
3. You'll be presented with a list of available mods to choose from
4. The selected mod is dynamically imported and its `main()` function is executed
5. The mod runs independently - when it finishes, you'll return to the terminal

**Note**: Mods run in the same Python environment as the main game, so they have access to all standard Python libraries and the game's function modules.

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

choice = cho.three_options("Question", "Answer One", "Answer Two", "Answer Three")

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

choice = cho.four_options("Question", "Answer One", "Answer Two", "Answer Three", "Answer Four")

if choice == "Answer One":
    print("You picked option one!")
elif choice == "Answer Two":
    print("You picked option two!")
elif choice == "Answer Three":
    print("You picked option three!")
elif choice == "Answer Four":
    print("You picked option four!")
```

`list_options()`:

```python
import functions.choices as cho

items = ["Sword", "Shield", "Potion", "Key", "Map"]
choice = cho.list_options("Which item do you want?", items)

print(f"You selected: {choice}")
```

**Note**: `list_options()` accepts a list of strings and allows the player to choose from any number of options. The function returns the exact string from the list that matches the player's input (case-insensitive).

#### save.py

`save()` (modified example from floor_one.py):

```python
import functions.save as save

inventory = ["Rusted Axe", "Key"]
bought_key = True
door_open = True

saveData = {}

saveData['inventory'] = inventory
saveData['bought_key'] = bought_key
saveData['door_open'] = door_open

save.save(saveData)
```

`load()` (modified example from floor_one.py):

```python
import functions.save as save

saveData = save.load()

inventory = saveData['inventory']
bought_key = saveData['bought_key']
door_open = saveData['door_open']
```

#### terminal.py

`clear()`:

```python
import functions.terminal as term

term.clear()
```

`run()`:

```python
import functions.terminal as term

term.run("echo \"hackr was here\"")
```

`print_traceback()`:

```python
import functions.terminal as term

message = "The message you want to display at the end of your traceback."
term.print_traceback(message)
```

`log_traceback()`:

```python
import functions.terminal as term

message = "The message you want to display at the end of your traceback."
term.log_traceback(message)
```

Output (traceback.txt):

```
I'm sorry, but an uncaught exception occured!

Traceback (most recent call last):
  File "c:\Users\hackr\InfiniteHallway-1\functions\terminal.py", line 31, in logTraceback
    try:genTraceback(msg)
        ~~~~~~~~~~~~^^^^^
  File "c:\Users\hackr\InfiniteHallway-1\functions\terminal.py", line 20, in genTraceback
    raise ValueError(msg)
ValueError: The message you want to display at the end of your traceback.
```

## Best Practices

### Save Data Management

When working with save data in mods:

- **Use unique keys**: Prefix your save data keys with your mod name to avoid conflicts with the main game or other mods
- **Check for existing data**: Always check if keys exist before accessing them
- **Handle missing saves**: Use `save.load()` which returns default values if the save file doesn't exist

Example:

```python
import functions.save as save

saveData = save.load()

# Use mod-specific keys
mod_inventory = saveData.get('my_mod_inventory', [])
mod_progress = saveData.get('my_mod_progress', 0)

# Update and save
saveData['my_mod_inventory'] = mod_inventory
saveData['my_mod_progress'] = mod_progress
save.save(saveData)
```

### Error Handling

- Use `term.print_traceback()` for debugging during development
- Use `term.log_traceback()` to log errors to a file for users to report
- Always handle potential errors when loading save data or accessing files

### User Experience

- Use `term.clear()` to keep the terminal clean between scenes
- Use `time.sleep()` (imported from the standard library) to add pacing to your story
- Provide clear, descriptive option text in choice functions
- Consider using `splash.displaySplash()` for an engaging intro

### Code Organization

- Keep your mod logic organized in functions
- Use descriptive variable names
- Comment complex logic
- Follow the example mod structure for consistency

## Example Mod Walkthrough

Here's a complete example mod that demonstrates common patterns:

```python
import functions.choices as cho
import functions.terminal as term
import functions.save as save
import functions.splash as splash
import time

def main():
    # Display intro splash
    custom_splashes = [
        "Welcome to the Example Adventure!",
        "Your journey begins now...",
        "Prepare yourself!"
    ]
    splash.displaySplash(custom_splashes)
    
    # Load or initialize save data
    saveData = save.load()
    mod_inventory = saveData.get('example_mod_inventory', [])
    mod_visited = saveData.get('example_mod_visited', False)
    
    term.clear()
    print("You find yourself in a mysterious room.")
    time.sleep(1)
    
    if not mod_visited:
        print("This is your first time here.")
    else:
        print("You've been here before.")
    
    # First choice
    choice1 = cho.two_options(
        "What do you do?",
        "Examine the room",
        "Leave immediately"
    )
    
    if choice1 == "Examine the room":
        print("You find a glowing key on the floor.")
        mod_inventory.append("Glowing Key")
        
        # Second choice
        choice2 = cho.three_options(
            "What next?",
            "Take the key",
            "Leave it",
            "Examine the key closer"
        )
        
        if choice2 == "Take the key":
            print("You pick up the key. It feels warm to the touch.")
        elif choice2 == "Leave it":
            print("You decide to leave the key where it is.")
            mod_inventory.remove("Glowing Key")
        else:
            print("The key seems to pulse with an inner light.")
    
    # Save progress
    saveData['example_mod_inventory'] = mod_inventory
    saveData['example_mod_visited'] = True
    save.save(saveData)
    
    print("\nYour adventure ends here... for now.")
    time.sleep(2)
```

## Troubleshooting

### My mod doesn't appear in the list

- Ensure your file is in the `/mods` directory
- Check that the file has a `.py` extension
- Verify the file is not a directory (subdirectories are ignored)

### "Error loading or running mod"

- Make sure your mod has a `main()` function defined
- Check for syntax errors in your Python code
- Ensure all imports are correct (use `functions.choices`, not `choices`)
- Verify that you're not using any game-specific functions that aren't documented

### Save data conflicts

- Use unique key prefixes for your mod's save data
- Always use `.get()` with default values when reading save data
- Don't overwrite keys used by the main game (like `inventory`, `bought_key`, etc.)

### Import errors

- Make sure you're importing from `functions.` (e.g., `functions.choices`, not just `choices`)
- The game must be run from the project root directory for imports to work correctly

## Additional Resources

- Check `/mods/example.py` for a working example mod
- Look at `/floors/floor_one.py` for examples of how the main game uses these functions
- Review the function source code in `/functions/` for detailed implementation details

## Contributing Mods

If you create an interesting mod, consider sharing it with the community! Mods can extend The Infinite Hallway in creative ways, from new storylines to mini-games to completely different game experiences.

Happy modding!

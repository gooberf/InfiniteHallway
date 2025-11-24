# Infinite Hallway

A small, playful text-adventure / learning project written in Python. It was created as an interactive way to explore basic Python concepts and to practice reading and modifying a simple codebase.

## Features

- Simple, file-based Python game with modular code under `floors/` and `functions/`.
- Lightweight and easy to run locally with a standard Python 3 interpreter.
- **Optional** Ollama LLM integration for AI-enhanced responses [(learn how to set up)](#llm-setup)
- Color-coded terminal output with colorama
- Interactive choice system with 2, 3, 4-option, and list-based menus
- Persistent configuration system for game preferences
- Save/load system for game progress
- Modding support - create custom floors and adventures
- Playtime tracking
- Splash screen system for engaging introductions

## Quick start

1. Make sure you have Python 3.8+ installed. Verify with:

	```bash
	python --version
	```

2. From the repository root, run the startup script (recommended):

	```bash
	python start.py
	```

	Alternatively, you can run the main script directly:

	```bash
	python main.py
	```

	The `start.py` script will automatically check for dependencies and verify all required files before launching the game.

3. Follow the on-screen prompts to play.

If your environment uses a different python launcher (for example `python3`), use that instead.

## Installation

### Dependencies

The game requires the following Python packages:
- `colorama` - for color-coded terminal output
- `ollama` - for optional AI features
- `rich` - for enhanced error handling and tracebacks

### Installing Dependencies

**Option 1: Using the provided script (Windows)**
- Run `tools/install_dependancies.bat`

**Option 2: Using pip**
```bash
pip install -r requirements.txt
```

**Option 3: Manual installation**
```bash
pip install colorama ollama rich
```

The `start.py` script will automatically detect missing dependencies and offer to install them for you.

## LLM Setup

The game supports optional AI-enhanced responses using Ollama. This feature is completely optional and the game works perfectly without it.

1. Download and install [Ollama](https://ollama.com)
2. Ensure Ollama is running when starting the game
3. When prompted, choose to enable LLM features
4. Enter the Ollama model you'd like to use (default: `llama2`)

The game will test the connection and offer to pull the model if it's not already installed.

### Revert LLM Choice

If you want to be asked again whether or not to enable LLMs, you can:
- Delete the `LLMsEnabled` file in `/config`, or
- Select "reset config" from the main menu

## Project layout

- `start.py` - **Recommended entry point** - checks dependencies and verifies files before launching
- `main.py` - main game entry point; handles LLM setup and main menu flow
- `Infinite Hall.py` - older copy / alternate entry (inspect before running)
- `floors/` - game floor scripts
  - `floor_one.py` - script for the first floor
  - `floor_two.py` - script for the second floor
- `functions/` - helper modules:
  - `choices.py` - interactive menu system (2, 3, 4-option, and list-based choices)
  - `terminal.py` - cross-platform terminal utilities (clear, run commands, traceback handling)
  - `deleteConfig.py` - configuration cleanup utilities
  - `easyMode.py` - activates the (totally real) easy mode
  - `save.py` - save/load system for game progress
  - `splash.py` - splash screen display system
  - `playtimetracker.py` - tracks playtime statistics
- `config/` - persistent configuration storage (auto-created on first run)
  - `LLMsEnabled` - tracks LLM enablement status
  - `model` - stores the selected Ollama model name
  - `easyMode` - tracks easy mode status
  - `quickStart` - tracks quick start preference
- `saves/` - persistent save data storage
  - `save.json` - your save file
- `mods/` - custom mods directory
  - Place `.py` files here to create custom game experiences
  - See [modding.md](modding.md) for detailed modding documentation
- `tools/`
  - `install_dependancies.bat` - installs Python packages required for the game to run (Windows)
###### btw we are not liable for any storage space that is taken up. the easy mode is a lie. you have been warned
###### you brought this on yourself if you accept easy_mode

## Modding

The Infinite Hallway supports mods! Create custom floors, alternative storylines, or completely different adventures. See [modding.md](modding.md) for comprehensive documentation on creating mods.

Quick modding overview:
- Place Python files in the `/mods` directory
- Each mod must have a `main()` function as the entry point
- Use functions from `functions/` for choices, terminal operations, saving, etc.
- Check `/mods/example.py` for a working example

## Main Menu Options

- **Start** - Begin a new game or continue your adventure
- **Reset Config** - Delete all configuration files and start fresh
- **Load Mod** - Select and run a custom mod from the `/mods` directory
- **Dev Tools** - Development utilities (start at specific floors, etc.)

## Configuration

The game stores configuration in the `/config` directory:
- `LLMsEnabled` - Whether AI features are enabled
- `model` - The Ollama model to use
- `easyMode` - Easy mode status
- `quickStart` - Whether to skip setup prompts

You can reset all configuration by selecting "reset config" from the main menu.

## Contributing

This is a small, informal project — contributions and experiments are welcome.

- Run the game and explore how functions in `functions/choices.py` and the files under `floors/` work.
- Add small features or refactor to make code clearer. Please keep changes focused and provide short commit messages.
- Create mods to extend the game in creative ways!

## Disclaimer

⚠️ **Easy Mode Warning**: We are not liable for any storage space that is taken up. The easy mode is a lie. You have been warned. You brought this on yourself if you accept easy_mode.

## License

This repository does not include a license file. If you plan to share or publish, add a LICENSE that matches how you want others to use your code.

Enjoy exploring the Infinite Hallway!


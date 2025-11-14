# Infinite Hallway

A small, playful text-adventure / learning project written in Python. It was created as an interactive way to explore basic Python concepts and to practice reading and modifying a simple codebase.

## Features

- Simple, file-based Python game with modular code under `floors/` and `functions/`.
- Lightweight and easy to run locally with a standard Python 3 interpreter.
- **Optional** Ollama LLM integration for AI-enhanced responses [(learn how to set up)](#llm-setup)
- Color-coded terminal output with colorama
- Interactive choice system with 2, 3, and 4-option menus
- Persistent configuration system for game preferences

## Quick start

1. Make sure you have Python 3.8+ installed. Verify with:

	python --version

2. From the repository root, run the main script:

	python main.py

3. Follow the on-screen prompts to play.

If your environment uses a different python launcher (for example `python3`), use that instead.

## LLM Setup
⚠️ **Note**: LLM functionality is currently not yet implemented. The setup prompts will work, but LLM responses will not be used in the game.

1. Download [Ollama](https://ollama.com)
2. Ensure Ollama is running when starting `main.py`

### Revert LLM Choice
If you want to be asked again whether or not to enable LLMs, delete the `LLMsEnabled` file in the root of the project

## Project layout

- `main.py` - entry point for running the game; handles LLM setup and main menu flow.
- `Infinite Hall.py` - (older copy / alternate entry; inspect before running).
- `floors/` - modules that define game floors/rooms, e.g. `floor_one.py`, `floor_two.py`.
- `functions/` - helper modules:
  - `choices.py` - interactive menu system (2, 3, and 4-option choices)
  - `clear_terminal.py` - cross-platform terminal clearing
  - `deleteConfig.py` - configuration cleanup utilities
- `config/` - persistent configuration storage (auto-created on first run)
  - `LLMsEnabled` - tracks LLM enablement status
  - `model` - stores the selected Ollama model name
- `data/` - persistent data storage (including saves)
  - `save.json` - your save file
###### btw we are not liable for any storage space that is taken up. the easy mode is a lie. you have been warned
 - you brought this on yourself if you accept easy_mode.
## Contributing

This is a small, informal project — contributions and experiments are welcome.

- Run the game and explore how functions in `functions/choices.py` and the files under `floors/` work.
- Add small features or refactor to make code clearer. Please keep changes focused and provide short commit messages.


## License

This repository does not include a license file. If you plan to share or publish, add a LICENSE that matches how you want others to use your code.

Enjoy exploring the Infinite Hallway!


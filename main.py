import functions.choices as choose
import floors.floor_one as f1
import functions.invHelper.invHelper as invHelper
import os

bad_time_starter = choose.two_options("Want to have a bad time?", "yes", "no", "chose yes", "chose no")

if bad_time_starter == "yes":
    invHelper.invHelper()
else:
    pass


if not os.path.exists("LLMsEnabled"):
    enableLLMs = choose.two_options("Want to enable LLMs? These can be used to talk to NPCs. Performance varies based on your hardware. Check the README for more information.", "yes", "no", "chose yes", "chose no")
    if enableLLMs == "yes":
        print("LLMs enabled.")
        with open("LLMsEnabled", "w") as file:
            file.write("1")
    else:
        print("LLMs disabled")


inventory = f1.floor_one()

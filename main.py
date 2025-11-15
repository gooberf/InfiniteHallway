import functions.choices as choose
import os
import ollama
import time
import functions.deleteConfig as delConfig
import floors.floor_two as f2

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

if os.path.exists("config") == False:
    os.mkdir("config")

if not os.path.exists("config/LLMsEnabled"):
    ai_option = choose.two_options("Would you like to enable the usage of Ollama for AI responses?", "yes", "no")

    if ai_option == "yes":
        model = input("Please enter the Ollama model you would like to use (default: llama2): ")
        if model.strip() == "":
            model = "llama2"
        with open("config/model", "w") as mf:
            mf.write(model)
        try:
            response = ollama.chat(model=model, messages=[{'role': 'user', 'content': 'Hello!'}])
            with open("config/LLMsEnabled", "w") as f:
                f.write("1")
            print("Ollama is running correctly! AI features enabled.")
        except Exception as e:
            print(f"There was an issue connecting to Ollama: {e}")
            rePull = choose.two_options("Would you like to attempt to pull the model?\nWarning: This will download >1GB of data.", "yes", "no")
            if rePull == "yes":
                try:
                    os.system(f"ollama pull {model}")
                    print("Model pulled successfully! Attempting test again.")
                    try:
                        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': 'Hello!'}])
                        with open("config/LLMsEnabled", "w") as f:
                            f.write("1")
                        print("Ollama is running correctly! AI features enabled.")
                    except Exception as e:
                        print(f"Failed to connect to Ollama after pulling the model: {e}")
                        with open("config/LLMsEnabled", "w") as f:
                            f.write("0")
                except Exception as e:
                    print(f"Failed to pull the model: {e}")
                    with open("config/LLMsEnabled", "w") as f:
                        f.write("0")
            else:
                with open("config/LLMsEnabled", "w") as f:
                    f.write("0")
    else:
        with open("config/LLMsEnabled", "w") as f:
            f.write("0")

if os.path.exists("config/LLMsEnabled"):
    with open("config/LLMsEnabled", "r") as f:
        status = f.read().strip()
    if status == "1":
        print("Testing Ollama connection...")
        with open("config/model", "r") as mf:
            model = mf.read().strip()
        try:
            test_response = ollama.chat(model=model, messages=[{'role': 'user', 'content': 'Hello!'}])
            print("Ollama is connected and ready to use AI features.")
        except Exception as e:
            print(f"Failed to connect to Ollama: {e}")
            delConfirm = choose.two_options("Would you like to delete all LLM related data, or, keep it?", "delete","keep")
            if delConfirm == "delete":
                os.remove("config/LLMsEnabled")
                os.remove("config/model")
                print("LLM configuration deleted. Please restart the program to set up again.")
                exit()
            else:
                print("Keeping existing configuration. Exiting...")
                exit()
    else:
        print("Ollama AI features are disabled.\nYou can change this by selecting 'reset config' in the main menu.")

time.sleep(2)

mainMenuOption = choose.two_options("main menu placeholder", "start", "reset config")
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
if mainMenuOption == "start":
    import floors.floor_one as f1
    inventory = f1.floor_one()
    inventory = f2.floor_two(inventory)
elif mainMenuOption == "reset config":
    delConfig.delete_config()
    print("Please restart the program to set up configuration again.")
    exit()



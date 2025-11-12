import functions.choices as choose
import floors.floor_one as f1
import os
import ollama
import time

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
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
time.sleep(2)


inventory = f1.floor_one()

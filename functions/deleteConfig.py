import os

def delete_config():
    if os.path.exists("config"):
        configFiles = os.listdir("config")
        for file in configFiles:
            os.remove(os.path.join("config", file))
        os.removedirs("config")
    print("all config data deleted.")
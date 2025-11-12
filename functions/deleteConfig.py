import os

def delete_config():
    if os.path.exists("config"):
        os.removedirs("config")
    print("all config data deleted.")
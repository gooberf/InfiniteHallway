from time import sleep

def typewrite(string: str, speed=0.05):
    for char in string:
        print(char, end="", flush=True)
        sleep(speed)
    print() 

# from pynput.keyboard import Key, Listener
import os

# key = []

try:
    while 1 == 1:
        answer = input("Write your reply here: " + "\n")
        print("Your answer is: "+answer + "\n")
        # answer = answer.clear()
        # os.system('cls' if os.name == 'nt' else 'clear')
        answer = input()
        print("Your answer is: " + answer + "\n")
        # print("Write your reply here: " + "\n")

except KeyboardInterrupt:
    "ctrl + c"
    pass

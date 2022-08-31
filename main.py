# from pynput.keyboard import Key, Listener
import os

# key = []
print("\n"+"Python Messenger has been initialized!")
try:
    while True:
        answer = input(
            "\n"+"write down your answer/question below and press enter to continue: " + "\n")
        print("Your answer is: "+answer + "\n")
        print("write down your answer/question below and press enter to continue: ")
        # answer = answer.clear()
        # os.system('cls' if os.name == 'nt' else 'clear')
        answer = input()
        print("Your answer is: " + answer + "\n")
        # print("Write your reply here: " + "\n")

except KeyboardInterrupt:
    pass
'''CTRL + C to_exit_program'''

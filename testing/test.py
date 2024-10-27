import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.waiting_animation import *
from src.theme import Theme
from src.change_attributes import *

def check_paths():
    if get_komorebi_path():
        print("Komorebi path exists")
    else:
        print("Komorebi path does not exist")

    if get_yasb_path():
        print("Yasb path exists")
    else:
        print("Yasb path does not exist")

    if get_vscode_path():
        print("VSCode path exists")
    else:
        print("VSCode path does not exist")


if __name__ == "__main__":

    while True:
        user_input = input("Test Available Paths:1\nTest Json and Css Edit:2\nExit:3\n")
        if user_input == "1":
            print("Checking paths\n")
            waiting_animation(5)
            check_paths()
            time.sleep(3)

        elif user_input == "2":
            print("Checking json and css edit\n")
            waiting_animation(2)
            change_json("testing/test.json", "theme", "blue")
            waiting_animation(2)
            change_css("testing/test.css", "#4CAF50", "#FF5733")
            waiting_animation(2)
        elif user_input == "3":
            break
        else:
            print("Invalid input")
            continue
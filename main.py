from src.theme import Theme
from src.get_path import *

available_themes = ["blue", "green", "red", "yellow"]

if __name__ == "__main__":
    chosen_them = input("Choose a theme: ")

    if chosen_them not in available_themes:
        print("Invalid theme")
    else:
        if chosen_them == "blue":
            theme = Theme("#0000FF", "#00FFFF", "#0000FF")
        elif chosen_them == "green":
            theme = Theme("#008000", "#00FF00", "#008000")
        elif chosen_them == "red":
            theme = Theme("#FF0000", "#FF0000", "#FF0000")
        elif chosen_them == "yellow":
            theme = Theme("#FFFF00", "#FFFF00", "#FFFF00")
        else:
            print("Invalid theme")

        print(theme.get_main_color())
        print(theme.get_secondary_color())
        print(theme.get_third_color())
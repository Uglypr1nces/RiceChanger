from src.theme import Theme
from src.get_path import *
from src.change_attributes import *
from utils.waiting_animation import *
from utils.variables import *

import subprocess

available_themes = [
    "Dynamic Media Player",
    "Red-Blue Audio Visualizer",
    "Dark Blue with Red Accents",
    "Rainy Japanese Nature",
    "Cloudy 2b2t Sky",
    "Time-Sensitive Anime Cutie"
]

wallpaper_paths = [
    # Wallpaper 1, a wallpaper that changes based on playing content
    "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/2938612768/project.json",
    # Wallpaper 2, a red,blue wallpaper with audio visualizer
    "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/1556245028/project.json"
    # Wallpaper 3, a dark blue mixed with a little red wallpaper
    "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/3265653261/project.json"
    # Wallpaper 4, a rainy nature/japanese wallpaper
    "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/3174556087/project.json"
    # Wallpaper 5, a cloudy white 2b2t wallpaper
    "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/3243968974/project.json"
    # Wallpaper 6, a cute anime wallpaper that adjusts to the time of day
    "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/1551961057project.json"
]

if __name__ == "__main__":
    css = yasb_css
    chosen_them = input("Choose a theme: ")

    if int(chosen_them) not in range(1, 7):
        print("Invalid theme")
    else:
        if chosen_them == "1":
            theme = Theme("#ffffff", "#1b1919", "#1b1919", 2938612768)
        elif chosen_them == "2":
            theme = Theme("#ac1b46", "#222c58", "#202122", 1556245028)
        elif chosen_them == "3":
            theme = Theme("#222c58", "#1c1c1f", "#a32354", 3265653261)
        elif chosen_them == "4":
            theme = Theme("#574408", "#237aa3", "#237aa3", 3174556087)
        elif chosen_them == "5":
            theme = Theme("#b8b6b6", "#4f5152", "#000000", 3243968974)
        elif chosen_them == "6":
            theme = Theme("#377edb", "#152e74", "#000000", 1551961057)
        else:
            print("Invalid theme")

        # Replace the placeholders with actual values
        new_css = css.replace("main_color", theme.get_main_color())
        new_css = new_css.replace("secondary_color", theme.get_yasb_color())


        change_advanced_json(get_komorebi_path(), "border_colours.single", theme.get_main_color())
        change_advanced_json(get_komorebi_path(), "border_colours.unfocused", theme.get_komorebi_color())
        change_json(get_vscode_path(), "workbench.colorTheme", theme.get_vs_code_theme())
        change_css(get_yasb_path(), new_css)
        change_wallpaper_engine("src/wallpaper_id.txt", str(theme.get_wallpaper_id()))
        batch_file_path = os.path.join("src", "change_wallpaper.bat")
        subprocess.call(batch_file_path, shell=True)
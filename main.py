from src.theme import Theme
from src.get_path import *
from src.change_attributes import *
from utils.waiting_animation import *
from utils.variables import *

import subprocess


if __name__ == "__main__":
    css = yasb_css
    chosen_theme = input("Choose a theme: ")

    if int(chosen_theme) not in range(1, 7):
        print("Invalid theme")
    else:
        if chosen_theme == "1":
            theme = Theme("#ffffff", "#1b1919", "#1b1919", 2938612768)
        elif chosen_theme == "2":
            theme = Theme("#ac1b46", "#222c58", "#202122", 1556245028)
        elif chosen_theme == "3":
            theme = Theme("#222c58", "#1c1c1f", "#a32354", 3265653261)
        elif chosen_theme == "4":
            theme = Theme("#574408", "#237aa3", "#237aa3", 3174556087)
        elif chosen_theme == "5":
            theme = Theme("#b8b6b6", "#4f5152", "#000000", 3243968974)
        elif chosen_theme == "6":
            theme = Theme("#377edb", "#152e74", "#000000", 1551961057)
        else:
            print("Invalid theme")

        # Replace the placeholders with actual values
        new_css = css.replace("main_color", theme.get_main_color())
        new_css = new_css.replace("secondary_color", theme.get_yasb_color())


        change_advanced_json(get_komorebi_path(), "border_colours.single", theme.get_main_color())
        change_advanced_json(get_komorebi_path(), "border_colours.unfocused", theme.get_komorebi_color())
        change_vs_code_json(get_vscode_path(), "workbench.colorTheme", vs_code_themes[int(chosen_theme) - 1])
        change_css(get_yasb_path(), new_css)
        change_wallpaper_engine("src/wallpaper_id.txt", str(theme.get_wallpaper_id()))
        batch_file_path = os.path.join("src", "change_wallpaper.bat")
        subprocess.call(batch_file_path, shell=True)
from src.theme import Theme
from src.get_path import *
from src.change_attributes import *
from src.theme_manager import *
from utils.waiting_animation import *
from utils.variables import *

dynamic_theme = Theme("#ffffff", "#1b1919", "#1b1919", 2938612768, "nature")
dynamic_theme2 = Theme("#098af3", "#0a5274", "#000000", 3163060610, "One Dark Pro") 
dynamic_theme3 = Theme("#c00505", "#464646", "#000000", 2955378002, "nature") 
dynamic_day_theme = Theme("#377edb", "#152e74", "#000000", 1551961057, "Community Material Theme Lighter")
day_white_theme = Theme("#c00505", "#ffffff", "#ffffff", 2440387496, "Monokai Pro Light") 
orange_blue_theme = Theme("#f3a109", "#237aa3", "#237aa3", 3298178668, "Grey-Blueish Orange Theme")
red_blue_theme = Theme("#ac1b46", "#222c58", "#202122", 1556245028, "Red")
night_blue_theme = Theme("#222c58", "#1c1c1f", "#a32354", 3265653261 , "Community Material Theme Ocean")
night_nature_theme = Theme("#574408", "#237aa3", "#237aa3", 3174556087,"Muted Nature (Dark)")
day_cloudy_theme = Theme("#b8b6b6", "#4f5152", "#000000", 3243968974, "Community Material Theme Darker")

themes = [dynamic_theme, dynamic_theme2, dynamic_theme3, dynamic_day_theme, day_white_theme, orange_blue_theme, red_blue_theme, night_blue_theme, night_nature_theme, day_cloudy_theme]


if __name__ == "__main__":
    chosen_theme = input("Choose a theme: ")

    if int(chosen_theme) not in range(1, 7):
        print("Invalid theme")
    else:
        apply_theme(themes[int(chosen_theme) - 1])
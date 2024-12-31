from src.theme import Theme
from src.get_path import *
from src.change_attributes import *
from src.theme_manager import *
from utils.waiting_animation import *
from utils.variables import *
from time import sleep

dynamic_theme1 = Theme("#ffffff", "#1b1919", "#1b1919", 2938612768, "nature", "Dynamic Theme")
dynamic_theme2 = Theme("#098af3", "#0a5274", "#000000", 3163060610, "One Dark Pro", "Dynamic Theme 2") 
dynamic_theme3 = Theme("#098af3", "#0a5274", "#000000", 2911866381, "One Dark Pro", "Dynamic Theme 3") 
dynamic_theme4 = Theme("#098af3", "#0a5274", "#000000", 3262885320, "One Dark Pro", "Dynamic Theme 4") 
dynamic_theme5 = Theme("#098af3", "#0a5274", "#000000", 3323544626, "One Dark Pro", "Dynamic Theme 5") 
dynamic_theme6 = Theme("#c00505", "#464646", "#000000", 2955378002, "nature", "Dynamic Theme 6") 

dynamic_day_theme = Theme("#377edb", "#152e74", "#000000", 1551961057, "Community Material Theme Lighter", "Dynamic Day Theme")
dynamic_day_theme1 = Theme("#377edb", "#152e74", "#000000", 3265468347, "Community Material Theme Lighter", "Dynamic Day Theme1")
dynamic_day_theme2 = Theme("#377edb", "#152e74", "#000000", 3236099158, "Community Material Theme Lighter", "Dynamic Day Theme2")
dynamic_day_theme3 = Theme("#377edb", "#152e74", "#000000", 3364579588, "Community Material Theme Lighter", "Dynamic Day Theme3")

day_white_theme = Theme("#c00505", "#ffffff", "#ffffff", 2440387496, "Monokai Pro Light", "Day White Theme") 
orange_blue_theme = Theme("#f3a109", "#237aa3", "#237aa3", 3298178668, "Grey-Blueish Orange Theme", "Orange Blue Theme")
red_blue_theme = Theme("#ac1b46", "#222c58", "#202122", 1556245028, "Red", "Red Blue Theme")
night_blue_theme = Theme("#222c58", "#1c1c1f", "#a32354", 3265653261 , "Community Material Theme Ocean", "Night Blue Theme")
night_nature_theme = Theme("#574408", "#237aa3", "#237aa3", 3174556087,"Muted Nature (Dark)", "Night Nature Theme")
day_cloudy_theme = Theme("#b8b6b6", "#4f5152", "#000000", 3243968974, "Community Material Theme Darker", "Day Cloudy Theme")

themes = [dynamic_theme1,
dynamic_theme2,
dynamic_theme3,
dynamic_theme4,
dynamic_theme5,
dynamic_theme6,
dynamic_day_theme,
dynamic_day_theme1,
dynamic_day_theme2,
dynamic_day_theme3,
 day_white_theme,
 orange_blue_theme,
 red_blue_theme,
 night_blue_theme,
 night_nature_theme,
 day_cloudy_theme]


if __name__ == "__main__":    
    print("Available themes: ")
    print("\n")   

    for theme in themes:
        sleep(0.3)
        print(theme.get_theme_name()) 

    print("\n")   
    chosen_theme = input("Choose a theme: ")

    if int(chosen_theme) not in range(1, len(themes) + 1):
        print("Invalid theme")
    else:
        apply_theme(themes[int(chosen_theme) - 1])
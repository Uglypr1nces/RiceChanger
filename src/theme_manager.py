from src.theme import Theme
from src.get_path import *
from src.change_attributes import *
from utils.waiting_animation import *
from utils.variables import *

import subprocess

def apply_theme(Theme):
    # Replace the placeholders with actual values
    new_css = yasb_css.replace("main_color", Theme.get_main_color())
    new_css = new_css.replace("secondary_color", Theme.get_yasb_color())

    change_advanced_json(get_komorebi_path(), "border_colours.single", Theme.get_main_color())
    change_advanced_json(get_komorebi_path(), "border_colours.unfocused", Theme.get_komorebi_color())
    change_vs_code_json(get_vscode_path(), "workbench.colorTheme", Theme.get_vs_code_theme())
    change_css(get_yasb_path(), new_css)
    change_wallpaper_engine("src/wallpaper_id.txt", str(Theme.get_wallpaper_id()))
    batch_file_path = "src"
    subprocess.call(os.path.join(batch_file_path,"change_wallpaper.bat"), shell=True)
class Theme:
    def __init__(self, main_color, komorebi_color, yasb_color, wallpaper_id):
        self.main_color = main_color
        self.komorebi_color = komorebi_color
        self.yasb_color = yasb_color
        self.wallpaper_id = wallpaper_id

    def get_main_color(self):
        return self.main_color

    def get_komorebi_color(self):
        return self.komorebi_color

    def get_yasb_color(self): 
        return self.yasb_color

    def get_wallpaper_id(self):
        return self.wallpaper_id

    def get_vs_code_theme(self):
        if self.main_color == "#0000FF":
            return "Quiet Light"

        if self.main_color == "#FFFFFF":
            return "Night Owl Light"
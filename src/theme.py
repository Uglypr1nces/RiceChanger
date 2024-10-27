class Theme:
    def __init__(self, main_color, secondary_color=None, third_color=None):
        self.main_color = main_color
        self.secondary_color = secondary_color
        self.third_color = third_color

    def get_main_color(self):
        return self.main_color

    def get_secondary_color(self):
        return self.secondary_color

    def get_third_color(self): 
        return self.third_color
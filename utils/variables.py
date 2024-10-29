yasb_css = """
* {
        font-family: 'JetBrainsMonoNL Nerd Font';
        font-size: 13px;
    }
    
    .bar {
        padding-right: 1px;
    }
    
    .bar .widget {
        background: main_color;
        border-radius: 5px;
        margin-left: 5px;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    
    .bar .widget .label {
        color: secondary_color;
        font-weight: bold;
    }
    
    .bar .widget:hover {
        background: #7c2525;
    }
    
    .label {
        padding: 2px 5px;
        border-radius: 5px;
    }
    
    
    
    .media-widget .thumbnail {
    
    }
    
    .media-widget .label {
        padding: 0px 0px 0px 0px;
        margin: 0px 0px 0px 0px;
    }
    
    .media-btn {
        color: #242424;
        padding-right: 5px;
        padding-left: 5px;
        font-weight: bold;
    
    }
    
    .media-btn {
        background: transparent;
    }
    
    .media-btn:hover {
        color: #656766;
    }
    
    .media-btn.shuffle.active {}
    
    
    .ws-btn:hover {
        background: #fbf1c7;
    }
    
    .komorebi-workspaces {
        padding: 0 6px
    }
    .komorebi-workspaces .ws-btn {
        border-radius: 6px;
        width: 12px;
        height: 12px;
        padding: 0;
        margin: 0 3px;
        background-color: #605f5f;
    }
    .komorebi-workspaces .ws-btn.active {
        background-color: #2e2c2c;
        width: 28px;
    }
    
    .battery-widget .label.status-full,
    .battery-widget .label.status-charging {
        color: #5f924d;
    }
    
    .battery-widget .label.status-critical {
        color: #d15142;
    }
    
    .battery-widget .label.status-low {
        color: #df8a45;
    }
    
    .battery-widget .label.status-medium {
        color: #e2b345;
    }
    
    .battery-widget .label.status-high {
        color: #b7b85a;
    }
    
    
    .dropdown-button {
        color: #242424;
        width: 30px;
        border-radius: 5px;
    
    }
    
    .dropdown-button::menu-indicator {
        height: 0;
        width: 5px;
    }
"""

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

vs_code_themes = [
    # Theme 1, dark theme
    "nature",
    # Theme 2, red theme
    "Red",
    # Theme 3, a dark blue theme
    "Community Material Theme Ocean",
    # Theme 4, nature theme
    "Muted Nature (Dark)",
    # Theme 5, a dark theme with a white main color
    "Community Material Theme Darker",
    # Theme 6, a white theme
    "Community Material Theme Lighter"
]
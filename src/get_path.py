import os

def get_user_name():
    return os.getlogin()

def get_komorebi_path():
    file_path = f"C:/Users/{get_user_name()}/.config/komorebi.json"
    if os.path.exists(file_path):
        return file_path
    else:
        return None

def get_yasb_path():
    file_path = f"C:/Users/{get_user_name()}/.yasb/styles.css"
    if os.path.exists(file_path):
        return file_path
    else:
        return None

def get_vscode_path():
    file_path = f"C:/Users/{get_user_name()}/AppData/Roaming/Code/User/settings.json"
    if os.path.exists(file_path):
        return file_path
    else:
        return None

        
def get_vencord_path():
    pass


if __name__ == "__main__":
    print("This is get_path.py")
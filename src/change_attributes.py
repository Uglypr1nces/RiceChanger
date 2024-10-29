import json

def change_json(path, key, value):
    try:
        with open(path, "r") as f:
            data = json.load(f)

        data[key] = value

        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print("Json edited successfully")
    except Exception as e:
        print(e)

def change_advanced_json(path, nested_key, value):
    try:
        # Open the JSON file and load the data
        with open(path, "r") as f:
            data = json.load(f)
        
        # Navigate to the nested key and change its value
        keys = nested_key.split('.')
        temp = data
        for key in keys[:-1]:  # Traverse to the second last key
            temp = temp[key]
        
        temp[keys[-1]] = value  # Update the last key with the new value

        # Write back to the file
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        
        print("Json edited successfully")
    except Exception as e:
        print(e)

def change_css(path, new_value):
    try:
        with open(path, "w") as f:
            f.write(new_value)
        print("CSS edited successfully")
    except Exception as e:
        print(e)

def change_wallpaper_engine(path, wallpaper_id):
    try:
        with open(path, "w") as f:
            f.write(wallpaper_id)
        print("Wallpaper Engine edited successfully")    
    except Exception as e:
        print(e)

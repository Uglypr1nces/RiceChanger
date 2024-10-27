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

def change_css(path, old_value, new_value):
    try:
        with open(path, "r") as f:
            data = f.read()

        data = data.replace(old_value, new_value)

        with open(path, "w") as f:
            f.write(data)
        print("CSS edited successfully")
    except Exception as e:
        print(e)

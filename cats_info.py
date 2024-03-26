from pathlib import Path

path = Path("Cats_File.txt")

def get_cats_info(path):
    try:
        with open(path, "r") as cats_info:
            cats = []
            for cat in cats_info:
                cat = cat.split(",")
                id = cat[0]
                name = cat[1]
                age = int(cat[2])
                cats_line = {"id": id, "name": name, "age": age}
                cats.append(cats_line)
    except FileNotFoundError:
        return None
    return cats

print(get_cats_info(path))
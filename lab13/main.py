# lab 5 of day 3 - 4 workbook

import os
from pathlib import Path
import json
import pickle
import csv
from directory_snapshot import DirectorySnapshot

# List me all the files , folders in my directory

def scan_directory(basepath):

    files = []
    # for each files in my directory (os.walk)
    # it return tuple of three items
    for root, dirs, filenames in os.walk(basepath):
        for name in filenames:
            full_path = os.path.join(root,name)
            files.append({
                "name":name,
                "path":full_path,
                "size":os.path.getsize(full_path)
            })
    return files

# JSON to Python conversion
# Save as JSON file

def save_to_json(data,filename):
    # write - open and overwrite (w)
    # append - open and add at the end (a)
    # read - r
    # with - try except file, it will open and catch error right away
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_from_json(filename):
    with open(filename,"r",encoding="utf-8") as f:
        return json.load(f)

# load from csv
def load_from_csv(filename):
    with open(filename, "r", newline="") as csv_file:
        # using DictReader -> Read it line by line
        reader = csv.DictReader(csv_file)
        # for each line print it
        for row in reader:
            print(row)

def save_to_csv(data,filename):
    with open(filename, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_with_pickle(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def load_with_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


def main():
    print("\n--- Part: Directory scan")
    base = Path(".")
    file_data = scan_directory(base)
    
    print("FIles found: ",len(file_data))
    print("Sample: ", file_data[:2])

    print("\n--- Part 2: JSON Serialization ---")
    # go save to file    
    save_to_json(file_data,"files.json")

    #to read from filed
    loaded_json = load_from_json("files.json")
    print("Loaded from JSON: ", len(loaded_json))

    print("\n -- Part 3: CSV Serialization ---")
    save_to_csv(file_data, "files.csv")

    # to read from file
    load_from_csv("files.csv")

    print("\n -- Part 4: Pickle Persistence ---")
    snapshot = DirectorySnapshot(base, file_data)
    print("Snapshot summary ", snapshot.summary())

    save_with_pickle(snapshot, "snapshot.pkl")

    restored = load_with_pickle("snapshot.pkl")
    print("Restored summary: ", restored.summary())


# Why can JSON store lists/dicts but not objects?
# JSOn and List and dict structure is the same
# To store and object it needs to be serialized and deserialized

# Why does pickle restore full object behavior?
#Pickle  stores the serialized object directly
# even for dict and list it needs to be serialized as Class
# tthat is why pickle restore full object behavior

# Which is safer for config files?
# JSON is saver - to turn on / off easily
# becareful not store sensitive information, in that case
# .env file (environment) file is the suitabke


if __name__ == "__main__":
    main()

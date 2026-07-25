import json
import os

if os.path.exists("pythonTracker.json"):
    with open("pythonTracker.json", "r") as f:
        currentModsDict = json.load(f)
        currentModsList = currentModsDict["mods"]
        print(currentModsList)
else:
    with open("pythonTracker.json", "w") as f:
        currentModsList = []
        for i in os.listdir(os.getcwd()):
            if os.path.isfile(i):
                currentModsList.append(i)
        currentModsDict = {
            "mods":currentModsList,
        }
        json.dump(currentModsDict,f)


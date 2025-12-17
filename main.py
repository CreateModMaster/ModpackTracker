import json
import os
nextDict = {}
packName = input("Enter pack name: ")
packFileRead = open(packName + ".json", "r")
currentDict = {
    "modsDir":[],
    "mods":[],
}
try:
    currentDict = json.load(packFileRead)
    modsDir = currentDict['modsDir']
except json.decoder.JSONDecodeError:
    modsDir = input("Enter mods directory: ")
    nextDict['modsDir'] = modsDir
noMods = os.listdir(modsDir)
print("Would you like to add/revert? ")
AorR = input().lower()
nextDict["modsDir"] = modsDir
if AorR == "add":
    currentMods = currentDict['mods']
    for mod in noMods:
        if not mod in currentMods:
            if mod == ".index":
                pass
            else:
                currentMods.append(mod)
    nextDict['mods'] = currentMods
elif AorR == "revert":
    currentMods = currentDict['mods']
    for mod in noMods:
        if not mod in currentMods:
            if mod == ".index":
                pass
            else:
                os.remove(modsDir + "\\" + mod)
nextDict['mods'] = currentMods
packFile = open(packName + ".json", "w")
json.dump(nextDict, packFile)
packFile.close()
packFileRead.close()
#A python program to easily keep track of the mods in a minecraft mods folder
#Copyright (C) 2025  Alex Inns
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or(at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import os
nextDict = {}
packName = input("Enter pack name: ")
try:
    packFileRead = open(packName + ".json", "r")
except FileNotFoundError:
    packFileRead = open(packName + ".json", "w")
    packFileRead.close()
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

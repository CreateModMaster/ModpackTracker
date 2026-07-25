import json
import os

if not os.path.isfile(os.getcwd() + "\\pythonTracker.json"):  #Checks to see if a history file already exists
    with open(os.getcwd() + "\\pythonTracker.json") as JsonFile:  #Opens the modpack history file
        if os.path.exists(os.getcwd() + "\\crash-reports"):  #Checks to see if there is a new crash report
            with open(os.getcwd() + "\\crash-reports" + os.listdir(os.getcwd() + "\\crash-reports")[0]) as CrashFile:  #Opens the crash report file
                changedMods = []  #Creates a new list to save any added/deleted mods since last run
                oldJsonDict = json.load(JsonFile)  #Converts history file to a python dictionary
                oldModsList = oldJsonDict["mods"]  #Saves the last known mods to a list
                newModsList = os.listdir(os.getcwd() + "\\mods")  #Creates a list of all the current mods
                if len(oldModsList) > len(newModsList): #Checks to see which way through the loop it should go
                    for i in oldModsList:  #Loops through the old mod list as that one is longer
                        if not i in newModsList:  #Checks to see if the current item in the old list is in the new list. If not, then we know it has been deleted
                            changedMods.append(i)  #Adds the deleted mod to list of changed mods
                else:
                    for i in newModsList:  #Loops through the new mod list as that one is longer
                        if not i in oldModsList:  #Checks to see if the current item in the new list is in the old list. If not, then we know it has been added
                            changedMods.append(i)  #Adds the added mod to the list of changed mods



import json
import os

if not os.path.isfile(os.getcwd() + "\\pythonTracker.json"):  #Checks to see if a history file already exists
    with open(os.getcwd() + "\\pythonTracker.json") as JsonFile:  #Opens the modpack history file
        if os.path.exists(os.getcwd() + "\\crash-reports"):  #Checks to see if there is a new crash report
            with open(os.getcwd() + "\\crash-reports" + os.listdir(os.getcwd() + "\\crash-reports")[0]) as CrashFile:  #Opens the crash report file
                changedModsName = []  #Creates a new list to save the name of any added/deleted mods since last run
                changedModsAction = []  #Creates a new list to save whether a mod file added or deleted since last run
                oldJsonDict = json.load(JsonFile)  #Converts history file to a python dictionary
                oldModsList = oldJsonDict["mods"]  #Saves the last known mods to a list
                newModsList = os.listdir(os.getcwd() + "\\mods")  #Creates a list of all the current mods
                for i in oldModsList:  #Loops through the old mod list as that one is longer
                    if not i in newModsList:  #Checks to see if the current item in the old list is in the new list. If not, then we know it has been deleted
                        changedModsName.append(i)  #Adds the deleted mod to list of changed mods
                        changedModsAction.append("--")  #Adds to the list of actions to mark that this mod has been deleted
                for i in newModsList:  #Loops through the new mod list as that one is longer
                    if not i in oldModsList:  #Checks to see if the current item in the new list is in the old list. If not, then we know it has been added
                        changedModsName.append(i)  #Adds the added mod to the list of changed mods
                        changedModsAction.append("++")  #Adds to the list of actions to mark that this mod had been added
                print("Your Minecraft instance crashed.")
                if "++" in changedModsAction:  #Checks to see if any mods have been downloaded since last run
                    print("You downloaded these mods since last launch: ")
                    for i in range(0,len(changedModsAction)):  #Loops through the list looking for downloaded mods
                        if changedModsAction[i] == "++":  #The program finds a downloaded action
                            print(changedModsName[i])  #It finds the action's matching pair in the list of names
                if "--" in changedModsAction:  #Checks to see if any mods have been removed since last run
                    print("And you removed these mods: ")
                    for i in range(0,len(changedModsAction)):  #Loops through the list looking for removed mods
                        if changedModsAction[i] == "--":  #The program finds a removed action
                            print(changedModsName[i])  #It finds the action's matching pair in the list of names
                print("\nPlease select what you would like to do about this problem:\na. Delete all the mods downloaded in the list above\nb. Perform a linear search by disabling each mod and running the instance to find the faulty mod\nc. Perform a linear search by moving each mod to another directory and running the instance, before moving the mod back. To find the faulty one.\nd. Perform a binary search by disabling mods to find the faulty one\ne. Perform a binary search by moving mods to another directory to find the faulty one\nf. Do Nothing")


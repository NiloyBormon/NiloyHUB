from tkinter import messagebox
import requests
import subprocess
import sys

def updateBtnFun():
    currentVersion = getCurrentVersion()
    latestVersion = getLatestVersion()
    if currentVersion == latestVersion:
        messagebox.showinfo("output", f"No update available current version {currentVersion} latest versioin {latestVersion}")
    else:
        choice = messagebox.askyesno("output", f"Update available current version {currentVersion} latest version{latestVersion}\nDo you want to update?")
        if choice:
            messagebox.showinfo("Updating", "Updating. This may take some time.")
            with open("update.exe","wb")as f:
                f.write(requests.get("https://github.com/NiloyBormon/NiloyHUB/raw/refs/heads/main/update.exe").content)
            with open ("NiloyHUBNew.exe","wb")as f:
                f.write(requests.get("https://github.com/NiloyBormon/NiloyHUB/raw/refs/heads/main/NiloyHUBGui.exe").content)
            updateCurrentVersionfun(latestVersion)
            messagebox.showinfo("sdfs","Update done. Cleaning up and restarting.")
            subprocess.Popen(["update.exe"])
            sys.exit()

def updateCurrentVersionfun(latestVersion):
    with open ("version.txt","w")as f:
        f.write(latestVersion)

def ToDoListBtnFun():
    try: 
        subprocess.Popen(["ToDoListGui.exe"])
    except:
        messagebox.showinfo("download", "Downloading required files. Please wait.")
        with open("ToDoListGui.exe", "wb")as f:
            f.write(requests.get("https://github.com/NiloyBormon/NiloyHUB/raw/refs/heads/main/ToDoListGui.exe").content)
        messagebox.showinfo("sf", "Download done opening")
        subprocess.Popen(["ToDoListGui.exe"])

def randomPasswordGeneratorFun():
    # userInput = simp
    messagebox.showinfo("", "under devlopment!")
    
def RockPaperScissorFun():
    messagebox.showinfo("Construction", "under developent!")

def getLatestVersion():
    version = requests.get("https://raw.githubusercontent.com/NiloyBormon/NiloyHUB/refs/heads/main/version").text
    return version.strip()

def getCurrentVersion():
    currentVersion = "0.0.1"
    try:
        with open ("version.txt","r")as f:
            currentVersion = f.read()
        return currentVersion.strip()
    except FileNotFoundError:
        with open("version.txt", "w") as f:
            f.write(currentVersion)
        return currentVersion.strip()


# currentVersion = getCurrentVersion()
# latestVersion = getLatestVersion()
# print(currentVersion,latestVersion)
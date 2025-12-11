from tkinter import messagebox, simpledialog
import json

def createNewTaskFun():
    tasks = loadOrCreateTasksFun()
    newTaskKey = simpledialog.askstring("New task","Enter your task")
    newTaskVakue = simpledialog.askstring("description","Describe your task")
    if newTaskKey:
        tasks[newTaskKey]=newTaskVakue
        saveTaskFun(tasks)
    messagebox.showinfo("output", "Task saved")

def viewTasksFun():
    tasks = loadOrCreateTasksFun()
    if not tasks:
        messagebox.showinfo("skdjf", "No task available")
    else :
        for keys in tasks:
            messagebox.showinfo("tasks", f"All tasks:\n{keys}, description: {tasks[keys]}")
                
def loadOrCreateTasksFun():
    tasks = {}
    try:
        with open("tasks.json","r")as f:
            tasks= json.load(f)
    except FileNotFoundError:
        with open("tasks.json","w")as f:
            json.dump(tasks,f)
    return tasks

def saveTaskFun(tasks):
    with open("tasks.json","w")as f:
        json.dump(tasks,f)

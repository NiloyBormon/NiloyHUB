import tkinter
from tkinter import messagebox, simpledialog
from toDoListBackEnd import createNewTaskFun, viewTasksFun

root = tkinter.Tk()
root.title("ToDoList")
root.geometry("250x150")

createNewTaskBtn = tkinter.Button(root, text="Create new task", command=createNewTaskFun)
createNewTaskBtn.pack(padx=10,pady=10)

viewTaskBtn = tkinter.Button(root, text="View tasks", command=viewTasksFun)
viewTaskBtn.pack(padx=10,pady=10)

root.mainloop()
import tkinter
from NiloyHUBBackEnd import updateBtnFun, ToDoListBtnFun, RockPaperScissorFun, randomPasswordGeneratorFun

root = tkinter.Tk()
root.title("NiloyHUB")
root.geometry("250x250")

welcomeLabel = tkinter.Label(root, text="Welcome to NiloyHUB", font=("arial",10))
welcomeLabel.pack(padx=10,pady=10)

updateBtn = tkinter.Button(root, text="Check for update", command=updateBtnFun)
updateBtn.pack(padx=10,pady=10)

ToDoListBtn = tkinter.Button(root, text="ToDoList", command=ToDoListBtnFun)
ToDoListBtn.pack(padx=10,pady=10)

RockPaperScissorBtn = tkinter.Button(root, text="Rock Paper Scissor",command=RockPaperScissorFun)
RockPaperScissorBtn.pack(padx=10,pady=10)

randomPasswordGeneratorBtn = tkinter.Button(root, text="Random password generator", command=randomPasswordGeneratorFun)
randomPasswordGeneratorBtn.pack(padx=10,pady=10)

root.mainloop()
import tkinter
from tkinter import messagebox
from RockPaperScissorsBackEnd import rockBtnFun

root = tkinter.Tk()
root.title("RockPaperScissors")
root.geometry("250x150")

# computerChoiceLbl = tkinter.Label(root, text=computerChoiceFun)
# computerChoiceLbl.pack(pady=10)

rockBtn = tkinter.Button(root, text="Rock", command=rockBtnFun)
rockBtn.pack(pady=10)

paperBtn = tkinter.Button(root, text="Paper")
paperBtn.pack(pady=10)

scissorBtn = tkinter.Button(root, text="Scissor")
scissorBtn.pack(pady=10)

root.mainloop()
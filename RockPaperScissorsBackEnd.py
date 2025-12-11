from tkinter import messagebox
import random

def pcChoiceFun():
    pcChoiceLst = ["Rock","Paper","Scissor"]
    pcChoice = random.randint(0,2)
    return pcChoiceLst[pcChoice]

def rockBtnFun():
    decission("Rock")

def decission(humanChoice):
    pcChoice = pcChoiceFun()
    if humanChoice == pcChoice:
        messagebox.showinfo("Draw", "Its a tie!")
    elif humanChoice == "Rock" and pcChoice=="Scissor":
        messagebox.showinfo("hjh","You win!")
        sccore += 1
    elif humanChoice == "Paper" and pcChoice=="Rock":
        messagebox.showinfo("hjh","You win!")
        sccore += 1
    elif humanChoice == "Scissor" and pcChoice=="Paper":
        messagebox.showinfo("hjh","You win!")
        sccore += 1
    else:
        messagebox.showinfo("lost", "You Loose")
        pcSccore += 1

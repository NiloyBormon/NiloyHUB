import tkinter 
from tkinter import messagebox

root = tkinter.Tk()
root.title("PasswordGeneratorGui")
root.geometry("250x150")

inputLengthTbx = tkinter.Text()
inputLengthTbx.pack(padx=10,pady=10)

if inputLengthTbx:
    messagebox.showinfo("outpto", f"{inputLengthTbx}")

root.mainloop()
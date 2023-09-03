from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import subprocess


def moss():
    global moss, running_window

    '''def moss_hide():
        moss_button = Button(running_window, bd=0.01)
        moss_button.config(text="MOSS", command=moss, bg=show_dl_menu)
        moss_button.place(x=25, y=0)
        running_window.update()'''

    moss = Tk()

    moss.attributes("-fullscreen", True)
    moss.attributes("-topmost", True)
    moss.config(bg="black")

    global cmd_output_label

    cmd_output_text = Label(moss, bg="black", fg="white", font=(None, 30), text="命令输出↓")
    cmd_output_label = Label(moss, text="None", bg="grey", fg="white", font=(None, 30))
    cmd_cmd_here = Label(moss, bg="black", fg="white", font=(None, 30), text="命令输入↓")
    cmd_in_entry = Entry(moss, bg="dark grey", bd=0.01, fg="white", font=(None, 30))
    cmd_cmd_here.grid(row=2, column=0)
    cmd_in_entry.grid(row=3, column=0)
    cmd_output_text.grid(row=4, column=0)
    cmd_output_label.grid(row=5, column=0)

    def mc(cmd_input):
        global moss
        if cmd_input == "exit":
            moss.destroy()
        elif cmd_input == "hide":
            moss.destroy()
            moss_hide()
        else:
            cmd_output_label.config(text="""no command named ' """ + cmd_input + " ' ")

    def cmd_input(event):
        mc(cmd_input=cmd_in_entry.get())

    moss.bind("<Return>", cmd_input)

    moss.mainloop()

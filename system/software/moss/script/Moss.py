from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import subprocess


def moss():
    global moss
    moss = Tk()

    moss.attributes("-fullscreen", True)
    moss.attributes("-topmost", True)
    moss.config(bg="black")

    global cmd_output_label

    cmd_output_text = Label(moss, bg="black", fg="white", font=(None, 30), text="命令输出↓")
    cmd_output_label = Label(moss, text="None", bg="grey", fg="white", font=(None, 30))
    cmd_cmd_here = Label(moss, bg="black", fg="white", font=(None, 30), text="命令输入↓")
    cmd_in_entry = Entry(moss, bg="dark grey", bd=0.01, fg="white", font=(None, 30))
    cmd_choose_interpreter = ttk.Combobox(moss)
    cmd_choose_interpreter["value"] = ["Python", "System Shell", "MOSS"]
    cmd_choose_interpreter["background"] = "grey"
    cmd_choose_interpreter["foreground"] = "black"
    cmd_choose_interpreter["font"] = (None, 30)
    cmd_choose_interpreter_text = Label(moss, bg="black", fg="white", font=(None, 30), text="选择解释器↓")
    cmd_choose_interpreter_text.grid(row=0, column=0)
    cmd_choose_interpreter.grid(row=1, column=0)
    cmd_cmd_here.grid(row=2, column=0)
    cmd_in_entry.grid(row=3, column=0)
    cmd_output_text.grid(row=4, column=0)
    cmd_output_label.grid(row=5, column=0)

    def mc(cmd_input):
        global moss
        if cmd_input == "exit":
            moss.destroy()

    def cmd_input(event):
        if cmd_choose_interpreter.get() == "System Shell":
            cmd_output_label.config(text=os.popen(cmd_in_entry.get(), "r", 10).read())
        if cmd_choose_interpreter.get() == "Python":
            cmd_output_label.config(text=subprocess.check_output(['python', "-c", cmd_in_entry.get()]).decode('utf-8'))
        if cmd_choose_interpreter.get() == "MOSS":
            mc(cmd_input=cmd_in_entry.get())

    moss.bind("<Return>", cmd_input)

    moss.mainloop()

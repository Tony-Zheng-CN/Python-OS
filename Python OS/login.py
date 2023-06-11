from tkinter import *
from PIL import Image, ImageTk
from main import *
from register import *
from start import start

user_name = open("./username").read()
user_password = open("./password").read()

login = Tk()

login.attributes("-fullscreen", True)
login.attributes("-alpha", 5)


def enter_b():
    if password_input.get() == user_password:
        start()
        login.destroy()
    else:
        exit("Error:Password is not TRUE\nError 01")


def enter_e(event):
    if password_input.get() == user_password:
        start()
        login.destroy()
    else:
        exit("Error:Password is not TRUE\nError 01")


name_label = Label(login, text="用户名:" + user_name, font=(None, 50))
name_label.place(x=login.winfo_screenwidth() / 2, y=login.winfo_screenheight() / 2, anchor="s")
password_input = Entry(login, show="*", font=(None, 50))
password_input.place(x=login.winfo_screenwidth() / 2, y=login.winfo_screenheight() / 2, anchor="n")
enter_button = Button(login, bd=0.01, text="确认", font=(None, 50), command=enter_b)
enter_button.place(x=login.winfo_screenwidth() / 2, y=login.winfo_screenheight() / 2 + 100, anchor="n")
login.bind("<Enter>")

login.mainloop()

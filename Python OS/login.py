from tkinter import *
from PIL import Image, ImageTk
from main import *
from register import *
from start import start

usernames = open("./username.js", "r").read().splitlines()
passwords = open("./password.js", "r").read().splitlines()
if not len(usernames) == len(passwords):
    exit("UserInfoError\nError 001")

login = Tk()

login.attributes("-fullscreen", True)
login.attributes("-alpha", 5)


def out(event):
    exit()


def enter_b():
    for x in range(0, len(usernames)):
        if usernames[x] == name_choose.get():
            user_index = x
            user_name = usernames[x]
            user_password = passwords[x]
    if password_input.get() == user_password:
        start()
        login.destroy()
    else:
        exit("InfoInputError\nError 002")


def enter_e(event):
    for x in range(0, len(usernames)):
        if usernames[x] == name_choose.get():
            user_index = x
            user_name = usernames[x]
            user_password = passwords[x]
    if password_input.get() == user_password:
        start()
        login.destroy()
    else:
        exit("InfoInputError\nError 002")


name_label = Label(login, text="用户名:", font=(None, 50))
name_label.place(x=login.winfo_screenwidth() / 2 - 300, y=login.winfo_screenheight() / 2, anchor="s")
name_choose = ttk.Combobox(login)
name_choose["value"] = usernames
name_choose["font"] = (None, 40)
name_choose.place(x=login.winfo_screenwidth() / 2 + 200, y=login.winfo_screenheight() / 2, anchor="s")
password_input = Entry(login, show="*", font=(None, 50))
password_input.place(x=login.winfo_screenwidth() / 2, y=login.winfo_screenheight() / 2, anchor="n")
enter_button = Button(login, bd=0.01, text="确认", font=(None, 50), command=enter_b)
enter_button.place(x=login.winfo_screenwidth() / 2, y=login.winfo_screenheight() / 2 + 100, anchor="n")
login.bind("<Return>", enter_e)
login.bind("<Escape>", out)

login.mainloop()

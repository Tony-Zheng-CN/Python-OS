from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from playsound import *
from PIL import Image
from PIL import ImageTk
from pyautogui import *
from math import *
import sys
import zipfile as zf
import win32gui

sys.path.append('./system/software/moss/script')
sys.path.append('./system/software/explorer/script')

from Moss import moss
from explorer import explorer

try:
    disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
except FileNotFoundError:
    disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
    disk_A.setpassword("Python")
    disk_A.close()
    disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
disk_A.extractall(path="./scratch file/disk/A", pwd="Python")


def shutdown():
    messagebox.showwarning(title="关机", message="正在关机")
    exit()


def restart():
    global main_window
    messagebox.showwarning(title="重启", message="正在重启")
    main_window.destroy()
    main()


def ico_click():
    sd_window = Tk()

    sd_window.config(bg="white")
    sd_window.title("关机或重启")

    sd_button = Button(sd_window, text="关机", command=shutdown, bd=0.01, font=(None, 20), bg="white")
    rs_button = Button(sd_window, text="重启", command=restart, bd=0.01, font=(None, 20), bg="white")
    cc_button = Button(sd_window, text="取消", command=sd_window.destroy, bd=0.01, font=(None, 20), bg="white")
    sd_button.grid(row=0, column=0)
    rs_button.grid(row=1, column=0)
    cc_button.grid(row=2, column=0)

    sd_window.mainloop()


def main():
    global main_window
    main_window = Tk()
    from tkinter import messagebox

    main_window.title("Python OS")
    main_window.attributes('-fullscreen', True)
    main_window.attributes('-topmost', False)
    main_window.config(bg='white')

    global explorer_img_png
    explorer_img_png = ImageTk.PhotoImage(Image.open("system/software/explorer/image/explorer.png"))
    moss_img_png = ImageTk.PhotoImage(Image.open("system/software/moss/image/Moss.png"))
    system_close_ico_png = ImageTk.PhotoImage(Image.open("system/image/close.png"))
    system_open_ico_png = ImageTk.PhotoImage(Image.open("system/image/open.png"))

    system_ico = Button(main_window, image=system_open_ico_png, bg="grey", bd=0.01, command=ico_click)
    system_ico.place(x=int(main_window.winfo_screenwidth() / 4) - 35, y=0)
    system_text = Label(main_window, text="系\n统", bg="grey", font=("Minecraft AE", 9))
    system_text.place(x=int(main_window.winfo_screenwidth() / 4), y=0)
    explorer_button = Button(main_window, bd=0.01)
    explorer_button.config(image=explorer_img_png, command=explorer, bg="grey")
    explorer_button.place(x=int(main_window.winfo_screenwidth() / 4) + 20, y=0)
    moss_button = Button(main_window, bd=0.01)
    moss_button.config(image=moss_img_png, command=moss, bg="grey")
    moss_button.place(x=int(main_window.winfo_screenwidth() / 4) + 65, y=0)

    main_window.mainloop()

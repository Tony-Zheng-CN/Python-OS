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
import os
import shutil

sys.path.append('system/software/moss/script')
sys.path.append('system/software/explorer/script')
sys.path.append('system/software/setting up/script')

from Moss import moss
from explorer import explorer
from set import setting

try:
    disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
except FileNotFoundError:
    disk_A = zf.ZipFile(file="./disks/A.zip", mode="w")
    disk_A.close()
    disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
try:
    os.mkdir("./scratch file/disk/A/")
except FileExistsError:
    pass
disk_A.extractall(path="./scratch file/disk/A")
disk_A.close()
try:
    disk_uo = zf.ZipFile(file="./disks/UserOption.zip", mode="r")
except FileNotFoundError:
    disk_uo = zf.ZipFile(file="./disks/UserOption.zip", mode="w")
    disk_uo.close()
    disk_uo = zf.ZipFile(file="./disks/UserOption.zip", mode="r")
try:
    os.mkdir("./scratch file/disk/disk_uo/")
except FileExistsError:
    pass
disk_uo.extractall(path="./scratch file/disk/UserOption")
disk_uo.close()


def shutdown():
    disk_A = zf.ZipFile(file=os.getcwd() + "\\disks\\A.zip", mode="w")
    file_list_shut = os.listdir("./scratch file/disk/A/")
    for x in range(0, len(file_list_shut)):
        disk_A.write("./scratch file/disk/A/" + file_list_shut[x], file_list_shut[x])
    disk_A.close()
    disk_uo = zf.ZipFile(file=os.getcwd() + "\\disks\\UserOption.zip", mode="w")
    file_list_shut = os.listdir("./scratch file/disk/UserOption/")
    for x in range(0, len(file_list_shut)):
        disk_uo.write("./scratch file/disk/UserOption/" + file_list_shut[x], file_list_shut[x])
    disk_uo.close()
    exit()


def shutdown_unsave():
    exit()


def restart():
    disk_A = zf.ZipFile(file=os.getcwd() + "\\disks\\A.zip", mode="w")
    file_list_shut = os.listdir("./scratch file/disk/A/")
    for x in range(0, len(file_list_shut)):
        disk_A.write("./scratch file/disk/A/" + file_list_shut[x], file_list_shut[x])
    disk_A.close()
    disk_uo = zf.ZipFile(file=os.getcwd() + "\\disks\\UserOption.zip", mode="w")
    file_list_shut = os.listdir("./scratch file/disk/UserOption/")
    for x in range(0, len(file_list_shut)):
        disk_uo.write("./scratch file/disk/UserOption/" + file_list_shut[x], file_list_shut[x])
    disk_uo.close()
    main_window.destroy()
    try:
        disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
    except FileNotFoundError:
        disk_A = zf.ZipFile(file="./disks/A.zip", mode="w")
        disk_A.close()
        disk_A = zf.ZipFile(file="./disks/A.zip", mode="r")
    disk_A.extractall(path="./scratch file/disk/A")
    disk_A.close()
    try:
        disk_uo = zf.ZipFile(file="./disks/UserOption.zip", mode="r")
    except FileNotFoundError:
        disk_uo = zf.ZipFile(file="./disks/UserOption.zip", mode="w")
        disk_uo.close()
        disk_uo = zf.ZipFile(file="./disks/UserOption.zip", mode="r")
    disk_uo.extractall(path="./scratch file/disk/UserOption")
    disk_uo.close()
    main()


def ico_click():
    sd_window = Tk()

    sd_window.config(bg="white")
    sd_window.title("关闭或重启")

    sd_button = Button(sd_window, text="关闭", command=shutdown, bd=0.01, font=(None, 20), bg="white")
    sd_unsave_button = Button(sd_window, text="不保存关闭", command=shutdown_unsave, bd=0.01, font=(None, 20), bg="red")
    rs_button = Button(sd_window, text="重启", command=restart, bd=0.01, font=(None, 20), bg="white")
    cc_button = Button(sd_window, text="取消", command=sd_window.destroy, bd=0.01, font=(None, 20), bg="white")
    sd_button.grid(row=0, column=0)
    rs_button.grid(row=1, column=0)
    cc_button.grid(row=2, column=0)
    sd_unsave_button.grid(row=3, column=0)

    sd_window.mainloop()


def main():
    try:
        options_file = open("./scratch file/disk/UserOption/show", "r")
        options = options_file.read().splitlines()
        options_file.close()
    except FileNotFoundError:
        options_file = open("./scratch file/disk/UserOption/show", "w")
        options_file.write("#000000\nshow:color(background)\n#353535"
                           "\nshow:color(menu)\n#ffffff\nshow:color(text)")
        options_file.close()
        options_file = open("./scratch file/disk/UserOption/show", "r")
        options = options_file.read().splitlines()
        options_file.close()
    global show_dl_bg, show_dl_menu, show_dl_fg
    show_dl_bg = options[0]
    show_dl_menu = options[2]
    show_dl_fg = options[4]

    global main_window
    main_window = Tk()
    from tkinter import messagebox

    main_window.title("Python OS")
    main_window.attributes('-fullscreen', True)
    main_window.attributes('-topmost', False)
    main_window.config(bg=show_dl_bg)

    global system_open_ico_png, explorer_img_png
    explorer_img_png = ImageTk.PhotoImage(Image.open(os.getcwd() + "/system/software/explorer/image/explorer.png"), master=main_window)
    moss_img_png = ImageTk.PhotoImage(Image.open(os.getcwd() + "/system/software/moss/image/Moss.png"), master=main_window)
    set_img_png = ImageTk.PhotoImage(Image.open(os.getcwd() + "/system/software/setting up/image/set.png"), master=main_window)
    system_close_ico_png = ImageTk.PhotoImage(Image.open(os.getcwd() + "/system/image/close.png"), master=main_window)
    system_open_ico_png = ImageTk.PhotoImage(Image.open(os.getcwd() + "/system/image/open.png"), master=main_window)

    system_ico = Button(main_window, image=system_open_ico_png, bg=show_dl_menu, bd=0.01, command=ico_click)
    system_ico.place(x=int(main_window.winfo_screenwidth() / 4) - 35, y=0)
    system_text = Label(main_window, text="系\n统", bg=show_dl_menu, font=("Minecraft AE", 9), fg=show_dl_fg)
    system_text.place(x=int(main_window.winfo_screenwidth() / 4), y=0)
    explorer_button = Button(main_window, bd=0.01)
    explorer_button.config(image=explorer_img_png, command=explorer, bg=show_dl_menu)
    explorer_button.place(x=int(main_window.winfo_screenwidth() / 4) + 20, y=0)
    moss_button = Button(main_window, bd=0.01)
    moss_button.config(image=moss_img_png, command=moss, bg=show_dl_menu)
    moss_button.place(x=int(main_window.winfo_screenwidth() / 4) + 20 + 45, y=0)
    set_button = Button(main_window, bd=0.01)
    set_button.config(image=set_img_png, command=setting, bg=show_dl_menu)
    set_button.place(x=int(main_window.winfo_screenwidth() / 4) + 20 + 45 + 45, y=0)
    app_text = Label(main_window, text="软\n件", bg=show_dl_menu, font=("Minecraft AE", 9), fg=show_dl_fg)
    app_text.place(x=int(main_window.winfo_screenwidth() / 4) + 20 + 45 + 45 + 45, y=0)

    main_window.mainloop()

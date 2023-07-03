import random as r
import time as t
import sys
from tkinter import *
import os
from tkinter import colorchooser
from PIL import Image
from PIL import ImageTk
from register import reg_new


def setting():
    options = open(os.getcwd() + "/scratch file/disk/UserOption/show.js", "r").read().splitlines()
    global set_frame
    show_dl_bg = options[0]
    show_dl_menu = options[2]
    show_dl_fg = options[4]

    set_win = Tk()

    set_win.attributes("-fullscreen", True)
    set_win.title("Python OS Set Up")
    set_win.config(bg=show_dl_bg)

    set_frame = Frame(set_win, bg=show_dl_bg)
    set_frame.place(x=433, y=0)

    def setting_desktop():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)
        l1 = Label(set_frame, text="None", font=(None, 20), fg=show_dl_fg, bg=show_dl_menu)
        l1.pack()

    def setting_app():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)

    def setting_show():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)
        set_show_lf = LabelFrame(set_frame, text="1.背景 控件 文字 颜色调整", bg=show_dl_menu
                                 , fg=show_dl_fg)
        set_show_lf.pack()

        def show_dl_changebg():
            global show_dl_nbg
            show_dl_nbg = colorchooser.askcolor(title="选择背景颜色")[1]

        def show_dl_changemenu():
            global show_dl_nmenu
            show_dl_nmenu = colorchooser.askcolor(title="选择控件颜色")[1]

        def show_dl_changefg():
            global show_dl_nfg
            show_dl_nfg = colorchooser.askcolor(title="选择文字颜色")[1]

        def show_dl_change():
            global show_dl_nfg, show_dl_nbg, show_dl_nmenu
            show_dl_write_thing = ""
            for x in range(0, len(options)):
                global show_dl_nfg, show_dl_nbg, show_dl_nmenu
                if x == 0:
                    # show_dl_write_thing = show_dl_write_thing + show_dl_entry1.get() + "\n"
                    show_dl_write_thing = show_dl_write_thing + show_dl_nbg + "\n"
                elif x == 2:
                    # show_dl_write_thing = show_dl_write_thing + show_dl_entry2.get() + "\n"
                    show_dl_write_thing = show_dl_write_thing + show_dl_nmenu + "\n"
                elif x == 4:
                    # show_dl_write_thing = show_dl_write_thing + show_dl_entry3.get() + "\n"
                    show_dl_write_thing = show_dl_write_thing + show_dl_nfg + "\n"
                else:
                    show_dl_write_thing = show_dl_write_thing + options[x] + "\n"
                write_options = open(os.getcwd() + "/scratch file/disk/UserOption/show.js", "w")
                write_options.write(show_dl_write_thing)
                write_options.close()

        # show_dl_entry1 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        # show_dl_entry1.grid(row=1, column=0)
        show_dl_cb1 = Button(set_show_lf, bg=show_dl_menu, fg=show_dl_fg, command=show_dl_changebg)
        show_dl_cb1.grid(row=1, column=0)
        show_dl_l1 = Label(set_show_lf, text="背景", fg=show_dl_fg, bg=show_dl_menu)
        show_dl_l1.grid(row=0, column=0)
        # show_dl_entry2 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        # show_dl_entry2.grid(row=1, column=1)
        show_dl_cb2 = Button(set_show_lf, bg=show_dl_menu, fg=show_dl_fg, command=show_dl_changemenu)
        show_dl_cb2.grid(row=1, column=1)
        show_dl_l2 = Label(set_show_lf, text="控件", fg=show_dl_fg, bg=show_dl_menu)
        show_dl_l2.grid(row=0, column=1)
        # show_dl_entry3 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        # show_dl_entry3.grid(row=1, column=2)
        show_dl_cb3 = Button(set_show_lf, bg=show_dl_menu, fg=show_dl_fg, command=show_dl_changefg)
        show_dl_cb3.grid(row=1, column=2)
        show_dl_l3 = Label(set_show_lf, text="文字", fg=show_dl_fg, bg=show_dl_menu)
        show_dl_l3.grid(row=0, column=2)

        show_dl_enter = Button(set_show_lf, text="确认", fg=show_dl_fg, bg=show_dl_menu
                               , command=show_dl_change)
        show_dl_enter.grid(row=2, column=0, columnspan=3)

    def setting_user():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)

        administrator_ico_png = ImageTk.PhotoImage(Image.open(os.getcwd() + "/system/image/administrator.png"),
                                                   master=set_win)

        set_userinfo_button = Button(set_frame, text="1.新建用户",
                                     command=reg_new, bg=show_dl_bg, fg=show_dl_fg,)
        set_userinfo_button.pack()

    def setting_sys():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)

    def setting_about():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)

    def setting_thank():
        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)

    def setting_out():
        set_win.destroy()

    set_desktop = Button(set_win, text="桌面设置", font=(None, 55),
                         bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                         command=setting_desktop)
    set_desktop.place(x=0, y=0)
    set_app = Button(set_win, text="应用设置", font=(None, 55),
                     bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                     command=setting_app)
    set_app.place(x=0, y=set_win.winfo_screenheight() / 8)
    set_show = Button(set_win, text="显示设置", font=(None, 55),
                      bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                      command=setting_show)
    set_show.place(x=0, y=set_win.winfo_screenheight() / 8 * 2)
    set_user = Button(set_win, text="用户设置", font=(None, 55),
                      bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                      command=setting_user)
    set_user.place(x=0, y=set_win.winfo_screenheight() / 8 * 3)
    set_sys = Button(set_win, text="系统设置", font=(None, 55),
                     bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                     command=setting_sys)
    set_sys.place(x=0, y=set_win.winfo_screenheight() / 8 * 4)
    set_about = Button(set_win, text="关于系统", font=(None, 55),
                       bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                       command=setting_about)
    set_about.place(x=0, y=set_win.winfo_screenheight() / 8 * 5)
    set_thank = Button(set_win, text="鸣谢名单", font=(None, 55),
                       bd=0.01, bg=show_dl_menu, fg=show_dl_fg,
                       command=setting_thank)
    set_thank.place(x=0, y=set_win.winfo_screenheight() / 8 * 6)
    set_out = Button(set_win, text="退出软件", font=(None, 55),
                     bd=0.01, bg=show_dl_menu, fg="#FF0000",
                     command=setting_out)
    set_out.place(x=0, y=set_win.winfo_screenheight() / 8 * 7)

    set_win.mainloop()

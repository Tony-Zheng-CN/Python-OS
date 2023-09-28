import random as r
import time as t
import sys
from tkinter import *
from tkinter import ttk
import os
from tkinter import colorchooser
from PIL import Image
from PIL import ImageTk


def setting():
    options = open(os.getcwd() + "/scratch file/disk/UserOption/show.txt", "r").read().splitlines()
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

        def show_dl_change():
            show_dl_write_thing = ""
            for x in range(0, len(options)):
                if x == 0:
                    # show_dl_write_thing = show_dl_write_thing + show_dl_entry1.get() + "\n"
                    show_dl_write_thing = show_dl_write_thing + show_dl_cb1.get() + "\n"
                elif x == 2:
                    # show_dl_write_thing = show_dl_write_thing + show_dl_entry2.get() + "\n"
                    show_dl_write_thing = show_dl_write_thing + show_dl_cb2.get() + "\n"
                elif x == 4:
                    # show_dl_write_thing = show_dl_write_thing + show_dl_entry3.get() + "\n"
                    show_dl_write_thing = show_dl_write_thing + show_dl_cb3.get() + "\n"
                else:
                    show_dl_write_thing = show_dl_write_thing + options[x] + "\n"
                write_options = open(os.getcwd() + "/scratch file/disk/UserOption/show.txt", "w")
                write_options.write(show_dl_write_thing)
                write_options.close()

        # show_dl_entry1 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        # show_dl_entry1.grid(row=1, column=0)
        show_dl_cb1 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        show_dl_cb1.grid(row=1, column=0)
        show_dl_l1 = Label(set_show_lf, text="背景", fg=show_dl_fg, bg=show_dl_menu)
        show_dl_l1.grid(row=0, column=0)
        # show_dl_entry2 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        # show_dl_entry2.grid(row=1, column=1)
        show_dl_cb2 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        show_dl_cb2.grid(row=1, column=1)
        show_dl_l2 = Label(set_show_lf, text="控件", fg=show_dl_fg, bg=show_dl_menu)
        show_dl_l2.grid(row=0, column=1)
        # show_dl_entry3 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
        # show_dl_entry3.grid(row=1, column=2)
        show_dl_cb3 = Entry(set_show_lf, bg=show_dl_menu, fg=show_dl_fg)
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

        def set_userinfo():
            set_userinfo_win = Tk()

            set_userinfo_win.geometry(
                "300x500+" + str(int(set_userinfo_win.winfo_screenheight() / 2) - 300) + "+" + str(
                    int(set_userinfo_win.winfo_screenwidth() / 2) - 500))
            set_userinfo_win.title("增加用户名、密码")
            set_userinfo_win.config(bg=show_dl_bg)

            set_new_name_label = Label(set_userinfo_win, text="新的用户名:", bg=show_dl_bg, fg=show_dl_fg)
            set_new_name_entry = Entry(set_userinfo_win, bg=show_dl_bg, fg=show_dl_fg)
            set_new_pass_label = Label(set_userinfo_win, text="新的密码:", bg=show_dl_bg, fg=show_dl_fg)
            set_new_pass_entry = Entry(set_userinfo_win, bg=show_dl_bg, fg=show_dl_fg)
            set_new_name_label.pack()
            set_new_name_entry.pack()
            set_new_pass_label.pack()
            set_new_pass_entry.pack()

            set_userinfo_win.mainloop()

        set_userinfo_button = Button(set_frame, text="1.设置用户名、密码",
                                     command=set_userinfo, bg=show_dl_bg, fg=show_dl_fg)
        set_userinfo_button.pack()

    def setting_sys():
        def set_bar():
            def write_bar(bar_setting):
                sys_bar_write_thing = ""
                for x in range(0, len(options)):
                    if x == 6:
                        # show_dl_write_thing = show_dl_write_thing + show_dl_entry1.get() + "\n"
                        sys_bar_write_thing = sys_bar_write_thing + bar_setting + "\n"
                    else:
                        sys_bar_write_thing = sys_bar_write_thing + options[x] + "\n"
                    write_options = open(os.getcwd() + "/scratch file/disk/UserOption/show.txt", "w")
                    write_options.write(sys_bar_write_thing)
                    write_options.close()

            global bar_setting
            if set_sys_bar_choose.get() == "横向":
                write_bar("abscissa")
            elif set_sys_bar_choose.get() == "纵向":
                write_bar("vertical")

        global set_frame
        set_frame.destroy()
        set_frame = Frame(set_win, bg=show_dl_bg)
        set_frame.place(x=433, y=0)
        set_sys_bf = LabelFrame(set_frame, text="1.设置任务栏样式", bg=show_dl_menu
                                , fg=show_dl_fg)
        set_sys_bar_choose = ttk.Combobox(set_sys_bf,
                                          background=show_dl_bg)
        set_sys_bar_choose["value"] = ["横向", "纵向"]
        set_sys_bar_choose.pack()
        set_sys_bar_button = Button(set_sys_bf, text="确认",
                                    background=show_dl_bg, fg=show_dl_fg, command=set_bar)
        set_sys_bar_button.pack()
        set_sys_bf.pack()

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

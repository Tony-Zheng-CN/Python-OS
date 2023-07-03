from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def reg():
    reg_win = Tk()

    reg_win.attributes("-fullscreen", True)
    reg_win.title("PythonOS-创建新用户")

    def enter_b():
        if username_entry.get() == "" or password_entry.get() == "":
            reg_win.destroy()
            messagebox.showerror(title="新建用户失败", text="错误原因:新用户名或密码为空")
        else:
            username_text = open('username.js', 'a+')
            password_text = open('password.js', 'a+')
            authority_text = open("authority.js", "a+")
            username_text.write(username_entry.get())
            password_text.write(password_entry.get())
            authority_text.write("sys")
            username_text.close()
            password_text.close()
            authority_text.close()
            reg_win.destroy()
            import login

    def enter_e(event):
        if username_entry.get() == "" or password_entry.get() == "":
            reg_win.destroy()
            messagebox.showerror(title="新建用户失败", text="错误原因:新用户名或密码为空")
        else:
            username_text = open('username.js', 'a+')
            password_text = open('password.js', 'a+')
            authority_text = open("authority.js", "a+")
            username_text.write(username_entry.get())
            password_text.write(password_entry.get())
            authority_text.write("sys")
            username_text.close()
            password_text.close()
            authority_text.close()
            reg_win.destroy()
            import login

    title_label = Label(reg_win, text="创建新用户", font=(None, 50))
    username_label = Label(reg_win, text="用户名:", font=(None, 30))
    username_entry = Entry(reg_win, font=(None, 30))
    password_label = Label(reg_win, text="密码:", font=(None, 30))
    password_entry = Entry(reg_win, font=(None, 30))
    enter_button = Button(text="确认", font=(None, 30), command=enter_b)

    title_label.grid(row=0, column=0, columnspan=2)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    enter_button.grid(row=3, column=0, columnspan=2)

    reg_win.bind("<Return>", enter_e)

    reg_win.mainloop()


def reg_new():
    reg_win = Tk()

    reg_win.attributes("-fullscreen", True)
    reg_win.title("PythonOS-创建新用户")

    def out_b():
        reg_win.destroy()

    def out_e(event):
        reg_win.destroy()

    def enter_b():
        if username_entry.get() == "" or password_entry.get() == "":
            reg_win.destroy()
            messagebox.showerror(title="新建用户失败", message="错误原因:新用户名或密码为空")
        else:
            username_text = open('username.js', 'a+')
            password_text = open('password.js', 'a+')
            authority_text = open('authority.js', 'a+')
            username_text.write("\n" + username_entry.get())
            password_text.write("\n" + password_entry.get())
            authority_text.write("\n" + authority_com.get())
            username_text.close()
            password_text.close()
            authority_text.close()
            reg_win.destroy()

    def enter_e(event):
        if username_entry.get() == "" or password_entry.get() == "":
            reg_win.destroy()
            messagebox.showerror(title="新建用户失败", message="错误原因:新用户名或密码为空")
        else:
            username_text = open('username.js', 'a+')
            password_text = open('password.js', 'a+')
            authority_text = open('authority.js', 'a+')
            username_text.write("\n" + username_entry.get())
            password_text.write("\n" + password_entry.get())
            authority_text.write("\n" + authority_com.get())
            username_text.close()
            password_text.close()
            authority_text.close()
            reg_win.destroy()

    title_label = Label(reg_win, text="创建新用户", font=(None, 50))
    username_label = Label(reg_win, text="用户名:", font=(None, 30))
    username_entry = Entry(reg_win, font=(None, 30))
    password_label = Label(reg_win, text="密码:", font=(None, 30))
    password_entry = Entry(reg_win, font=(None, 30))
    authority_label = Label(reg_win, text="权限:", font=(None, 30))
    authority_com = ttk.Combobox(reg_win)
    authority_com["value"] = ["sys", "user", "visitor"]
    authority_com["font"] = (None, 30)
    enter_button = Button(reg_win, text="确认", font=(None, 30), command=enter_b)
    out_button = Button(reg_win, text="退出", font=(None, 30), command=out_b)

    title_label.grid(row=0, column=0, columnspan=2)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    authority_label.grid(row=3, column=0)
    authority_com.grid(row=3, column=1)
    enter_button.grid(row=4, column=0)
    out_button.grid(row=4, column=1)

    reg_win.bind("<Return>", enter_e)
    reg_win.bind("<Escape>", out_e)

    reg_win.mainloop()

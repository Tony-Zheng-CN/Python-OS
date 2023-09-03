from tkinter import *


def reg():
    reg_win = Tk()

    reg_win.attributes("-fullscreen", True)
    reg_win.title("PythonOS-创建新用户")

    def enter():
        username_text = open('username', 'w+')
        password_text = open('password', 'w+')
        username_text.write(username_entry.get())
        password_text.write(password_entry.get())
        username_text.close()
        password_text.close()
        reg_win.destroy()
        import login

    title_label = Label(reg_win, text="创建新用户", font=(None, 50))
    username_label = Label(reg_win, text="用户名:", font=(None, 30))
    username_entry = Entry(reg_win, font=(None, 30))
    password_label = Label(reg_win, text="密码:", font=(None, 30))
    password_entry = Entry(reg_win, font=(None, 30))
    enter_button = Button(text="确认", command=enter, font=(None, 30))

    title_label.grid(row=0, column=0, columnspan=2)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    enter_button.grid(row=3, column=0, columnspan=2)

    reg_win.mainloop()

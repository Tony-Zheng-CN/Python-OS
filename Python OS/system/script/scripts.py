from tkinter import messagebox


def shutdown():
    messagebox.showwarning(title="关机", message="正在关机")
    exit()


def restart():
    global main_window
    messagebox.showwarning(title="重启", message="正在重启")
    main_window.destroy()
    main()

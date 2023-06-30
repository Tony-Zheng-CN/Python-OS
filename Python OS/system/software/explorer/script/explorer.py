import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *


def explorer():
    options = open(os.getcwd() + "/scratch file/disk/UserOption/show.js", "r").read().splitlines()
    show_dl_bg = options[0]
    show_dl_menu = options[2]
    show_dl_fg = options[4]

    exp_window = Tk()

    exp_window.attributes("-topmost", True)
    exp_window.attributes("-fullscreen", True)
    exp_window.config(bg="black")

    class FileManager:
        def __init__(self, root):
            self.status_bar = None
            self.file_listbox = None
            self.open_file_path = None
            self.root = root
            self.root.title("文件资源管理器")
            self.current_dir = os.getcwd() + "/scratch file/disk/A"
            self.file_list = []
            self.init_ui()

        def init_ui(self):
            # 创建顶部菜单栏
            top_menu = tk.Menu(self.root)
            self.root.config(menu=top_menu)

            # 创建文件操作菜单
            file_menu = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="文件", menu=file_menu)

            # 菜单项：新建文件夹
            file_menu.add_command(label="新建文件夹", command=self.create_folder)

            # 菜单项：删除文件
            file_menu.add_command(label="删除文件", command=self.delete_file)

            # 菜单项：复制文件
            file_menu.add_command(label="复制文件", command=self.copy_file)

            # 菜单项：移动文件
            file_menu.add_command(label="移动文件", command=self.move_file)

            top_menu.add_command(label="退出", command=self.root.destroy)
            # 创建文件列表框
            self.file_listbox = tk.Listbox(self.root, width=215, height=49, bg=show_dl_bg, fg=show_dl_fg,
                                           selectbackground=show_dl_menu)
            self.file_listbox.pack(anchor="nw")

            # 创建底部状态栏
            self.status_bar = tk.Label(self.root, text='当前目录: ' + self.current_dir, bd=1, relief=tk.SUNKEN,
                                       anchor=tk.W, bg=show_dl_bg, fg=show_dl_fg)
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

            # 初始显示当前目录的文件列表
            self.refresh_file_list(self.current_dir)

            exp_window.mainloop()

        def refresh_file_list(self, folder_path):
            # 刷新文件列表
            self.current_dir = folder_path
            self.file_list = os.listdir(folder_path)

            # 清空文件列表框
            self.file_listbox.delete(0, tk.END)

            # 逐行添加文件到列表框
            for file_name in self.file_list:
                full_path = os.path.join(folder_path, file_name)
                if os.path.isdir(full_path):
                    self.file_listbox.insert(tk.END, "/" + file_name)
                else:
                    self.file_listbox.insert(tk.END, file_name)

            # 更新底部状态栏
            self.status_bar['text'] = '当前目录: ' + self.current_dir

        def create_folder(self):
            # 新建文件夹
            self.root.attributes("-topmost", False)
            folder = filedialog.asksaveasfilename(initialdir=self.current_dir, title="新建文件夹",
                                                  initialfile="新建文件夹",
                                                  defaultextension="", filetypes=[("文件夹", "")])
            if folder:
                try:
                    os.makedirs(folder)
                    self.refresh_file_list(self.current_dir)
                except Exception as e:
                    messagebox.showerror("错误", e)
            self.root.attributes("-topmost", True)

        def delete_file(self):
            self.root.attributes("-topmost", False)
            # 删除文件
            sele_items = self.file_listbox.curselection()
            if len(sele_items) <= 0:
                return
            sele = self.file_list[sele_items[0]]
            if messagebox.askyesno("确认", "确认删除文件 " + sele + " 吗？"):
                try:
                    full_path = os.path.join(self.current_dir, sele)
                    if os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                    else:
                        os.remove(full_path)
                    self.refresh_file_list(self.current_dir)
                except Exception as e:
                    messagebox.showerror("错误", e)
            self.root.attributes("-topmost", True)

        def copy_file(self):
            # 复制文件
            self.root.attributes("-topmost", False)
            sele_items = self.file_listbox.curselection()
            if len(sele_items) <= 0:
                return
            sele = self.file_list[sele_items[0]]
            src = os.path.join(self.current_dir, sele)
            dst = filedialog.asksaveasfilename(initialdir=self.current_dir, title="复制文件", initialfile=sele,
                                               defaultextension="", filetypes=[("所有文件", "*.*")])
            if dst:
                try:
                    shutil.copy2(src, dst)
                    self.refresh_file_list(self.current_dir)
                except Exception as e:
                    messagebox.showerror("错误", e)
            self.root.attributes("-topmost", True)

        def move_file(self):
            # 移动文件
            self.root.attributes("-topmost", False)
            sele_items = self.file_listbox.curselection()
            if len(sele_items) <= 0:
                return
            sele = self.file_list[sele_items[0]]
            src = os.path.join(self.current_dir, sele)
            dst = filedialog.asksaveasfilename(initialdir=self.current_dir, title="移动文件", initialfile=sele,
                                               defaultextension="", filetypes=[("所有文件", "*.*")])
            if dst:
                try:
                    shutil.move(src, dst)
                    self.refresh_file_list(self.current_dir)
                except Exception as e:
                    messagebox.showerror("错误", e)
            self.root.attributes("-topmost", True)

    exp = FileManager(root=exp_window)
    exp.init_ui()

from tkinter import *
import os

mainpath = os.getcwd()
disks_list = os.listdir(mainpath+"/disks")
disks_con = len(disks_list)
file_types_list = [".mp3", ".wav", ".txt", ".docx", ".png", ".gif", ".mov", ".mp4"]
files_name_list = []
files_type_list = []



def explorer():
    exp_window = Tk()

    exp_window.title("文件资源管理器/explorer")
    exp_window.attributes("-topmost", True)
    exp_window.attributes("-fullscreen", True)
    exp_window.config(bg="white")

    class File(object):
        def __init__(self):
            self.file_type = file_type
            self.file_path = file_pat

        def confirm_file_type(self):
            files_name_list.append(file_path.endswith(self.file_path)[0])
            files_type_list.append(file_path.endswith(self.file_path)[1])

    exp_window.mainloop()

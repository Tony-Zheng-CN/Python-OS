from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
import os
from tkinter import ttk
import random as r
import time as t


def start():
    start_window = Tk()

    start_window.attributes('-fullscreen', True)
    start_window.attributes('-topmost', True)
    start_window.config(bg='white')

    # playsound(os.getcwd() + '/start.wav')

    def testing():
        global action_listbox, progress
        action_listbox.insert(END, '性能测试 - 0%')
        start = t.perf_counter()
        test_num = 0
        test_num = test_num + 1
        end = t.perf_counter()
        test_time = float('{:.10f}'.format(end - start))
        if test_time <= 0.0000050000:
            action_listbox.insert(END, '性能测试 - 50%')
            progress['value'] = 50
            start = t.perf_counter()
            test_num = 0
            # noinspection PyUnusedLocal
            test_num = test_num - 1
            end = t.perf_counter()
            test_time = float('{:.10f}'.format(end - start))
            if test_time <= 0.000050000:
                action_listbox.insert(END, '性能测试 - 100%')
                action_listbox.insert(END, '性能测试 - 通过')
                progress['value'] = 100
            else:
                exit('性能测试 - 失败')

        main_files_need = ['username', 'main.py', 'password',
                           'start.wav',
                           'system/image/open.png',
                           'system/image/close.png',
                           'system/software/explorer/image/explorer.png',
                           'system/software/explorer/image/explorer.ico',
                           'system/software/explorer/script/explorer.py',
                           'system/software/moss/script/Moss.py',
                           'system/software/moss/image/Moss.png',
                           'system/software/moss/image/Moss.ico'
                           ]

        for x in range(0, len(main_files_need)):
            try:
                open('./' + main_files_need[x], 'r').close()
                action_listbox.insert(END, '主要运行文件存在 - ' + main_files_need[x])
                progress['value'] = progress['value'] + 500 / len(main_files_need) * (x + 1)
            except FileNotFoundError:
                exit('主要运行文件丢失 - ' + main_files_need[x])
        start_window.destroy()
        from main import main
        main()

    # noinspection PyUnusedLocal
    def click_screen(event):
        global action_listbox, progress
        click_to_open.destroy()
        progress_text = Label(start_window, text='开机进度:'
                              , font=('Minecraft AE', 30))
        progress_text.place(x=0, y=start_window.winfo_screenheight() / 2, anchor='sw')
        starting = Label(master=start_window, text='正在开机          \n操作内容↓'
                         , font=('Minecraft AE', 30))
        starting.place(x=0, y=start_window.winfo_screenheight() / 2, anchor='nw')
        progress = ttk.Progressbar(start_window, length=500, maximum=500)
        progress.place(x=200, y=start_window.winfo_screenheight() / 2, anchor='sw')
        action_scroll = Scrollbar(start_window, troughcolor='grey'
                                  , width=270, orient="horizontal"
                                  , elementborderwidth=0, bg='white')
        action_scroll.place(x=390, y=start_window.winfo_screenheight() / 2 + 85
                            , anchor='nw')
        action_listbox = Listbox(start_window, font=('Minecraft AE', 20)
                                 , yscrollcommand=action_scroll, height=10)
        action_listbox.place(x=0, y=start_window.winfo_screenheight() / 2 + 100
                             , anchor='nw')
        start_window.update()
        testing()

    click_screen()

    start_window.mainloop()

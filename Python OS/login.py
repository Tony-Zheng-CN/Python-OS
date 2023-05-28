from tkinter import *
from PIL import Image, ImageTk
import pyautogui as pag
from main import *
from register import *
from start import start

try:
    username = open(r'username', 'r').read()
    password = open(r'password', 'r').read()

    if password == pag.password(title='登录', text='用户:' + username):
        start()
    else:
        print('密码错误')
        exit()
except FileNotFoundError:
    reg()
    start()


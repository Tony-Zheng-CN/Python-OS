def reg():
    username = input('用户名:')
    password = input('密码:')

    username_txt = open('username', 'w+')
    password_txt = open('password', 'w+')
    username_txt.write(username)
    password_txt.write(password)

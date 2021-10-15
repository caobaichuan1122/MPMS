import os
import tkinter
import pymysql
from pathlib import Path
import tkinter.messagebox
import sys
import tkinter.font as tf
from tkinter import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./image")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loginpage():
    global window
    window = Tk()
    window.title('Monash Patient Management System')
    window.geometry("845x468")
    window.configure(bg = "#FFFFFF")
    global user
    global pwd

    canvas = Canvas(
        bg = "#FFFFFF",
        height = 468,
        width = 845,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("log/image_1.png"))
    image_1 = canvas.create_image(
        261.0,
        237.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("log/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        680.0,
        167.0,
        image=entry_image_1
    )
    user = Entry(
        bd=0,
        bg="#E8E8E8",
        highlightthickness=0,
         font = '12',
    )
    user.place(
        x=561.0,
        y=147.0,
        width=238.0,
        height=38.0
    )

    user.insert(0,'example@monash.edu')


    entry_image_2 = PhotoImage(
        file=relative_to_assets("log/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        680.0,
        246.0,
        image=entry_image_2
    )
    pwd = Entry(
        bd=0,
        bg="#E8E8E8",
        highlightthickness=0,
        show = '*'
    )
    pwd.place(
        x=561.0,
        y=226.0,
        width=238.0,
        height=38.0
    )
    pwd.insert(0,'password:')

    button_login_1 = PhotoImage(
        file=relative_to_assets("log/button_1.png"))
    login = Button(
        image=button_login_1,
        borderwidth=0,
        highlightthickness=0,
        command= login_verify,
        relief="flat"
    )
    login.place(
        x=688.0,
        y=353.0,
        width=108.0,
        height=36.0
    )

    button_register_2 = PhotoImage(
        file=relative_to_assets("log/button_2.png"))
    register = Button(
        image=button_register_2,
        borderwidth=0,
        highlightthickness=0,
        command= user_register,
        relief="flat"
    )
    register.place(
        x=564.0,
        y=353.0,
        width=108.0,
        height=36.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("log/image_2.png"))
    image_2 = canvas.create_image(
        680.0,
        79.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()

def user_register():
    global register_screen
    register_screen = Toplevel(window)
    register_screen.title("Registration")
    register_screen.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="entry", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="account * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="registration", width=10, height=1, bg="white", command=register_user).pack()

def login_verify():
    username1 = user.get()
    password1 = pwd.get()
    # user.delete(0,-1)
    pwd.delete(0,'end')
    conn = pymysql.connect(host='34.129.105.0', user='Team27', password='Team_27_yu', db='team27', port=3306, charset='utf8')
    cur = conn.cursor()
    select_sql = "select password,account from user WHERE account=%s"
    cur.execute(select_sql,[username1])
    result = cur.fetchone()
    if result is None:
        tkinter.messagebox.showerror('error','username error!')
    else :
        if result[0] == password1 and result[1] == username1:
            if result[1] == 'admin@monash.edu':
                window.destroy()
                os.system("python admin_control.py")
            else:
                window.destroy()
                os.system("python controller.py")
        elif result[0] != password1:
            tkinter.messagebox.showerror('error','password error!')
    cur.close()
    conn.close()

def register_user():
    username_info = username.get()
    password_info = password.get()
    conn = pymysql.connect(host='34.129.105.0', user='Team27', passwd='Team_27_yu', db='team27', port=3306, charset='utf8')
    cur = conn.cursor()

    select_sql = "select account from user WHERE password=%s"
    cur.execute(select_sql, [username_info])
    result = cur.fetchone()
    if result is None:
        sql = 'insert into user(account,password)' \
              'values("%s","%s")' % \
              (username_info, password_info)
        try:
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        except:
            conn.rollback()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(register_screen, text="registration success！", fg="green").pack()

loginpage()



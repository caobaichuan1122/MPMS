import tkinter
import pymysql
from pathlib import Path
import tkinter.messagebox
import tkinter.font as tf
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./image")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def user_register():
    global window1
    window1 = Toplevel(window)

    window1.geometry("446x612")
    window1.configure(bg="#FFFFFF")

    canvas1 = Canvas(
        bg="#FFFFFF",
        height=612,
        width=446,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas1.place(x=0, y=0)
    image_logo = PhotoImage(
        file=relative_to_assets("register/image_1.png"))
    image_1 = canvas1.create_image(
        224.0,
        87.0,
        image=image_logo
    )

    entry_image_user = PhotoImage(
        file=relative_to_assets("register/entry_1.png"))
    entry_bg_1 = canvas1.create_image(
        224.0,
        193.0,
        image=entry_image_user
    )
    entry_1 = Entry(
        bd=0,
        bg="#E2E6E8",
        highlightthickness=0
    )
    entry_1.place(
        x=105.0,
        y=173.0,
        width=238.0,
        height=38.0
    )

    entry_image_pwd = PhotoImage(
        file=relative_to_assets("register/entry_2.png"))
    entry_bg_2 = canvas1.create_image(
        224.0,
        297.0,
        image=entry_image_pwd
    )
    entry_2 = Entry(
        bd=0,
        bg="#E3E7E9",
        highlightthickness=0
    )
    entry_2.place(
        x=105.0,
        y=277.0,
        width=238.0,
        height=38.0
    )

    entry_image_pwd1 = PhotoImage(
        file=relative_to_assets("register/entry_3.png"))
    entry_bg_3 = canvas1.create_image(
        224.0,
        401.0,
        image=entry_image_pwd1
    )
    entry_3 = Entry(
        bd=0,
        bg="#E3E7E9",
        highlightthickness=0
    )
    entry_3.place(
        x=105.0,
        y=381.0,
        width=238.0,
        height=38.0
    )

    button_image_sub = PhotoImage(
        file=relative_to_assets("register/button_1.png"))
    button_1 = Button(
        image=button_image_sub,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=154.0,
        y=485.0,
        width=139.0,
        height=36.0
    )


def login_verify():
    username1 = user.get()
    password1 = pwd.get()
    # user.delete(0,-1)
    pwd.delete(0,'end')
    conn = pymysql.connect(host='34.129.150.96', user='Team27', password='Team_27_yu', db='team27', port=3306, charset='utf8')
    cur = conn.cursor()
    select_sql = "select pw from user WHERE un=%s"
    cur.execute(select_sql,[username1])
    result = cur.fetchone()
    if result is None:
        tkinter.messagebox.showerror('error','username error!')
    else :
        if result[0] == password1:
            tkinter.messagebox.showinfo('info','login sucess!')
        elif result[0] != password1:
            tkinter.messagebox.showerror('error','password error!')


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
        command=user_register,
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

loginpage()



from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# def register():
#     OUTPUT_PATH = Path(__file__).parent
#     ASSETS_PATH = OUTPUT_PATH / Path("./image/register")
#
#
#     def relative_to_assets(path: str) -> Path:
#         return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("446x612")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    bg = "#FFFFFF",
    height = 612,
    width = 446,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=("./image/register/image_1.png"))
image_1 = canvas.create_image(
    224.0,
    87.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=("./image/register/entry_1.png"))
entry_bg_1 = canvas.create_image(
    224.0,
    193.0,
    image=entry_image_1
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

entry_image_2 = PhotoImage(
    file=("./image/register/entry_2.png"))
entry_bg_2 = canvas.create_image(
    224.0,
    297.0,
    image=entry_image_2
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

entry_image_3 = PhotoImage(
    file=("./image/register/entry_3.png"))
entry_bg_3 = canvas.create_image(
    224.0,
    401.0,
    image=entry_image_3
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

button_image_1 = PhotoImage(
    file=("./image/register/button_1.png"))
button_1 = Button(
    image=button_image_1,
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
window.resizable(False, False)
window.mainloop()


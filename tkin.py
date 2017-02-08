from Tkinter import *
import tkFileDialog
from PIL import Image, ImageTk
import exifread
from tkinter import messagebox

# global vars

filename_left = None
filename_right = None


def callback():
    print "adfasfkjadfkj"


def get_meta_data():
    tags = exifread.process_file(open(filename.name, 'rb'))
    # datum = tags['GPS GPSMapDatum'].printable
    # make = tags['Image Make'].printable
    model = tags['Image Model'].printable
    latitude = tags['GPS GPSLatitude'].values[0].num + tags['GPS GPSLatitude'].values[1].num / float(60) + \
               tags['GPS GPSLatitude'].values[2].num / (float(3600) * tags['GPS GPSLatitude'].values[2].den)

    longitude = tags['GPS GPSLongitude'].values[0].num + tags['GPS GPSLongitude'].values[1].num / float(60) + \
                tags['GPS GPSLongitude'].values[2].num / (float(3600) * tags['GPS GPSLongitude'].values[2].den)

    messagebox.showinfo(message="Latitude: %s\nLongitude: %s"%(latitude, longitude))

    return "adfa"


def callback_click(e):
    messagebox.showinfo(message="clicked at x: %s, y:%s"%(e.x, e.y))
    return


def open_left_img():
    global filename_left
    filename_left = tkFileDialog.askopenfile()
    fp = open(filename_left.name)
    img = ImageTk.PhotoImage(file=fp)

    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel_left = Label(root, image=img)
    panel_left.image = img
    panel_left.bind('<Button-1>', callback_click)
    # The Pack geometry manager packs widgets in rows or columns.
    #panel_left.pack(side="left", padx=10, pady=10)
    panel_left.grid(row=1,
                    column=1,
                    rowspan=10,
                    columnspan=10)

    return filename_left


def open_right_img():
    global filename_right
    filename_right = tkFileDialog.askopenfile()
    fp = open(filename_right.name)
    img = ImageTk.PhotoImage(file=fp)

    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel_right = Label(root, image=img)
    panel_right.image = img
    panel_right.bind('<Button-1>', callback_click)
    # The Pack geometry manager packs widgets in rows or columns.
    #panel_right.pack(side="right", padx=10, pady=10)
    panel_right.grid(row=15,
                     column=1,
                     rowspan=10,
                     columnspan=10)

    return filename_right

root = Tk()

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New", command=callback)
file_menu.add_command(label="Open Left", command=open_left_img)
file_menu.add_command(label="Open Right", command=open_right_img)
file_menu.add_command(label="Open Right", command=open_right_img)
file_menu.add_separator()
file_menu.add_command(label="exit", command=callback)

help_menu = Menu(menu)
menu.add_cascade(label="help", menu=help_menu)
help_menu.add_command(label="about", command=get_meta_data)


root.mainloop()

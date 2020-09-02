# Author: Eric Orellana
# This file when run will present a window that will give the option of
# stating a server or a client messaging system.

from tkinter import *
import os

top = Tk()
top.title("Pigeon Coop")

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'pigeon.gif')
photo = PhotoImage(file=image_path)
l1 = Label(image = photo)
l1.image = photo

def server():
    import Server

def client():
    import Client

B0 = Button(top, text = "Create a Server", command = server)
B1 = Button(top, text = "Connect to a Server", command = client)
L0 = Label(top, text = "Choose an option below:")

top.resizable(width=False, height=False)
l1.pack(side = TOP)
L0.pack(side = TOP, expand = YES)
B0.pack(side = TOP, expand = YES)
B1.pack(side = TOP, expand = YES)
top.mainloop()

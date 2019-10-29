from tkinter.messagebox import showinfo
from tkinter import *

def show_application():
    root = Tk()

    frame_start = Frame(master=root, pady=30, padx=30)
    frame_start.pack()

    username = Entry(master=frame_start)
    username.pack()

    btn_message = Button(master=frame_start, text='Example without param', command=say_hi_user)
    btn_message.pack()

    btn_message = Button(master=frame_start, text='Example with param', command=say_hello(username.get()))
    btn_message.pack()

    btn_message = Button(master=frame_start, text='Example with lambda', command=lambda: say_hello(username.get()))
    btn_message.pack()

    root.mainloop()


def say_hi_user():
    showinfo(title='popup', message='Hi, user!')


def say_hello(username):
    showinfo(title='popup', message='Hello, {}!'.format(username))


def say_bye(username):
    showinfo(title='popup', message='Bye, {}!'.format(username))


show_application()
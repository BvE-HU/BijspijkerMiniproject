from tkinter import *


def show_application():
    root = Tk()

    frame_start = Frame(master=root, pady=30, padx=30)
    frame_departures = create_departures_frame(root, frame_start)

    frame_start.grid(column=0, row=0, sticky="nsew")
    frame_departures.grid(column=0, row=0, sticky="nsew")

    btn_show_departures = Button(master=frame_start, text='Toon Vertrektijden', command=frame_departures.tkraise)
    btn_show_departures.pack()

    frame_start.tkraise()
    root.mainloop()


def create_departures_frame(root, frame_previous):
    frame_departures = Frame(master=root, pady=40, padx=40)

    return frame_departures


def show_departures(txt_output, departure):
    pass


def load_departures_NS(station):
    pass


show_application()
# Mike Gorman
# 13.1 name and address


# Write a GUI program that displays your name and address when a button
# is clicked (you can use the address of the school). The program’s window
# should resemble the sketch on the far left side of figure 13-26 when it runs.
# When the user clicks the Show Info button, the program should display your name
# and address as shown in the sketch on the right of the figure.

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # create StringVar objects for name, street, city
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.city_value = tkinter.StringVar()

        # create frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create label widgets
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.city_label = tkinter.Label(self.info_frame, textvariable=self.city_value)

        # pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.city_label.pack()

        # create the buttons
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # enter the main loop
        tkinter.mainloop()

    # show info function
    def show(self):
        self.name_value.set('Mike Gorman')
        self.street_value.set('2808 Stilling Blvd')
        self.city_value.set('McHenry, Il 60050')

# call MyGUI
my_gui = MyGUI()

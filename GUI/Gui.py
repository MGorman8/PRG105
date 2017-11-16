# import required library TK Interface

import tkinter


class MyGUI:
    def __init__(self):
        # create the main window from tkinter
        self.main_window = tkinter.Tk()

        # create a label (widget) to contain 'Hello World'
        self.label_1 = tkinter.Label(self.main_window, text="Good Evening!")
        self.label_2 = tkinter.Label(self.main_window, text='I am tired. :(')
        # pack label to make it referenceable to the main window
        #       (side='left' is left align...'right' is right align... also 'top' and 'bottom'
        self.label_1.pack()
        self.label_2.pack()
        # enter the main loop of TKinter
        tkinter.mainloop()


def main():
    MyGUI()

main()

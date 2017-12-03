# Mike Gorman
# 13.3 Miles Per Gallon

# Write a GUI program that calculates a car’s gas mileage.
# The program’s window should have Entry widgets that let the user enter
# the number of gallons of gas the car holds, and the number of miles it
# can be driven on a full tank. When a Calculate MPG button is clicked,
# the program should display the number of miles that the car may be driven
# per gallon of gas. Use the following formula to calculate miles per gallon:

# MPG = miles / gallons
# Make sure you label Entry widgets and results appropriately.
# Document appropriately with comments, upload to GitHub and hand in a link to the code.


import tkinter
import tkinter.messagebox


class MPGGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()

        # create frames for top will hold number of gallons entry widget,
        # mid frame will hold number of miles driven
        # bottom frame will hold buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create the widgets for the top frame
        self.gallons_label = tkinter.Label(self.top_frame, text='How many gallons is your gas tank? ',bg='antiquewhite1')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10, bg='lightblue')

        # pack top frame widgets
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='right')

        # create middle frame widgets
        self.miles_label = tkinter.Label(self.mid_frame, text='How many miles did you drive?        ',bg='antiquewhite1')
        self.miles_entry = tkinter.Entry(self.mid_frame, width=10, bg='lightblue')

        # need StringVar object to associate with the label;
        # use set method to store blank characters
        self.value = tkinter.StringVar()

        # create the label to pair with the stringvar object
        # self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # pack mid frame widgets
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='right')

        # create buttons in the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert, bg='lightgreen')
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy, bg='red')

        # pack buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # enter tkinter main loop
        tkinter.mainloop()

    # convert method/function
    def convert(self):
        # Get the value the user entered into kilo_entry widget.
        # mpg = miles/gallons

        # put user data into variables
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())

        # math
        num_mpg = miles / gallons
        # format 2 decimals
        str_mpg = f'{num_mpg:.2f}'

        # convert miles per gallon to a string
        mpg = str(str_mpg)

        # display the result in a dialogue box
        tkinter.messagebox.showinfo('MPG\'s', 'You got ' + mpg + ' miles per gallon on that tank of fuel.')


miles_per_gallon = MPGGUI()

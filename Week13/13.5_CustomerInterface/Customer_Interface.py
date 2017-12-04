# Mike Gorman
# 13.5 Customer Interface

# Make up an interface for a business offering 7-10 services or products with prices.
# Write a GUI program to allow the user to click buttons to add services or products
# and show total at the bottom. Make sure all necessary labels and instructions to
# the user are included in your GUI.

# Possibilities: Garage, Salon, Coffee shop..... Document well and hand in on GitHub.

import tkinter


class ShopGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create frames -- top/title, check boxes and prices, total, bottom/buttons
        self.title_frame = tkinter.Frame(self.main_window)
        self.check_box_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # label for title frame
        self.title_label = tkinter.Label(self.title_frame, width=35, font=('fixedsys', 18),
                                         text='Welcome to Watto\'s Discount Yard', fg='yellow', bg='darkgreen')
        # pack the title label
        self.title_label.pack(side='top')

        # label for instructions in check_box_frame
        self.check_box_label = tkinter.Label(self.check_box_frame, width=51, font=('courier new', 14),
                                             text='Select the items you wish to purchase', fg='yellow', bg='darkgreen')
        # pack the instructions label
        self.check_box_label.pack(side='top')

        # create the IntVar objects for checkboxes
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()
        self.cb_var9 = tkinter.IntVar()
        self.cb_var10 = tkinter.IntVar()

        # set checkboxes to unchecked
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)
        self.cb_var9.set(0)
        self.cb_var10.set(0)

        # create the checkbox widgets
        self.cb1 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$9.53                     Jug of Blue Milk',
                                       variable=self.cb_var1, bg='lightblue')
        self.cb2 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$2,300.00              Mostly working Speeder',
                                       variable=self.cb_var2, bg='lightblue')
        self.cb3 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$67.34                   Blaster Power Cell',
                                       variable=self.cb_var3, bg='lightblue')
        self.cb4 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$53.33                   1lb of scrap from Jabba\'s Sail Barge',
                                       variable=self.cb_var4, bg='lightblue')
        self.cb5 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$3.22                     Grilled Wamp Rat',
                                       variable=self.cb_var5, bg='lightblue')
        self.cb6 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$1,293.00               Power Droid',
                                       variable=self.cb_var6, bg='lightblue')
        self.cb7 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$7,933.00               Hyper Drive for Nubian Capital Ship',
                                       variable=self.cb_var7, bg='lightblue')
        self.cb8 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$99.99                    Kyber Crystal',
                                       variable=self.cb_var8, bg='lightblue')
        self.cb9 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                       text='$19,854.37             Interdimentional Phonebooth',
                                       variable=self.cb_var9, bg='lightblue')
        self.cb10 = tkinter.Checkbutton(self.check_box_frame, width=40, anchor='w',
                                        text='$1,000,000.00        Death Star Plans',
                                        variable=self.cb_var10, bg='lightblue')

        # pack the checkboxes
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()
        self.cb9.pack()
        self.cb10.pack()

        # create total frame widget
        self.total_label = tkinter.Label(self.total_frame, text='Your bill is $')

        # StringVar for total label
        self.total = tkinter.StringVar()
        self.total_bill_label = tkinter.Label(self.total_frame, textvariable=self.total)

        # pack total widgets
        self.total_label.pack()
        self.total_bill_label.pack()

        # create buttons in the bottom frame
        self.calc_button = tkinter.Button(self.button_frame, text="Total", command=self.total, bg='lightgreen')
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy, bg='red')

        # pack buttons
        self.calc_button.pack(side='left', padx=40)
        self.quit_button.pack(side='right', padx=40)

        # pack the frames
        self.title_frame.pack()
        self.check_box_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        # enter the main loop
        tkinter.mainloop()

# total function/method
    def total(self):
        total_bill = float(0.00)

        if self.cb_var1.get() == 1:
            total_bill += 9.53
        if self.cb_var2.get() == 1:
            total_bill = total_bill + 2300.00
        if self.cb_var3.get() == 1:
            total_bill = total_bill + 67.34
        if self.cb_var4.get() == 1:
            total_bill = total_bill + 53.33
        if self.cb_var5.get() == 1:
            total_bill = total_bill + 3.22
        if self.cb_var6.get() == 1:
            total_bill = total_bill + 1293.00
        if self.cb_var7.get() == 1:
            total_bill = total_bill + 7933.00
        if self.cb_var8.get() == 1:
            total_bill = total_bill + 99.99
        if self.cb_var9.get() == 1:
            total_bill = total_bill + 19854.37
        if self.cb_var10.get() == 1:
            total_bill = total_bill + 1000000


        # convert total bill into string and store as total
        total = '{:.2f}'.format(total_bill)
        self.total.set(total)


Shop_Gui = ShopGUI()

# -*- coding: iso-8859-1 -*-


from tkinter import *
from threading import *
from os import listdir
from tkinter import messagebox


class frame():

    def __init__(self):
        self.mainframe = Tk(className=" Schwingung")
        #self.mainframe.wm_iconbitmap("Icon.ico")


        self.integer1 = IntVar()
        self.boolean1 = True

        self.string1 = StringVar()
        self.string2 = StringVar()

        self.string3 = StringVar()
        self.string4 = ""


        self.string2.set("Courier")

        self.mainframe.M = Menu(self.mainframe)

        self.mainframe.M.m = Menu(self.mainframe.M, tearoff =0)

        self.mainframe.M.m.add_radiobutton(label = "rot", variable = self.string1, value = "800")
        self.mainframe.M.m.add_radiobutton(label = "grün", variable = self.string1, value = "080")
        self.mainframe.M.m.add_radiobutton(label = "blau", variable = self.string1, value = "008")

        self.mainframe.M.m.m1 = Menu(self.mainframe.M.m,tearoff =0)

        self.mainframe.M.m.m1.add_radiobutton(label = "weiß", variable = self.integer1, value = 1)
        self.mainframe.M.m.m1.add_radiobutton(label = "schwarz", variable = self.integer1, value = 2)

        self.mainframe.M.m.add_cascade(menu = self.mainframe.M.m.m1, label = "Helligkeit")

        self.mainframe.M.add_cascade(menu = self.mainframe.M.m, label = "Farbe")


        self.mainframe.M.add_command(label= "Ändern", command = self.color)



        self.mainframe.config(menu = self.mainframe.M)



        self.mainframe.canvas1 = Canvas(master = self.mainframe ,width = "35c", height = "20c", background = "#080")
        self.mainframe.canvas1.pack(fill = BOTH, expand = 1)


        for i in range(-40,300,6):
            self.mainframe.canvas1.create_oval(350-i,350-i,450+i,450+i, outline = "#900", width = 1.1)

        for i in range(-40,300,12):
            self.mainframe.canvas1.create_oval(350-i,350-i,450+i,450+i, outline = "#009", width = 1.1)

        for i in range(-40,300,6):
            self.mainframe.canvas1.create_oval(742-i,350-i,842+i,450+i, outline = "#900", width = 1.1)

        for i in range(-40,300,12):
            self.mainframe.canvas1.create_oval(742-i,350-i,842+i,450+i, outline = "#009", width = 1.1)

        self.mainframe.canvas1.create_line(1242,400,42,400)
        self.mainframe.canvas1.create_line(596,50,596,800)

        self.mainframe.mainloop()




    def color(self):
        if self.string1.get() != "":
            self.s =  "#" + str(self.string1.get())
            if self.integer1.get()==1 :
                self.s =self.s.replace("8", "C")
            elif self.integer1.get()==2:
                self.s =self.s.replace("8", "4")
            self.mainframe.canvas1.config(background = self.s)
            #self.mainframe.canvas1.empty1.config(background = self.s)

        if self.integer1.get() != 0 and self.boolean1:
            self.mainframe.M.m.m1.add_radiobutton(label = "neutral", variable = self.integer1, value = 0)
            self.boolean1 = False
        elif self.integer1.get() == 0:
            self.mainframe.M.m.m1.delete(2)
            self.boolean1 = True





window = frame()


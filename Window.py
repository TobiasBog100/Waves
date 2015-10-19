# -*- coding: iso-8859-1 -*-


from tkinter import *
from threading import *
from os import listdir
from tkinter import messagebox


class frame():

    def __init__(self):
        self.mainframe = Tk(className=" C++ Umwandler")
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

        self.mainframe.M.add_separator()
        self.mainframe.M.add_command(label= "Speichern", command = self.safer1)

        self.mainframe.config(menu = self.mainframe.M)



        self.mainframe.canvas1 = Canvas(master = self.mainframe ,width = "10c", height = "10c", background = "#080")
        self.mainframe.canvas1.pack(fill = BOTH, expand = 1)


        self.mainframe.canvas1.SpeicherN = Label(master=self.mainframe.canvas1, text = "Speicherortname:").grid(row=0 , column=1, pady="5m", sticky= W)
        self.mainframe.canvas1.SpeicherOrt = Entry(master=self.mainframe.canvas1, textvariable=self.string3, width=40).grid(row=0 , column=1, pady="5m", padx="32m", sticky= W)

        self.mainframe.canvas1.empty1 = Label(master= self.mainframe.canvas1, background="#080")
        self.mainframe.canvas1.empty1.grid(row=1, column=0,padx="2.5m")


        self.mainframe.canvas1.bary = Scrollbar(master = self.mainframe.canvas1, orient=VERTICAL)
        self.mainframe.canvas1.bary.grid(row=1 , column=2, sticky="NS")

        self.mainframe.canvas1.barx = Scrollbar(master = self.mainframe.canvas1, orient=HORIZONTAL)
        self.mainframe.canvas1.barx.grid(row=2 , column=1, sticky="EW")

        self.mainframe.canvas1.editor = Text(master= self.mainframe.canvas1 ,yscrollcommand = self.mainframe.canvas1.bary.set, xscrollcommand = self.mainframe.canvas1.barx.set ,font="Courier",relief = SUNKEN, height=20 ,width=70, wrap=NONE)


        self.mainframe.canvas1.bary.config(command = self.mainframe.canvas1.editor.yview)
        self.mainframe.canvas1.barx.config(command = self.mainframe.canvas1.editor.xview)
        self.mainframe.canvas1.editor.grid(row=1 , column=1, sticky="E")

        self.mainframe.canvas1.Button1 = Button(master= self.mainframe.canvas1, text="Umwandeln", command= self.changer)
        self.mainframe.canvas1.Button1.grid(row=3, column=1, pady="5m")

        self.mainframe.canvas1.Checkbutton1 = Checkbutton(master= self.mainframe.canvas1, onvalue="Courier" , offvalue="Arial", command=self.Schrift,indicatoron=False,variable=self.string2, textvariable=self.string2,width =6 )
        self.mainframe.canvas1.Checkbutton1.grid(row=3, column=1, pady="5m", padx="5m", sticky=W)

        self.mainframe.canvas1.endtext = Label(master=self.mainframe.canvas1,text="Präsentiert\nvon\nPython\nund C++",font=("Arial",12))
        self.mainframe.canvas1.endtext.grid(row=3, column=3)


        self.mainframe.mainloop()




    def color(self):
        if self.string1.get() != "":
            self.s =  "#" + str(self.string1.get())
            if self.integer1.get()==1 :
                self.s =self.s.replace("8", "C")
            elif self.integer1.get()==2:
                self.s =self.s.replace("8", "4")
            self.mainframe.canvas1.config(background = self.s)
            self.mainframe.canvas1.empty1.config(background = self.s)

        if self.integer1.get() != 0 and self.boolean1:
            self.mainframe.M.m.m1.add_radiobutton(label = "neutral", variable = self.integer1, value = 0)
            self.boolean1 = False
        elif self.integer1.get() == 0:
            self.mainframe.M.m.m1.delete(3)
            self.boolean1 = True





    def safer1(self):
        self.string4=self.mainframe.canvas1.editor.get(1.0,END)
        self.string5 = self.string3.get()
        if self.string5 !="" or self.string4!="":
            Hintergrund = Stocktxt(self.string5,self.string4, False)
            Hintergrund.start()


    def changer(self):
        self.string4=self.mainframe.canvas1.editor.get(1.0,END)
        self.string5 = self.string3.get()
        if self.string5 !="" or self.string4!="":
            Hintergrund = Stocktxt(self.string5,self.string4, True)
            Hintergrund.start()



    def Schrift(self):

        if self.string2.get()=="Courier":

            self.mainframe.canvas1.editor.config(font="Courier")
        else:

            self.mainframe.canvas1.editor.config(font="Arial")



class Stocktxt(Thread):

    def __init__(self, ort ,text, boolean):
        Thread.__init__(self)
        self.o = ort+".txt"
        self.t = str(text)
        self.b = boolean

    def run(self):
        if self.o in listdir():
            self.ask= messagebox.askyesno("Überschreibungswarnung","Datei existiert bereits!!!\nWollen sie sie überschreiben?")
            if not self.ask:
                return 0


        self.stock = open(self.o,"w")
        self.stock.write(self.t)
        self.stock.close()
        if self.b:
                self.code = open("Code.txt","w")
                self.code.write("T")
                self.code.close()

        return 0


window = frame()


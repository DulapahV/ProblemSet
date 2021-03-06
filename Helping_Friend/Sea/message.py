from tkinter import *
import datetime

class main:
    def __init__(self):
        window1 = Tk()
        window1.title("Age Calculator")
        window1.geometry("620x780")
        image1 = PhotoImage(file=r'C:\Users\Dulapah Vibulsanti\OneDrive\Documents\GitHub\ProblemSet\Helping_Friend\Sea\agecalc.gif')
        Label(window1, image= image1).grid()
        n = Label(text="Name:")
        year = Label(text="Birth's Year(A.D.):")
        month = Label(text="Month:")
        date = Label(text="Day:")
        value1 = list(range(1940, 2023))
        self.y = IntVar(value=2021)
        value2 = list(range(1,13))
        self.m = IntVar(value=1)
        value3 = list(range(1,32))
        self.d = IntVar(value=1)
        self.nameEntry = Entry()
        self.yearEntry = OptionMenu(window1, self.y, *value1)
        self.monthEntry = OptionMenu(window1, self.m, *value2)
        self.dateEntry = OptionMenu(window1, self.d, *value3)
        n.grid(column=0, row=1, sticky ="w", padx=256)
        year.grid(column=0, row=2,sticky ="w",padx=200)
        month.grid(column=0, row=3,sticky ="w",padx=253)
        date.grid(column=0, row=4,sticky ="w",padx=269)
        self.nameEntry.grid(column=0, row=1)
        self.yearEntry.grid(column=0, row=2)
        self.monthEntry.grid(column=0, row=3)
        self.dateEntry.grid(column=0, row=4)
        self.exit = Button(window1, text="Exit", width=5, command=window1.destroy,bg="yellow")
        self.exit.grid(column=0, row=6)
        button = Button(window1, text="Calculate Age", command=self.getInput, bg="light blue")
        button.grid(column=0, row=5, pady=10)
        window1.mainloop()
    def getInput(self):
        window2 = Tk()
        name = self.nameEntry.get()
        if True in [char.isdigit() for char in name]:
            print("Invalid")
            exit(0)
        try:
            if self.d.get() == 31:
                if self.m.get() == 4 or self.m.get() == 6 or self.m.get() == 9 or self.m.get() == 11:
                    raise IndexError
        except:
            print("Invalid")

        if self.m.get() == 2 and self.d.get() > 29:
            print("Invalid")
            exit(0)
        try:
            if not (self.y.get() % 4) == 0:
                if not (self.y.get() % 100) == 0:
                    if not (self.y.get() % 400) == 0:
                        if self.d.get() >= 28 and self.m.get() == 2:
                            raise IndexError
        except:
            print("Invalid")
            exit(0)
        Yourname = Person(name, datetime.date(self.y.get(), self.m.get(), self.d.get()))
        textArea = Text(master=window2, height=10, width=25)
        textArea.grid(column=0, row=6)
        answer = " !Hello *{Yourname}*!.\n !*You are {age} years old*!".format(Yourname = name, age = Yourname.age())
        self.exit = Button(window2, text="Exit", width=10, command=window2.destroy,bg="yellow")
        self.exit.grid(column=5, row=6)
        textArea.insert(END, answer)
class Person(main):
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if age <= 0:
            print("Invalid")
            exit(0)
        return age

main()
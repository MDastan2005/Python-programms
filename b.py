from tkinter import *
from math import sqrt, factorial, sin, cos, radians


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 30, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "√", "=",
            "1", "2", "3", "/", "X!",
            "4", "5", "6", "+", "sin",
            "7", "8", "9", "-", "cos",
            ".", "0", "(", ")", "X^2",
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 20),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 500:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            result = []
            try:
                result.append(str(round((eval(self.formula)) ** 2, 16)))
            except:
                result.append("ERROR!")
            self.formula = result[0]
        elif operation == "=":
            result = []
            try:
                result.append(str(round((eval(self.formula)), 16)))
            except:
                result.append("ERROR!")
            self.formula = result[0]
        elif operation == "√":
            result = []
            try:
                number = round(sqrt(eval(self.formula)), 16)
                intnumber = int(number)
                result.append(str(intnumber if number - intnumber < 1e-15 else number))
            except:
                result.append("ERROR!")
            self.formula = result[0]
        elif operation == "X!":
            result = []
            try:
                result.append(str(factorial(eval(self.formula))))
            except:
                result.append("ERROR!")
            self.formula = result[0]
        elif operation == "sin":
            result = []
            try:
                result.append(str(round(sin(radians(eval(self.formula))), 15)))
            except:
                result.append("ERROR!")
            self.formula = result[0]
        elif operation == "cos":
            result = []
            try:
                result.append(str(round(cos(radians(eval(self.formula))), 15)))
            except:
                result.append("ERROR!")
            self.formula = result[0]
        else:
            if self.formula == "0" or self.formula == "ERROR!":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("602x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()

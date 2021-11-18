from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from unitconvert import lengthunits

class Window():
    def __init__(self):
        # Varaibles

        self.units_dict = {
            'Meter' : 'm',
            'Kilometer' : 'km',
            'Centimeter' : 'cm',
            'Milimeter' : 'mm',
            'Mile' : 'mi',
            'Yard' : 'yd',
            'Foot' : 'ft',
            'Inch' : 'in',
        }

        self.from_menu_options = [
            'Select',
            'Meter',
            'Kilometer',
            'Centimeter',
            'Milimeter',
            'Mile',
            'Yard',
            'Foot',
            'Inch',
        ]

        self.to_menu_options = [
            'Select',
            'Meter',
            'Kilometer',
            'Centimeter',
            'Milimeter',
            'Mile',
            'Yard',
            'Foot',
            'Inch',
        ]
        

        self.win = Tk()
        self.win.title("Unit Converter")
        self.win.resizable(False, False)
        self.win.configure(bg="#a1d3ff")
        self.win.bind('<Return>', lambda e: self.convert())
        self.draw()
        self.win.mainloop()

    def convert(self):
        try:
            self.output = lengthunits.LengthUnit(float(self.from_input.get()), self.units_dict[self.from_menu_variable.get()], self.units_dict[self.to_menu_variable.get()]).doconvert()
            self.to_value.configure(text=f'{round(self.output, 2)}')
        except:
            messagebox.showerror("Error", "Please enter a Number only !")
            
    def draw(self):
        # Dropdown menu - From and To

        self.from_menu_variable = StringVar()
        self.from_menu = Combobox(self.win, font=("Bulleto Killa",10,"bold"), textvariable=self.from_menu_variable, state="readonly")
        self.from_menu['values'] = self.from_menu_options
        self.from_menu.current(0)
        self.from_menu.grid(row=0, column=0, padx=10, pady=10)

        # to Label

        self.to_label = Label(self.win, text="To", font=("Comic Sans MS",20,"bold"), bg="#a1d3ff")
        self.to_label.grid(row=0, column=1)

        self.to_menu_variable = StringVar()
        self.to_menu = Combobox(self.win, textvariable=self.to_menu_variable, font=("Bulleto Killa",10,"bold"), state="readonly")
        self.to_menu['values'] = self.to_menu_options
        self.to_menu.current(0)
        self.to_menu.grid(row=0, column=2, padx=10, pady=10)

        # input boxes

        self.from_input_variable = IntVar()
        self.from_input = Entry(self.win, textvariable=self.from_input_variable, font=("Comic Sans MS",15), width=13)
        self.from_input.grid(row=1, column=0, padx=10, pady=10)

        self.to_value = Label(self.win, text="OUTPUT", font=("Comic Sans MS",20,"bold"), bg="#a1d3ff", fg="black")
        self.to_value.grid(row=1, column=2, padx=5, pady=10)

class Converter():
    pass

if __name__ == '__main__':
    my_class = Window()

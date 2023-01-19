import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class Cuboid:
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b
        self.height = h

    def calculate_CSA(self):    # Curved surface area / Lateral surface area
        CSA = 2 * self.height * ( self.length + self.breadth )
        return CSA

    def calculate_TSA(self):
        TSA = 2 * ( self.length * self.breadth + self.breadth * self.height + self.height * self.length)
        return TSA

    def calculate_perimeter(self):    # Curved surface area / Lateral surface area
        perimeter = 4 * ( self.length + self.breadth + self.height )
        return perimeter

    def calculate_vol(self):
        vol = self.length * self.breadth * self.height
        return vol

    def calculate_diagonal(self):    # Curved surface area / Lateral surface area
        diagonal = ( self.length**2 + self.breadth**2 + self.height**2 ) ** (1/2)
        return diagonal
    


def CSA_button_clicked():
    try:
        l = float(length.get())
        b = float(breadth.get())
        h = float(height.get())
        cuboid = Cuboid(l,b,h)
        csa = cuboid.calculate_CSA()
        result = f'Curved Surface Area = {csa}'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


def TSA_button_clicked():
    try:
        l = float(length.get())
        b = float(breadth.get())
        h = float(height.get())
        cuboid = Cuboid(l,b,h)
        tsa = cuboid.calculate_TSA()
        result = f'Total Surface Area = {tsa}'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

def perimeter_button_clicked():
    try:
        l = float(length.get())
        b = float(breadth.get())
        h = float(height.get())
        cuboid = Cuboid(l,b,h)
        p = cuboid.calculate_perimeter()
        result = f'Perimeter = {p}'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

def vol_button_clicked():
    try:
        l = float(length.get())
        b = float(breadth.get())
        h = float(height.get())
        cuboid = Cuboid(l,b,h)
        vol = cuboid.calculate_vol()
        result = f'Volume = {vol}'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

def diagonal_button_clicked():
    try:
        l = float(length.get())
        b = float(breadth.get())
        h = float(height.get())
        cuboid = Cuboid(l,b,h)
        d = cuboid.calculate_diagonal()
        result = f'Diagonal of the cuboid = {d}'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


# for gui details and interactions

root = tk.Tk()
root.title('Cuboid details')
root.geometry('400x150')
root.resizable(False, False)

frame = ttk.Frame(root)
options = {'padx': 5, 'pady': 5}

length_label = ttk.Label(frame, text='Length')
breadth_label = ttk.Label(frame, text='Breadth')
height_label = ttk.Label(frame, text='Height')
length_label.grid(column=0, row=0, sticky='W', **options)
breadth_label.grid(column=0, row=1, sticky='W', **options)
height_label.grid(column=0, row=2, sticky='W', **options)

length = tk.StringVar()
length_entry = ttk.Entry(frame, textvariable=length)
length_entry.grid(column=1, row=0, **options)
length_entry.focus()

breadth = tk.StringVar()
breadth_entry = ttk.Entry(frame, textvariable=breadth)
breadth_entry.grid(column=1, row=1, **options)
breadth_entry.focus()

height = tk.StringVar()
height_entry = ttk.Entry(frame, textvariable=height)
height_entry.grid(column=1, row=2, **options)
height_entry.focus()

# for clicking buttons

CSA_button = ttk.Button(frame, text='CSA')
CSA_button.grid(column=2, row=0, sticky='W', **options)
CSA_button.configure(command=CSA_button_clicked)

TSA_button = ttk.Button(frame, text='TSA')
TSA_button.grid(column=2, row=1, sticky='W', **options)
TSA_button.configure(command=TSA_button_clicked)

perimeter_button = ttk.Button(frame, text='Perimeter')
perimeter_button.grid(column=3, row=0, sticky='W', **options)
perimeter_button.configure(command=perimeter_button_clicked)

vol_button = ttk.Button(frame, text='Volume')
vol_button.grid(column=3, row=1, sticky='W', **options)
vol_button.configure(command=vol_button_clicked)

diagonal_button = ttk.Button(frame, text='Diagonal')
diagonal_button.grid(column=2, row=2, sticky='W', **options)
diagonal_button.configure(command=diagonal_button_clicked)

result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()
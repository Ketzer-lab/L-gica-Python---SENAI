import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convercao():
    

taxa_dolar = {
    "USD": 1.0,
    "BRL": 5.50,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 157.00
}

root= tk.Tk()
root.title("Coversor de Moedas")

label_valor= tk.Label(root, text="Valor:").grid(row=0, column=0, sticky="e")
entry_valor= tk.Entry(root, width=25).grid(row=0, column=1)

Label_moeda= tk.Label(root, text="Origem:").grid(row=1, column=0, sticky="e")
combo_moeda= ttk.Combobox(root, width=22).grid(row=1, column=1)

label_conver= tk.Label(root, text="Convertida:").grid(row=2, column=0, sticky="e")
combo_conver= ttk.Combobox(root, width=22).grid(row=2, column=1)

button= tk.Button(root, text="Converter", command=quit).grid(row=3, column=1)

root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def conversao():

    taxa_dolar = {
    "USD": 1.0,
    "BRL": 5.50,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 157.00
    }

    valor = entry_valor.get()
    origem = combo_moeda.get()
    conver = combo_conver.get()

    calculo = valor * conver

    label_result.config(text= f"{origem}{valor} = {calculo}{calculo}")

root= tk.Tk()
root.title("Coversor de Moedas")

label_valor= tk.Label(root, text="Valor:").grid(row=0, column=0, sticky="e",padx=10, pady=10)
entry_valor= tk.Entry(root, width=25).grid(row=0, column=1, sticky="e",padx=10, pady=10)

Label_moeda= tk.Label(root, text="Origem:").grid(row=1, column=0, sticky="e",padx=10, pady=10)
combo_moeda= ttk.Combobox(root, values=["USD", "BRL", "EUR", "GBP", "JPY"], width=22).grid(row=1, column=1, sticky="e",padx=10, pady=10)

label_conver= tk.Label(root, text="Convertida:").grid(row=2, column=0, sticky="e",padx=10, pady=10)
combo_conver= ttk.Combobox(root, values=["USD", "BRL", "EUR", "GBP", "JPY"], width=22).grid(row=2, column=1, sticky="e",padx=10, pady=10)

button= tk.Button(root, text="Converter", command=conversao).grid(row=3, column=1, sticky="w",padx=10, pady=10)

label_result= tk.Label(root, text="").grid()

root.mainloop()
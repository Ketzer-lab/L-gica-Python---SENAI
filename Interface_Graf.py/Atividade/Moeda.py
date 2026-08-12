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

    try:
        valor = float(entry_valor.get())

        origem = combo_moeda.get()
        conver = combo_conver.get()

        if not origem or not conver:
            messagebox.showwarning("Erro!", "Selecione ambas as moedas")
            return

        num_origem = taxa_dolar[origem]
        num_cover = taxa_dolar[conver]

        calculo = round(valor / num_origem * num_cover, 2)
    except ValueError:
        messagebox.showwarning("Erro!", "Digite valores válidos!")

    label_result.config(text= f"{origem} {valor:.2f} = {conver} {calculo:.2f}")
    return calculo

root= tk.Tk()
root.title("Coversor de Moedas")

foto = tk.PhotoImage(file="Moeda.png")
label_foto = tk.Label(root, image=foto)
label_foto.grid(row=0, column=0, padx=10, pady=10)

label_valor= tk.Label(root, text="Valor:")
label_valor.grid(row=0, column=1, sticky="e",padx=10, pady=10)

entry_valor= tk.Entry(root, width=25)
entry_valor.grid(row=0, column=2, sticky="e",padx=10, pady=10)

Label_moeda= tk.Label(root, text="Origem:").grid(row=1, column=0, sticky="e",padx=10, pady=10)
combo_moeda= ttk.Combobox(root, values=["USD", "BRL", "EUR", "GBP", "JPY"], state="readonly", width=22)
combo_moeda.grid(row=1, column=2, sticky="e",padx=10, pady=10)

label_conver= tk.Label(root, text="Convertida:").grid(row=2, column=0, sticky="e",padx=10, pady=10)
combo_conver= ttk.Combobox(root, values=["USD", "BRL", "EUR", "GBP", "JPY"], state="readonly", width=22)
combo_conver.grid(row=2, column=2, sticky="e",padx=10, pady=10)

button= tk.Button(root, text="Converter", command=conversao)
button.grid(row=3, column=2, sticky="w",padx=10, pady=10)

label_result= tk.Label(root, text="")
label_result.grid(row=4, column=1, columnspan=2, pady=10)

root.mainloop()
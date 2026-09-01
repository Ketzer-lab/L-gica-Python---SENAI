import tkinter as tk
from tkinter import ttk

# JANELA PRINCIPAL

root = tk.Tk()

root.title("SAPZ - Calculadora de Resistor")
root.geometry("650x450")
root.config(bg="#D9EAF7")
root.resizable(False, False)

# TÍTULO

titulo = tk.Label(
    root,
    text="Calculadora de Resistor",
    font=("Helvetica", 22, "bold"),
    bg="#D9EAF7",
    fg="#1F3B5B"
)

titulo.pack(pady=20)

# FRAME PRINCIPAL

frame = tk.Frame(
    root,
    bg="white",
    padx=25,
    pady=20,
    relief="solid",
    bd=1
)

frame.pack(padx=30, pady=10, fill="both", expand=True)


# PERGUNTA

label_in = tk.Label(
    frame,
    text="Como deseja informar o resistor?",
    font=("Helvetica", 14, "bold"),
    bg="white"
)

label_in.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=(0, 15)
)

# RADIOBUTTONS

opcao = tk.IntVar()

rbutton_v = tk.Radiobutton(
    frame,
    text="Valor da resistência",
    variable=opcao,
    value=1,
    bg="white",
    font=("Helvetica", 11)
)

rbutton_v.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)

rbutton_c = tk.Radiobutton(
    frame,
    text="Cores do resistor",
    variable=opcao,
    value=2,
    bg="white",
    font=("Helvetica", 11)
)

rbutton_c.grid(
    row=1,
    column=2,
    columnspan=2,
    pady=10
)

# LINHA SEPARADORA

separador = ttk.Separator(
    frame,
    orient="horizontal"
)

separador.grid(
    row=2,
    column=0,
    columnspan=4,
    sticky="ew",
    pady=15
)

# CONFIGURAÇÃO DAS COLUNAS

for coluna in range(4):
    frame.columnconfigure(coluna, weight=1)

# LABELS DAS BANDAS

banda1 = tk.Label(
    frame,
    text="Banda 1",
    font=("Helvetica", 11, "bold"),
    bg="white"
)

banda1.grid(row=3, column=0, pady=(0, 5))

banda2 = tk.Label(
    frame,
    text="Banda 2",
    font=("Helvetica", 11, "bold"),
    bg="white"
)

banda2.grid(row=3, column=1, pady=(0, 5))

multiplicador = tk.Label(
    frame,
    text="Multiplicador",
    font=("Helvetica", 11, "bold"),
    bg="white"
)

multiplicador.grid(row=3, column=2, pady=(0, 5))

tolerancia = tk.Label(
    frame,
    text="Tolerância",
    font=("Helvetica", 11, "bold"),
    bg="white"
)

tolerancia.grid(row=3, column=3, pady=(0, 5))

# CORES

cores = [
    "Preto",
    "Marrom",
    "Vermelho",
    "Laranja",
    "Amarelo",
    "Verde",
    "Azul",
    "Violeta",
    "Cinza",
    "Branco"
]

cores2 = [
    "marrom",
    "vermelho",
    "verde",
    "azul",
    "violeta",
    "cinza",
    "ouro",
    "prata"
]

# COMBOBOXES

combo1 = ttk.Combobox(
    frame,
    values=cores,
    state="readonly",
    width=12
)

combo1.grid(
    row=4,
    column=0,
    padx=5
)

combo2 = ttk.Combobox(
    frame,
    values=cores,
    state="readonly",
    width=12
)

combo2.grid(
    row=4,
    column=1,
    padx=5
)

combo3 = ttk.Combobox(
    frame,
    values=cores,
    state="readonly",
    width=12
)

combo3.grid(
    row=4,
    column=2,
    padx=5
)

combo4 = ttk.Combobox(
    frame,
    values=cores2,
    state="readonly",
    width=12
)

combo4.grid(
    row=4,
    column=3,
    padx=5
)

# BOTÃO

button = tk.Button(
    frame,
    text="Calcular Resistência",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=8,
    cursor="hand2"
)

button.grid(
    row=5,
    column=0,
    columnspan=4,
    pady=30
)

# Label 2

label_in = tk.Label(
    frame,
    text="Digite o valor da resistência ou selecione as cores",
    font=("Helvetica", 10, "bold"),
    bg="white"
)

label_in.grid(
    row=6,
    column=0,
    columnspan=4,
    sticky="w",
    pady=(0, 10)
)

root.mainloop()
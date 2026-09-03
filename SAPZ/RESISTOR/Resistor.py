import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas

# Funções

def calculo():

    try:
        cores_c1 = {
        "black": 0, 
        "brown": 1, 
        "red": 2, 
        "orange": 3, 
        "yellow": 4, 
        "green": 5, 
        "blue": 6, 
        "violet": 7, 
        "gray": 8, 
        "white": 9
        }

        cores_c2 = {    
        "brown": 1,
        "red": 2,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "gray": 0.05,
        "gold": 5,
        "silver": 10
        }

        banda1 = combo1.get()
        banda2 = combo2.get()
        multiplicador = combo3.get()
        tolerancia = combo4.get()

        if banda1:
            canvas.itemconfig(Banda1, fill=cores[banda1])
        if banda2:
            canvas.itemconfig(Banda2, fill=cores[banda2])
        if multiplicador:
            canvas.itemconfig(Multiplicador, fill=cores[multiplicador])
        if tolerancia:
            canvas.itemconfig(Tolerancia, fill=cores2[tolerancia])
    
        cor_1 = cores[banda1]
        cor_2 = cores[banda2]
        cor_3 = cores[multiplicador]
        cor_4 = cores2[tolerancia]

        resistencia_C = ((cores_c1[cor_1]*10)+cores_c1[cor_2])*(10**cores_c1[cor_3])
        tolerancia_C = cores_c2[cor_4]

        if resistencia_C < 1000:
            resultado = f"{resistencia_C} Ω"
        elif 1000 <= resistencia_C < 1000000:
            resultado = f"{resistencia_C / 1000} KΩ"
        elif resistencia_C >= 1000000:
            resultado = f"{resistencia_C / 1000000} MΩ"

        label_in.config(text=f"Resistência: {resultado}   Tolerância: ±{tolerancia_C}%")

    except KeyError:
        label_in.config(text=f"Por favor preencha todas as caixas!")


# Janela Principal

root = tk.Tk()

root.title("SAPZ - Calculadora de Resistor")
root.geometry("650x650")
root.config(bg="#D9EAF7")
root.resizable(False, False)

# Título

titulo = tk.Label(
    root,
    text="Calculadora de Resistor",
    font=("Helvetica", 22, "bold"),
    bg="#D9EAF7",
    fg="#1F3B5B"
)

titulo.pack(pady=20)

# Frame Principal

frame = tk.Frame(root, bg="white", padx=25, pady=20, relief="solid", bd=1)

frame.pack(padx=30, pady=10, fill="both", expand=True)

# CORES

cores = {
    "Preto": "black",
    "Marrom": "brown",
    "Vermelho": "red",
    "Laranja": "orange",
    "Amarelo": "yellow",
    "Verde": "green",
    "Azul": "blue",
    "Violeta": "violet",
    "Cinza": "gray",
    "Branco": "white"
}

cores2 = {
    "Marrom": "brown",
    "Vermelho": "red",
    "Verde": "green",
    "Azul": "blue",
    "Violeta": "violet",
    "Cinza": "gray",
    "Ouro": "gold",
    "Prata": "silver"
}

# Pergunta

label_in = tk.Label(frame, text="Como deseja informar o resistor?", font=("Helvetica", 14, "bold"), bg="white")

label_in.grid(row=0, column=0, columnspan=4, pady=(0, 15))

# RADIOBUTTONS

opcao = tk.IntVar()

rbutton_v = tk.Radiobutton(frame, text="Valor da resistência", variable=opcao, value=1, bg="white", font=("Helvetica", 11))

rbutton_v.grid(row=1, column=0, columnspan=2, pady=10)

rbutton_c = tk.Radiobutton(frame, text="Cores do resistor", variable=opcao, value=2, bg="white", font=("Helvetica", 11))

rbutton_c.grid(row=1, column=2, columnspan=2, pady=10)

# Linha Separadora

separador = ttk.Separator(frame, orient="horizontal")

separador.grid(row=2, column=0, columnspan=4, sticky="ew", pady=15)

# Configuração das Colunas

for coluna in range(4):
    frame.columnconfigure(coluna, weight=1)

# Labels das Bandas

banda1 = tk.Label(frame, text="Banda 1", font=("Helvetica", 11, "bold"), bg="white")

banda1.grid(row=3, column=0, pady=(0, 5))

banda2 = tk.Label(frame, text="Banda 2", font=("Helvetica", 11, "bold"), bg="white"
)

banda2.grid(row=3, column=1, pady=(0, 5))

multiplicador = tk.Label(frame, text="Multiplicador", font=("Helvetica", 11, "bold"), bg="white")

multiplicador.grid(row=3, column=2, pady=(0, 5))

tolerancia = tk.Label(frame, text="Tolerância", font=("Helvetica", 11, "bold"), bg="white")

tolerancia.grid(row=3, column=3, pady=(0, 5))

# COMBOBOXES

combo1 = ttk.Combobox(frame, values=list(cores.keys()), state="readonly", width=12)

combo1.grid(row=4, column=0, padx=5)

combo2 = ttk.Combobox(frame, values=list(cores.keys()), state="readonly", width=12)

combo2.grid(row=4, column=1, padx=5)

combo3 = ttk.Combobox(frame, values=list(cores.keys()), state="readonly", width=12)

combo3.grid(row=4, column=2, padx=5)

combo4 = ttk.Combobox(frame, values=list(cores2.keys()), state="readonly", width=12)

combo4.grid(row=4, column=3, padx=5)

# Botão

button = tk.Button(frame, text="Calcular Resistência", command=calculo, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=15, pady=8,)

button.grid(row=5, column=0, columnspan=4, pady=30)

# Label 2

label_in = tk.Label(frame, text="Digite o valor da resistência ou selecione as cores", font=("Helvetica", 10, "bold"), bg="white")

label_in.grid(row=6, column=0, columnspan=4, sticky="w", pady=(0, 10))

# Canvas
canvas = Canvas(frame, width=500, height=160, bg="white", highlightthickness=0, bd=0)
canvas.grid(row=7, column=0, columnspan=4, pady=(0, 10))

# Corpo do resistor
base = canvas.create_rectangle(
    60, 50, 420, 110,
    fill='light yellow',
    outline='black'
)

# Banda 1
Banda1 = canvas.create_rectangle(
    130, 50, 160, 110,
    fill='light yellow'
)

# Banda 2
Banda2 = canvas.create_rectangle(
    190, 50, 220, 110,
    fill='light yellow'
)

# Multiplicador
Multiplicador = canvas.create_rectangle(
    250, 50, 280, 110,
    fill='light yellow'
)

# Tolerância
Tolerancia = canvas.create_rectangle(
    330, 50, 360, 110,
    fill='light yellow'
)

root.mainloop()
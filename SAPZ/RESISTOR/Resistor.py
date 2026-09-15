import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas

combo1 = combo2 = combo3 = combo4 = None
entry_res = combo_tol = None
widgets_modo = []

def limpar():

    global widgets_modo

    for widget in widgets_modo:
        widget.destroy()

    widgets_modo.clear()

    label_resultado.config(text="")

def calculo():

    if opcao.get() == 2:

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

            # Comboboxes
            banda1 = combo1.get()
            banda2 = combo2.get()
            multiplicador = combo3.get()
            tolerancia = combo4.get()

            if not banda1 or not banda2 or not multiplicador or not tolerancia:
                label_resultado.config(text="Por favor preencha todas as caixas!")
                return

            # Adiciona cor ao resistor
            canvas.itemconfig(Banda1, fill=cores[banda1], outline=cores[banda1])
            canvas.itemconfig(Banda2, fill=cores[banda2], outline=cores[banda2])
            canvas.itemconfig(Multiplicador, fill=cores[multiplicador], outline=cores[multiplicador])
            canvas.itemconfig(Tolerancia, fill=cores2[tolerancia], outline=cores2[tolerancia])

            cor_1 = cores[banda1]
            cor_2 = cores[banda2]
            cor_3 = cores[multiplicador]
            cor_4 = cores2[tolerancia]

            resistencia_C = ((cores_c1[cor_1] * 10) + cores_c1[cor_2]) * (10 ** cores_c1[cor_3])
            tolerancia_C = cores_c2[cor_4]

            if resistencia_C < 1000:
                resultado = f"{resistencia_C} Ω"
            elif resistencia_C < 1000000:
                resultado = f"{resistencia_C / 1000} KΩ"
            else:
                resultado = f"{resistencia_C / 1000000} MΩ"

            label_resultado.config(text=f"Resistência: {resultado}   Tolerância: ±{tolerancia_C}%")

        except (ValueError, KeyError):
            label_resultado.config(text="Valor inválido!")

    elif opcao.get() == 1:

        try:

            cores_inverso = {
                0: "black",
                1: "brown",
                2: "red",
                3: "orange",
                4: "yellow",
                5: "green",
                6: "blue",
                7: "violet",
                8: "gray",
                9: "white"
            }

            valor = int(entry_res.get())

            if valor <= 0:
                label_resultado.config(text="Digite um valor maior que zero!")
                return

            potencia = 0

            while valor >= 100:
                valor = valor / 10
                potencia += 1

            primeiro = int(valor) // 10
            segundo = int(valor) % 10

            cor_1 = cores_inverso[primeiro]
            cor_2 = cores_inverso[segundo]
            cor_3 = cores_inverso[potencia]

            canvas.itemconfig(Banda1, fill=cor_1, outline=cor_1)
            canvas.itemconfig(Banda2, fill=cor_2, outline=cor_2)
            canvas.itemconfig(Multiplicador, fill=cor_3, outline=cor_3)

            tolerancia_cor = combo_tol.get()

            if not tolerancia_cor:
                label_resultado.config(text="Selecione uma tolerância!")
                return

            cor_4 = cores2[tolerancia_cor]

            canvas.itemconfig(Tolerancia, fill=cor_4, outline=cor_4)

        except (ValueError, KeyError):
            label_resultado.config(text="Digite um valor válido!")

def radio_ident():

    global combo1, combo2, combo3, combo4
    global entry_res, combo_tol

    limpar()

    if opcao.get() == 2:

        banda1_label = tk.Label(frame, text="Banda 1", font=("Helvetica", 11, "bold"), bg="white")
        banda1_label.grid(row=3, column=0, pady=(0, 5))
        widgets_modo.append(banda1_label)

        banda2_label = tk.Label(frame, text="Banda 2", font=("Helvetica", 11, "bold"), bg="white")
        banda2_label.grid(row=3, column=1, pady=(0, 5))
        widgets_modo.append(banda2_label)

        multiplicador_label = tk.Label(frame, text="Multiplicador", font=("Helvetica", 11, "bold"), bg="white")
        multiplicador_label.grid(row=3, column=2, pady=(0, 5))
        widgets_modo.append(multiplicador_label)

        tolerancia_label = tk.Label(frame, text="Tolerância", font=("Helvetica", 11, "bold"), bg="white")
        tolerancia_label.grid(row=3, column=3, pady=(0, 5))
        widgets_modo.append(tolerancia_label)

        combo1 = ttk.Combobox(frame, values=list(cores.keys()), state="readonly", width=12)
        combo1.grid(row=4, column=0, padx=5)
        widgets_modo.append(combo1)

        combo2 = ttk.Combobox(frame, values=list(cores.keys()), state="readonly", width=12)
        combo2.grid(row=4, column=1, padx=5)
        widgets_modo.append(combo2)

        combo3 = ttk.Combobox(frame, values=list(cores.keys()), state="readonly", width=12)
        combo3.grid(row=4, column=2, padx=5)
        widgets_modo.append(combo3)

        combo4 = ttk.Combobox(frame, values=list(cores2.keys()), state="readonly", width=12)
        combo4.grid(row=4, column=3, padx=5)
        widgets_modo.append(combo4)

        button = tk.Button(frame, text="Calcular Resistência", command=calculo, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=15, pady=8)
        button.grid(row=5, column=0, columnspan=4, pady=30)
        widgets_modo.append(button)

    elif opcao.get() == 1:

        valor_res = tk.Label(frame, text="Valor da resistência:", font=("Helvetica", 11, "bold"), bg="white")
        valor_res.grid(row=3, column=0, columnspan=2, sticky="ew")
        widgets_modo.append(valor_res)

        tolerancia_label = tk.Label(frame, text="Tolerância:", font=("Helvetica", 11, "bold"), bg="white")
        tolerancia_label.grid(row=3, column=2, columnspan=2, sticky="ew")
        widgets_modo.append(tolerancia_label)

        entry_res = tk.Entry(frame)
        entry_res.grid(row=4, column=0, columnspan=2, sticky="ew")
        widgets_modo.append(entry_res)

        combo_tol = ttk.Combobox(frame, values=list(cores2.keys()), state="readonly")
        combo_tol.grid(row=4, column=2, columnspan=2, sticky="ew")
        widgets_modo.append(combo_tol)

        button = tk.Button(frame, text="Calcular Resistência", command=calculo, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=15, pady=8)
        button.grid(row=5, column=0, columnspan=4, pady=30)
        widgets_modo.append(button)

root = tk.Tk()

root.title("SAPZ - Calculadora de Resistor")
root.geometry("650x650")
root.config(bg="#D9EAF7")
root.resizable(False, False)

titulo = tk.Label(root, text="Calculadora de Resistor", font=("Helvetica", 22, "bold"), bg="#D9EAF7", fg="#1F3B5B")
titulo.pack(pady=20)

frame = tk.Frame(root, bg="white", padx=25, pady=20, relief="solid", bd=1)
frame.pack(padx=30, pady=10, fill="both", expand=True)

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

# Labels
label_pergunta = tk.Label(frame, text="Como deseja informar o resistor?", font=("Helvetica", 14, "bold"), bg="white")
label_pergunta.grid(row=0, column=0, columnspan=4, pady=(0, 15))

label_resultado = tk.Label(frame, text="", font=("Helvetica", 10, "bold"), bg="white")
label_resultado.grid(row=6, column=0, columnspan=4, pady=(0, 10))

# Radio buttons
opcao = tk.IntVar()

rbutton_v = tk.Radiobutton(frame, text="Valor da resistência", variable=opcao, command=radio_ident, value=1, bg="white", font=("Helvetica", 11))
rbutton_v.grid(row=1, column=0, columnspan=2, pady=10)

rbutton_c = tk.Radiobutton(frame, text="Cores do resistor", variable=opcao, command=radio_ident, value=2, bg="white", font=("Helvetica", 11))
rbutton_c.grid(row=1, column=2, columnspan=2, pady=10)

separador = ttk.Separator(frame, orient="horizontal")
separador.grid(row=2, column=0, columnspan=4, sticky="ew", pady=15)

# Grid
for coluna in range(4):
    frame.columnconfigure(coluna, weight=1)

# Canvas
canvas = Canvas(frame, width=500, height=160, bg="white", highlightthickness=0, bd=0)
canvas.grid(row=7, column=0, columnspan=4, pady=(0, 10))

base = canvas.create_rectangle(
    60, 50, 420, 110,
    fill="light yellow",
    outline="black"
)

Banda1 = canvas.create_rectangle(
    130, 51, 160, 109,
    fill="light yellow",
    outline="light yellow"
)

Banda2 = canvas.create_rectangle(
    190, 51, 220, 109,
    fill="light yellow",
    outline="light yellow"
)

Multiplicador = canvas.create_rectangle(
    250, 51, 280, 109,
    fill="light yellow",
    outline="light yellow"
)

Tolerancia = canvas.create_rectangle(
    330, 51, 360, 109,
    fill="light yellow",
    outline="light yellow"
)

root.mainloop()
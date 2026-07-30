import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

def calculo():
    try:
        peso = float(entrypeso.get())
        altura = float(entryaltura.get())

        imc = peso / (altura*altura)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        resultado.config(
            text=f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}"
        )

    except ValueError:
        resultado.config(text="Digite valores válidos!")


labelpeso = tk.Label(root, text="Peso(Kg)")
labelpeso.pack()
entrypeso = tk.Entry(root)
entrypeso.pack()

labelaltura = tk.Label(root, text="Altura(m)")
labelaltura.pack()
entryaltura = tk.Entry(root)
entryaltura.pack()

button = tk.Button(            
    root,
    text="Calcular",
    command=calculo
    )
button.pack()

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()
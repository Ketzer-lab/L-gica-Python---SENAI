import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Calculadora de IMC")
root.geometry("800x600")


def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura * altura)

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


# Título
titulo = tk.Label(root, text="Calculadora de IMC", font=("Arial", 20))
titulo.pack(pady=20)


# Peso
label_peso = tk.Label(root, text="Peso (Kg)")
label_peso.pack()

entry_peso = tk.Entry(root)
entry_peso.pack()


# Altura
label_altura = tk.Label(root, text="Altura (m)")
label_altura.pack()

entry_altura = tk.Entry(root)
entry_altura.pack()


# Botão
button = tk.Button(
    root,
    text="Calcular",
    command=calcular_imc
)
button.pack(pady=20)


# Resultado
resultado = tk.Label(root, text="", font=("Arial", 14))
resultado.pack()


root.mainloop()

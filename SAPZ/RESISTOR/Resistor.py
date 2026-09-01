import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Radiobutton, IntVar
from tkinter import messagebox

root = tk.Tk(); root.title("SAPZ - Resistor")
root.geometry("550x450")
root.config(bg="light blue")

opcao = IntVar()

label = tk.Label(root, text="Calculadora de resistor:", font=("Heçvetica", 20))
label.config(bg="light blue")
label.place(x =40, y=45)

frame = tk.Frame(root, width=500, height=320, bg="white")
frame.place(x=25, y=100)

label_in = tk.Label(frame, text="Como deseja informar o resistor?", font=("Heçvetica", 15))
label_in.grid(rowspan=1, column=0)

rbutton_v = Radiobutton(frame, text="Valor da resistência", variable=opcao, value=1)
rbutton_v.grid(row=1, column=0)

rbutton_c = Radiobutton(frame, text="Cores do resistor", variable=opcao, value=1)
rbutton_c.grid(row=1, column=1)

banda1 = tk.Label(frame, text="Banda 1")
banda1.grid(row=3, column=0)
combo1 = ttk.Combobox(frame, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combo1.grid(row=4, column=0)

banda2 = tk.Label(frame, text="Banda 2")
banda2.grid(row=3, column=1)
combo2 = ttk.Combobox(frame, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combo2.grid(row=4, column=1)

multiplicador = tk.Label(frame, text="Multiplicador")
multiplicador.grid(row=3, column=2)
combo3 = ttk.Combobox(frame, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combo3.grid(row=4, column=2)

tolerancia = tk.Label(frame, text="tolerância")
tolerancia.grid(row=3, column=3)
combo4 = ttk.Combobox(frame, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combo4.grid(row=4, column=3)

button = tk.Button(frame, text="Calcular Resistência", command=quit)
button.grid(row=5, column=0)

root.mainloop()
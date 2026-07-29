import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

minha_imagem = tk.PhotoImage(file="exemplo.png")

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)

root.mainloop()

#A imagem precisa ser um PNG e precisa estar na mesma pasta do código
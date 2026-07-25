import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

minha_imagem = tk.PhotoImage(file="ouroboros.png")

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)

root.mainloop()
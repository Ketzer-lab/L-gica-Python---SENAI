import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("SENAI - Cadastro")
root.config(bg="white")

foto = tk.PhotoImage(file="profile.png").subsample(3, 3)
label_foto = tk.Label(root, image=foto, bg="white")
label_foto.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

label_nome = tk.Label(root, text="Nome:", bg="white").grid(row=0, column=1, sticky="e", padx=5)
entry_nome = tk.Entry(root, width=25); entry_nome.grid(row=0, column=2, padx=5, pady=5)

label_gen = tk.Label(root, text="Gênero:", bg="white").grid(row=1, column=1, sticky="e", padx=5)
combo_gen = ttk.Combobox(root, values=["Masculino", "Feminino"], width=22); combo_gen.grid(row=1, column=2, padx=5, pady=5)

label_eye = tk.Label(root, text="Cor dos olhos:", bg="white").grid(row=2, column=1, sticky="e", padx=5)
combo_eye = ttk.Combobox(root, values=["Castanho", "Azul", "Verde", "Preto"], width=22); combo_eye.grid(row=2, column=2, padx=5, pady=5)

label_altura = tk.Label(root, text="Altura(m):", bg="white").grid(row=3, column=1, sticky="e", padx=5)
entry_altura = tk.Entry(root, width=25); entry_altura.grid(row=3, column=2, padx=5, pady=5)

label_peso = tk.Label(root, text="Peso(Kg):", bg="white").grid(row=4, column=1, sticky="e", padx=5)
entry_peso = tk.Entry(root, width=25); entry_peso.grid(row=4, column=2, padx=5, pady=5)

botao = tk.Button(
    root,
    text="Enviar", 
    bg="white"
).grid(row=5, column=2, pady=15)

root.mainloop()
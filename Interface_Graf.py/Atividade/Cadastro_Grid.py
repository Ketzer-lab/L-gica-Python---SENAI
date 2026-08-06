import tkinter as tk

root = tk.Tk(); root.title("SENAI - Cadastro")
root.config(bg="white")

# Foto de perfil (placeholder)
foto = tk.PhotoImage(file="profile.png").subsample(3, 3)
label_foto = tk.Label(root, image=foto, bg="white")
label_foto.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

label_nome = tk.Label(root, text="Nome: ", bg="white").grid(row=0, column=1, sticky="w", padx=5)
entry_nome = tk.Entry(root, width=25); entry_nome.grid(row=0, column=2, padx=5, pady=5)

label_gen = tk.Label(root, text="Gênero: ", bg="white").grid(row=1, column=1, sticky="w", padx=5)
entry_gen = tk.Entry(root, width=25); entry_gen.grid(row=1, column=2, padx=5, pady=5)

label_eye = tk.Label(root, text="Cor dos olhos: ", bg="white").grid(row=2, column=1, sticky="w", padx=5)
entry_eye = tk.Entry(root, width=25); entry_eye.grid(row=2, column=2, padx=5, pady=5)

label_altura = tk.Label(root, text="Altura(m): ", bg="white").grid(row=3, column=1, sticky="w", padx=5)
entry_altura = tk.Entry(root, width=25); entry_altura.grid(row=3, column=2, padx=5, pady=5)

label_peso = tk.Label(root, text="Peso(Kg): ", bg="white").grid(row=4, column=1, sticky="w", padx=5)
entry_peso = tk.Entry(root, width=25); entry_peso.grid(row=4, column=2, padx=5, pady=5)

botao = tk.Button(
    root,
    text="Enviar", 
    bg="white"
).grid(row=5, column=2, pady=15)

root.mainloop()
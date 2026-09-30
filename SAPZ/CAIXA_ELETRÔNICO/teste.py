import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas

#=======================#
#   JANELA PRINCIPAL    #
#=======================#

root = tk.Tk()
root.title("SAPZ - Caixa Eletronico")
root.config(bg="#04233A")
root.geometry("400x500")
root.resizable(False, False)

#===========#
#   LABELS  #
#===========#

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, minsize=50)

bem_vindo = tk.Label(root, text="BEM VINDO AO \nCAIXA ELETRÔNICO", font=("Helvetica", 20, "bold"), bg="#04233A", fg="#FFFFFF")
bem_vindo.grid(row=0, column=0, columnspan=1, sticky="ew")

usuario_label = tk.Label(root, text="Usuário:", font=("Helvetica", 15, "bold"), bg="#04233A", fg="#FFFFFF")
usuario_label.grid(row=2, column=0, columnspan=1, sticky="ew")

senha_label = tk.Label(root, text="Senha:", font=("Helvetica", 15, "bold"), bg="#04233A", fg="#FFFFFF")
senha_label.grid(row=3, column=0, columnspan=1, sticky="ew")


root.mainloop()
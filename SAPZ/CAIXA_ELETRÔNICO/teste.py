import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas

#===============#
#    FUNÇÕES    #
#===============#

def caixa():
    root.geometry("1000x600")
    root.resizable(False, False)

    root.grid_columnconfigure(350)
    root.grid_rowconfigure(1, minsize=50)
    root.grid_rowconfigure(3, minsize=40)

    caixa_label = tk.Label(root, text="CAIXA ELETRÔNICO", font=("Helvetica", 25, "bold"), bg="#04233A", fg="#FFFFFF")
    caixa_label.grid(row=0, column=0, rowspan=1, sticky="ew")

    saldo_label = tk.Label(root, text="teste", font=("Helvetica", 25, "bold"), bg="#04233A", fg="#FFFFFF")
    saldo_label.grid(row=2, column=2, rowspan=1, columnspan=1)

    button_cashout = tk.Button(root, text="SACAR DINHEIRO", command=sacar, width=35, height=3, bg="#0CA120", fg="#FFFFFF")
    button_cashout.grid(row=2, column=0, columnspan=1, sticky="w")

    button_cashin = tk.Button(root, text="DEPOSITAR DINHEIRO", command=depositar, width=35, height=3, bg="#0CA120", fg="#FFFFFF")
    button_cashin.grid(row=4, column=0, rowspan=1, sticky="w")

    button_quit = tk.Button(root, text="SAIR", command=root.destroy, width=35, height=3, bg="#0CA120", fg="#FFFFFF")
    button_quit.grid(row=10, column=0, columnspan=1, sticky="w")

def sacar():
    print()

def depositar():
    print()

def limpar_root():
    for widget in root.winfo_children():
        widget.destroy()
    

def login():
    login_user = entry_user.get()
    login_senha = entry_senha.get()

    if login_user == user and login_senha == senha:
        limpar_root()
        caixa()

#===============#
#   Variaveis   #
#===============#

user = "user"
senha = "senha"

#=======================#
#   JANELA PRINCIPAL    #
#=======================#

root = tk.Tk()
root.title("SAPZ - Caixa Eletronico")
root.config(bg="#04233A")
root.geometry("350x450")
root.resizable(False, False)

#===========#
#   LABELS  #
#===========#

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(4, minsize=20)
root.grid_rowconfigure(7, minsize=40)
root.grid_rowconfigure(9, minsize=20)


bem_vindo = tk.Label(root, text="BEM VINDO AO \nCAIXA ELETRÔNICO", font=("Helvetica", 20, "bold"), bg="#04233A", fg="#FFFFFF")
bem_vindo.grid(row=0, column=0, columnspan=1, sticky="ew")

user_label = tk.Label(root, text="Usuário:", font=("Helvetica", 17, "bold"), bg="#04233A", fg="#FFFFFF")
user_label.grid(row=2, column=0, columnspan=1, sticky="ew")

senha_label = tk.Label(root, text="Senha:", font=("Helvetica", 17, "bold"), bg="#04233A", fg="#FFFFFF")
senha_label.grid(row=5, column=0, columnspan=1, sticky="ew")

#=======================#
#   CAIXAS DE TEXTO     #
#=======================#

entry_user = tk.Entry(root, width=25)
entry_user.grid(row=3, column=0, columnspan=1, ipady=10)

entry_senha = tk.Entry(root, width=25)
entry_senha.grid(row=6, column=0, columnspan=1, ipady=10)

#===========#
#   BOTÕES  #
#===========#

button_login = tk.Button(root, text="ENTRAR", command=login, width=25, height=2, bg="#0CA120", fg="#FFFFFF")
button_login.grid(row=8, column=0, columnspan=1)

button_quit = tk.Button(root, text="SAIR", command=root.destroy, width=25, height=2, bg="#0CA120", fg="#FFFFFF")
button_quit.grid(row=10, column=0, columnspan=1)

root.mainloop()
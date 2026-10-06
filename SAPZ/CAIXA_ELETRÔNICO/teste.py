import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas
import os

#===============#
#    FUNÇÕES    #
#===============#

def limpar_root():
    for widget in root.winfo_children():
        widget.destroy()
    
def login():
    login_user = entry_user.get()
    login_senha = entry_senha.get()

    if login_user == user and login_senha == senha:
        caixa()

def caixa():

    limpar_root

    root.geometry("1000x600")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    caixa_label = tk.Label(frame, text="CAIXA ELETRÔNICO", font=("Helvetica", 25, "bold"), bg="light yellow", fg="#04233A")
    caixa_label.pack(pady=20)

    caminho_saldo = os.path.join(os.path.dirname(__file__), "SALDO.txt")

    with open(caminho_saldo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    numero = conteudo.strip()

    saldo_label = tk.Label(frame, text=f"SALDO\n\nR$ {numero}", font=("Helvetica", 25, "bold"), bg="light yellow")
    saldo_label.pack(pady=20)

    button_cashout = tk.Button(frame, text="SACAR DINHEIRO", command=sacar, width=35, height=3, bg="#0CA120", fg="white")
    button_cashout.pack(pady=10)

    button_cashin = tk.Button(frame, text="DEPOSITAR DINHEIRO", command=depositar, width=35, height=3, bg="#0CA120", fg="white")
    button_cashin.pack(pady=10)

    button_quit = tk.Button(frame, text="SAIR", command=root.destroy, width=35, height=3, bg="#0CA120", fg="white")
    button_quit.pack(pady=10)


def sacar():
    limpar_root()
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame1 = tk.Frame(root, bg="light yellow")
    frame1.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    frame2 = tk.Frame(frame1, bg="light yellow")
    frame2.place(relx=0.5, rely=0.5, relwidth=0.9, anchor="center")

    sacar_entry = tk.Entry(frame2, font=("Arial", 20))
    sacar_entry.pack(fill="x", pady=10)

    sacar_button = tk.Button(frame2, text="SACAR", font=("Arial", 20), command=caixa)
    sacar_button.pack(fill="x", pady=10)



def depositar():
    limpar_root()
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame1 = tk.Frame(root, bg="light yellow")
    frame1.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    frame2 = tk.Frame(frame1, bg="light yellow")
    frame2.place(relx=0.5, rely=0.5, relwidth=0.9, anchor="center")

    depositar_entry = tk.Entry(frame2, font=("Arial", 20))
    depositar_entry.pack(fill="x", pady=10)
    
    depositar_button = tk.Button(frame2, text="DEPOSITAR", font=("Arial", 20), command=caixa)
    depositar_button.pack(fill="x", pady=10)

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
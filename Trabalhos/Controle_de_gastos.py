import tkinter as tk
from tkinter import messagebox
import os
import json

#===================#
#     Variaveis     #
#===================#

caminho_json = os.path.join(os.path.dirname(__file__), "data.json")
SALDO_INICIAL = 0
usuario_logado = None

#=================#
#     Funções     #
#=================#

def limpar_root():
    for widget in root.winfo_children():
        widget.destroy()


def login():
    global usuario_logado

    nome = entry_user.get().strip()
    senha = entry_senha.get()
    contas = carregar_contas()

    if nome in contas and contas[nome]["senha"] == senha:
        usuario_logado = nome
        controle()
    else:
        messagebox.showerror("Login inválido", "Usuário ou senha incorretos.")


def carregar_contas():
    if os.path.exists(caminho_json):
        try:
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            contas = dados.get("contas", {})

        except (json.JSONDecodeError, OSError):
            contas = {}
    else:
        contas = {}

    if "user" not in contas:
        contas["user"] = {"senha": "1", "saldo": SALDO_INICIAL}

    salvar_contas(contas)
    return contas


def salvar_contas(contas):
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump({"contas": contas}, arquivo, ensure_ascii=False, indent=4)


def criar_conta():
    nome = entry_novo_usuario.get().strip()
    senha = entry_nova_senha.get()

    if not nome or not senha:
        messagebox.showerror("Erro", "Preencha o usuário e a senha.")
        return

    if "," in nome or "," in senha or "\n" in nome or "\n" in senha:
        messagebox.showerror("Erro", "Não use vírgulas ou quebras de linha no usuário ou na senha.")
        return

    contas = carregar_contas()

    if nome in contas:
        messagebox.showerror("Erro", "Esse usuário já existe. Escolha outro nome.")
        return

    contas[nome] = {"senha": senha, "saldo": SALDO_INICIAL}
    salvar_contas(contas)

    messagebox.showinfo("Conta criada", f"Conta de {nome} criada com sucesso!\nSaldo inicial: R$ {SALDO_INICIAL:.2f}")
    tela_login()

def b_depositar():
    messagebox.showinfo("Depósito", "Função de depósito ainda não implementada.")

def b_sacar():
    messagebox.showinfo("Saque", "Função de saque ainda não implementada.")

#=======================#
#   TELAS DE ACESSO     #
#=======================#

def tela_login():
    global entry_user, entry_senha

    limpar_root()
    root.geometry("350x450")
    root.resizable(False, False)
    root.configure(bg="#EFF0B8")
    root.grid_columnconfigure(0, weight=1)

    tk.Label(root, text="BEM VINDO AO\nCONTROLE DE GASTOS", font=("Helvetica", 20, "bold"), bg="#EFF0B8", fg="black").grid(row=0, column=0, pady=15)
    tk.Label(root, text="Usuário:", font=("Helvetica", 17, "bold"), bg="#EFF0B8", fg="black").grid(row=1, column=0, pady=5)

    entry_user = tk.Entry(root, width=25)
    entry_user.grid(row=2, column=0, ipady=8)

    tk.Label(root, text="Senha:", font=("Helvetica", 17, "bold"), bg="#EFF0B8", fg="black").grid(row=3, column=0, pady=5)

    entry_senha = tk.Entry(root, width=25, show="*")
    entry_senha.grid(row=4, column=0, ipady=8)

    tk.Button(root, text="ENTRAR", command=login, width=25, height=2, bg="#0CA120", fg="white").grid(row=5, column=0, pady=12)
    tk.Button(root, text="CRIAR CONTA", command=tela_criar_conta, width=25, height=2, bg="#2471A3", fg="white").grid(row=6, column=0, pady=5)
    tk.Button(root, text="SAIR", command=root.destroy, width=25, height=2, bg="#F31313", fg="white").grid(row=7, column=0, pady=5)


def tela_criar_conta():
    global entry_novo_usuario, entry_nova_senha

    limpar_root()
    root.geometry("400x400")
    root.configure(bg="#EFF0B8")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="center")

    tk.Label(frame, text="CRIAR CONTA", font=("Helvetica", 22, "bold"), bg="light yellow", fg="black").pack(pady=20)
    tk.Label(frame, text="Novo usuário:", font=("Arial", 14), bg="light yellow").pack(pady=5)

    entry_novo_usuario = tk.Entry(frame, font=("Arial", 16))
    entry_novo_usuario.pack(padx=20, fill="x")

    tk.Label(frame, text="Nova senha:", font=("Arial", 14), bg="light yellow").pack(pady=5)

    entry_nova_senha = tk.Entry(frame, font=("Arial", 16), show="*")
    entry_nova_senha.pack(padx=20, fill="x")

    tk.Button(frame, text="CRIAR CONTA", command=criar_conta, width=25, height=2, bg="#0CA120", fg="white").pack(pady=15)
    tk.Button(frame, text="VOLTAR", command=tela_login, width=25).pack()

def controle():
    limpar_root()
    root.geometry("1000x600")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    # Label principal
    tk.Label(
        frame,
        text=f"CAIXA ELETRÔNICO\nUsuário: {usuario_logado}",
        font=("Helvetica", 25, "bold"),
        bg="light yellow",
        fg="#04233A"
    ).pack(pady=20)

    # Área para organizar os controles
    conteudo = tk.Frame(frame, bg="light yellow")
    conteudo.pack(fill="both", expand=True, padx=20, pady=10)

    conteudo.grid_columnconfigure(0, weight=1)
    conteudo.grid_columnconfigure(1, weight=1)
    conteudo.grid_rowconfigure(0, weight=1)

    # Lado esquerdo: botões
    frame_botoes = tk.Frame(conteudo, bg="light yellow")
    frame_botoes.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)

    tk.Button(
        frame_botoes,
        text="DEPOSITAR DINHEIRO",
        command=b_depositar,
        width=30,
        height=3,
        bg="#0CA120",
        fg="white"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="SACAR DINHEIRO",
        command=b_sacar,
        width=30,
        height=3,
        bg="#E09625",
        fg="white"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="SAIR",
        command=tela_login,
        width=30,
        height=3,
        bg="#F31313",
        fg="white"
    ).pack(pady=12)

    # Lado direito: saldo
    frame_saldo = tk.Frame(
        conteudo,
        bg="white",
        relief="groove",
        bd=2
    )
    frame_saldo.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    saldo = carregar_contas()[usuario_logado]["saldo"]

    tk.Label(
        frame_saldo,
        text="SALDO DISPONÍVEL",
        font=("Helvetica", 20, "bold"),
        bg="white",
        fg="#04233A"
    ).pack(pady=(70, 20))

    tk.Label(
        frame_saldo,
        text=f"R$ {saldo:.2f}",
        font=("Helvetica", 30, "bold"),
        bg="white",
        fg="#0CA120"
    ).pack(pady=20)

#==========================#
#     Janela Principal     #
#==========================#

root = tk.Tk()
root.title("Controle de gastos")
root.config(bg="#EFF0B8")
root.geometry("1000x600")
root.resizable(False, False)

tela_login()  # Abre a tela de login ao iniciar o sistema

root.mainloop()
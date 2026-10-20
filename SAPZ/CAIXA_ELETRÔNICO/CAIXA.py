import tkinter as tk
from tkinter import messagebox
import os

#===============#
#   VARIÁVEIS   #
#===============#

caminho_saldo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SALDO.txt")
usuario_logado = None
SALDO_INICIAL = 1000


#=======================#
#   ARQUIVO DE CONTAS   #
#=======================#

def carregar_contas():
    contas = {}

    if os.path.exists(caminho_saldo):
        with open(caminho_saldo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            partes = linha.strip().split(",")

            if len(partes) == 3:
                nome, senha, saldo = partes
                try:
                    contas[nome] = {"senha": senha, "saldo": int(saldo)}
                except ValueError:
                    continue

            elif len(partes) == 1 and partes[0].isdigit():
                # Migra o saldo do formato antigo para a conta user
                contas["user"] = {"senha": "1", "saldo": int(partes[0])}

    if "user" not in contas:
        contas["user"] = {"senha": "1", "saldo": SALDO_INICIAL}

    salvar_contas(contas)
    return contas


def salvar_contas(contas):
    with open(caminho_saldo, "w", encoding="utf-8") as arquivo:
        for nome, dados in contas.items():
            arquivo.write(f"{nome},{dados['senha']},{dados['saldo']}\n")


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


#===============#
#    FUNÇÕES    #
#===============#

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
        caixa()
    else:
        messagebox.showerror("Login inválido", "Usuário ou senha incorretos.")


def caixa():
    limpar_root()
    root.geometry("1000x600")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    tk.Label(frame, text=f"CAIXA ELETRÔNICO\nUsuário: {usuario_logado}", font=("Helvetica", 25, "bold"), bg="light yellow", fg="#04233A").pack(pady=20)

    saldo = carregar_contas()[usuario_logado]["saldo"]
    tk.Label(frame, text=f"SALDO\n\nR$ {saldo:.2f}", font=("Helvetica", 25, "bold"), bg="light yellow").pack(pady=20)

    tk.Button(frame, text="DEPOSITAR DINHEIRO", command=b_depositar, width=35, height=3, bg="#0CA120", fg="white").pack(pady=10)
    tk.Button(frame, text="SACAR DINHEIRO", command=b_sacar, width=35, height=3, bg="#E09625", fg="white").pack(pady=10)
    tk.Button(frame, text="SAIR", command=tela_login, width=35, height=3, bg="#F31313", fg="white").pack(pady=10)


def validar_valor(entrada, operacao):
    entrada = entrada.strip()

    if "," in entrada or "." in entrada:
        messagebox.showerror("Valor inválido", "Não é permitido usar vírgula ou ponto.\nDigite um valor inteiro, por exemplo: 50.")
        return None

    try:
        valor = int(entrada)
    except ValueError:
        messagebox.showerror("Valor inválido", f"Digite um valor inteiro válido para o {operacao}.")
        return None

    if valor <= 0:
        messagebox.showerror("Valor inválido", "Digite um valor maior que zero.")
        return None

    return valor


def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    possiveis = [False] * (valor + 1)
    possiveis[0] = True

    for quantia in range(1, valor + 1):
        for cedula in cedulas:
            if quantia >= cedula and possiveis[quantia - cedula]:
                possiveis[quantia] = True
                break

    if not possiveis[valor]:
        return None

    usadas = {cedula: 0 for cedula in cedulas}
    restante = valor

    while restante > 0:
        for cedula in cedulas:
            if restante >= cedula and possiveis[restante - cedula]:
                usadas[cedula] += 1
                restante -= cedula
                break

    return usadas


def formatar_cedulas(usadas):
    return "".join(f"{quantidade}x R$ {cedula:.2f}\n" for cedula, quantidade in usadas.items() if quantidade > 0)


def sacar():
    valor = validar_valor(sacar_entry.get(), "saque")
    if valor is None:
        return

    usadas = calcular_cedulas(valor)

    if usadas is None:
        messagebox.showerror("Valor inválido", "O saque deve usar cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.")
        return

    contas = carregar_contas()
    saldo = contas[usuario_logado]["saldo"]

    if valor > saldo:
        messagebox.showerror("Saldo insuficiente", f"Seu saldo atual é de R$ {saldo:.2f}.")
        return

    saldo -= valor
    contas[usuario_logado]["saldo"] = saldo
    salvar_contas(contas)

    messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado!\n\nCédulas sacadas:\n{formatar_cedulas(usadas)}Saldo restante: R$ {saldo:.2f}")
    caixa()


def depositar():
    valor = validar_valor(depositar_entry.get(), "depósito")
    if valor is None:
        return

    usadas = calcular_cedulas(valor)

    if usadas is None:
        messagebox.showerror("Valor inválido", "O depósito deve usar cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.")
        return

    contas = carregar_contas()
    saldo = contas[usuario_logado]["saldo"] + valor
    contas[usuario_logado]["saldo"] = saldo
    salvar_contas(contas)

    messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado!\n\nCédulas depositadas:\n{formatar_cedulas(usadas)}Novo saldo: R$ {saldo:.2f}")
    caixa()


def b_sacar():
    global sacar_entry

    limpar_root()
    root.geometry("500x300")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    sacar_entry = tk.Entry(frame, font=("Arial", 20))
    sacar_entry.pack(fill="x", padx=20, pady=20)

    tk.Button(frame, text="SACAR", font=("Arial", 20), command=sacar).pack(fill="x", padx=20, pady=5)
    tk.Button(frame, text="VOLTAR", command=caixa).pack(pady=5)


def b_depositar():
    global depositar_entry

    limpar_root()
    root.geometry("500x300")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor="center")

    depositar_entry = tk.Entry(frame, font=("Arial", 20))
    depositar_entry.pack(fill="x", padx=20, pady=20)

    tk.Button(frame, text="DEPOSITAR", font=("Arial", 20), command=depositar).pack(fill="x", padx=20, pady=5)
    tk.Button(frame, text="VOLTAR", command=caixa).pack(pady=5)


#=======================#
#   TELAS DE ACESSO     #
#=======================#

def tela_login():
    global entry_user, entry_senha

    limpar_root()
    root.geometry("350x450")
    root.resizable(False, False)
    root.configure(bg="#04233A")
    root.grid_columnconfigure(0, weight=1)

    tk.Label(root, text="BEM VINDO AO\nCAIXA ELETRÔNICO", font=("Helvetica", 20, "bold"), bg="#04233A", fg="white").grid(row=0, column=0, pady=15)
    tk.Label(root, text="Usuário:", font=("Helvetica", 17, "bold"), bg="#04233A", fg="white").grid(row=1, column=0, pady=5)

    entry_user = tk.Entry(root, width=25)
    entry_user.grid(row=2, column=0, ipady=8)

    tk.Label(root, text="Senha:", font=("Helvetica", 17, "bold"), bg="#04233A", fg="white").grid(row=3, column=0, pady=5)

    entry_senha = tk.Entry(root, width=25, show="*")
    entry_senha.grid(row=4, column=0, ipady=8)

    tk.Button(root, text="ENTRAR", command=login, width=25, height=2, bg="#0CA120", fg="white").grid(row=5, column=0, pady=12)
    tk.Button(root, text="CRIAR CONTA", command=tela_criar_conta, width=25, height=2, bg="#2471A3", fg="white").grid(row=6, column=0, pady=5)
    tk.Button(root, text="SAIR", command=root.destroy, width=25, height=2, bg="#F31313", fg="white").grid(row=7, column=0, pady=5)


def tela_criar_conta():
    global entry_novo_usuario, entry_nova_senha

    limpar_root()
    root.geometry("400x400")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="center")

    tk.Label(frame, text="CRIAR CONTA", font=("Helvetica", 22, "bold"), bg="light yellow", fg="#04233A").pack(pady=20)
    tk.Label(frame, text="Novo usuário:", font=("Arial", 14), bg="light yellow").pack(pady=5)

    entry_novo_usuario = tk.Entry(frame, font=("Arial", 16))
    entry_novo_usuario.pack(padx=20, fill="x")

    tk.Label(frame, text="Nova senha:", font=("Arial", 14), bg="light yellow").pack(pady=5)

    entry_nova_senha = tk.Entry(frame, font=("Arial", 16), show="*")
    entry_nova_senha.pack(padx=20, fill="x")

    tk.Button(frame, text="CRIAR CONTA", command=criar_conta, width=25, height=2, bg="#0CA120", fg="white").pack(pady=15)
    tk.Button(frame, text="VOLTAR", command=tela_login, width=25).pack()


#=======================#
#   JANELA PRINCIPAL    #
#=======================#

root = tk.Tk()
root.title("SAPZ - Caixa Eletrônico")
root.config(bg="#04233A")

carregar_contas()
tela_login()
root.mainloop()
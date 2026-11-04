import tkinter as tk
from tkinter import messagebox, ttk
import os
import json
from datetime import datetime


#===================#
#     Variaveis     #
#===================#

caminho_json = os.path.join(os.path.dirname(__file__), "contas.json")
caminho_move = os.path.join(os.path.dirname(__file__), "move.json")

SALDO_INICIAL = 0
usuario_logado = None


#=================#
#     Funções     #
#=================#

def limpar_root():
    for widget in root.winfo_children():
        widget.destroy()


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
        contas["user"] = {
            "senha": "1",
            "saldo": SALDO_INICIAL
        }

    salvar_contas(contas)
    return contas


def salvar_contas(contas):
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(
            {"contas": contas},
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_movimentacoes():
    if not os.path.exists(caminho_move):
        return []

    try:
        with open(caminho_move, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        movimentacoes = dados.get("movimentacoes", [])

        if not isinstance(movimentacoes, list):
            raise ValueError

        return movimentacoes

    except (OSError, json.JSONDecodeError, ValueError, AttributeError):
        messagebox.showerror(
            "Erro",
            "Não foi possível ler o arquivo move.json."
        )
        return None


def salvar_movimentacoes(movimentacoes):
    with open(caminho_move, "w", encoding="utf-8") as arquivo:
        json.dump(
            {"movimentacoes": movimentacoes},
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def sair():
    global usuario_logado
    usuario_logado = None
    tela_login()


def login():
    global usuario_logado

    nome = entry_user.get().strip()
    senha = entry_senha.get()

    contas = carregar_contas()

    if nome in contas and contas[nome]["senha"] == senha:
        usuario_logado = nome
        controle()
    else:
        messagebox.showerror(
            "Login inválido",
            "Usuário ou senha incorretos."
        )


def criar_conta():
    nome = entry_novo_usuario.get().strip()
    senha = entry_nova_senha.get()

    if not nome or not senha:
        messagebox.showerror(
            "Erro",
            "Preencha o usuário e a senha."
        )
        return

    if "," in nome or "," in senha or "\n" in nome or "\n" in senha:
        messagebox.showerror(
            "Erro",
            "Não use vírgulas ou quebras de linha."
        )
        return

    contas = carregar_contas()

    if nome in contas:
        messagebox.showerror(
            "Erro",
            "Esse usuário já existe."
        )
        return

    contas[nome] = {
        "senha": senha,
        "saldo": SALDO_INICIAL
    }

    salvar_contas(contas)

    messagebox.showinfo(
        "Conta criada",
        f"Conta de {nome} criada com sucesso!\n"
        f"Saldo inicial: R$ {SALDO_INICIAL:.2f}"
    )

    tela_login()


#=============================#
#   ADICIONAR MOVIMENTAÇÃO    #
#=============================#

def adicionar_movimentacao(tipo):
    descricao = desc_entry.get().strip()
    valor_texto = val_entry.get().strip().replace(",", ".")
    data = dat_entry.get().strip()

    if not descricao or not valor_texto or not data:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos."
        )
        return

    try:
        valor = float(valor_texto)

        if valor <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um valor maior que zero."
        )
        return

    try:
        datetime.strptime(data, "%d/%m/%Y")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Use a data no formato DD/MM/AAAA."
        )
        return

    if usuario_logado is None:
        messagebox.showerror(
            "Erro",
            "Nenhum usuário está logado."
        )
        return

    movimentacoes = carregar_movimentacoes()

    if movimentacoes is None:
        return

    contas = carregar_contas()

    movimentacoes.append({
        "usuario": usuario_logado,
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor,
        "data": data
    })

    if tipo == "receita":
        contas[usuario_logado]["saldo"] += valor

    else:
        if contas[usuario_logado]["saldo"] < valor:
            messagebox.showerror(
                "Saldo insuficiente",
                "Você não possui saldo suficiente."
            )
            return

        contas[usuario_logado]["saldo"] -= valor

    try:
        salvar_movimentacoes(movimentacoes)
        salvar_contas(contas)

    except OSError:
        messagebox.showerror(
            "Erro",
            "Não foi possível salvar os dados."
        )
        return

    messagebox.showinfo(
        "Sucesso",
        f"{tipo.capitalize()} adicionada com sucesso!"
    )

    controle()


def adicionar_receita():
    adicionar_movimentacao("receita")


def adicionar_despesa():
    adicionar_movimentacao("despesa")


#=============================#
#   FILTRAR MOVIMENTAÇÕES     #
#=============================#

def obter_movimentacoes_usuario():
    movimentacoes = carregar_movimentacoes()

    if movimentacoes is None:
        return None

    resultado = []

    for indice, mov in enumerate(movimentacoes):
        if mov.get("usuario") == usuario_logado:
            resultado.append((indice, mov))

    return resultado


def filtrar_por_data(movimentacoes, data_inicial, data_final):

    try:
        inicio = None
        fim = None

        if data_inicial.strip():
            inicio = datetime.strptime(
                data_inicial.strip(),
                "%d/%m/%Y"
            )

        if data_final.strip():
            fim = datetime.strptime(
                data_final.strip(),
                "%d/%m/%Y"
            )

        if inicio and fim and inicio > fim:
            messagebox.showerror(
                "Erro",
                "A data inicial não pode ser maior que a data final."
            )
            return None

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite as datas no formato DD/MM/AAAA."
        )
        return None

    resultado = []

    for indice, mov in movimentacoes:
        try:
            data_mov = datetime.strptime(
                mov["data"],
                "%d/%m/%Y"
            )
        except (ValueError, KeyError, TypeError):
            continue

        if inicio and data_mov < inicio:
            continue

        if fim and data_mov > fim:
            continue

        resultado.append((indice, mov))

    resultado.sort(
        key=lambda item: datetime.strptime(
            item[1]["data"],
            "%d/%m/%Y"
        )
    )

    return resultado


#=============================#
#     EXCLUIR MOVIMENTAÇÃO    #
#=============================#

def excluir_movimentacao():
    selecionado = tabela_excluir.selection()

    if not selecionado:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma movimentação para excluir."
        )
        return

    indice = int(selecionado[0])

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        "Tem certeza que deseja excluir essa movimentação?"
    )

    if not confirmar:
        return

    movimentacoes = carregar_movimentacoes()

    if movimentacoes is None:
        return

    if indice >= len(movimentacoes):
        messagebox.showerror(
            "Erro",
            "Movimentação não encontrada."
        )
        return

    mov = movimentacoes[indice]

    if mov.get("usuario") != usuario_logado:
        messagebox.showerror(
            "Erro",
            "Você não pode excluir movimentações de outro usuário."
        )
        return

    contas = carregar_contas()
    valor = float(mov["valor"])

    if mov["tipo"] == "receita":
        contas[usuario_logado]["saldo"] -= valor

    elif mov["tipo"] == "despesa":
        contas[usuario_logado]["saldo"] += valor

    movimentacoes.pop(indice)

    try:
        salvar_movimentacoes(movimentacoes)
        salvar_contas(contas)

    except OSError:
        messagebox.showerror(
            "Erro",
            "Não foi possível salvar os dados."
        )
        return

    messagebox.showinfo(
        "Sucesso",
        "Movimentação excluída com sucesso!"
    )

    tela_excluir_movimentacoes()


#=============================#
#       RELATÓRIO             #
#=============================#

def gerar_relatorio():
    movimentacoes = obter_movimentacoes_usuario()

    if movimentacoes is None:
        return

    total_receitas = 0
    total_despesas = 0
    quantidade = 0

    for indice, mov in movimentacoes:
        valor = float(mov["valor"])

        if mov["tipo"] == "receita":
            total_receitas += valor

        elif mov["tipo"] == "despesa":
            total_despesas += valor

        quantidade += 1

    contas = carregar_contas()
    saldo = contas[usuario_logado]["saldo"]

    limpar_root()

    root.geometry("600x600")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.9,
        relheight=0.9,
        anchor="center"
    )

    tk.Label(
        frame,
        text="RELATÓRIO FINANCEIRO",
        font=("Helvetica", 24, "bold"),
        bg="light yellow",
        fg="#04233A"
    ).pack(pady=25)

    tk.Label(
        frame,
        text=f"Usuário: {usuario_logado}",
        font=("Arial", 15, "bold"),
        bg="light yellow"
    ).pack(pady=10)

    tk.Label(
        frame,
        text="TOTAL DE RECEITAS",
        font=("Arial", 16, "bold"),
        bg="light yellow",
        fg="#0CA120"
    ).pack(pady=(20, 0))

    tk.Label(
        frame,
        text=f"R$ {total_receitas:.2f}",
        font=("Arial", 20, "bold"),
        bg="light yellow",
        fg="#0CA120"
    ).pack()

    tk.Label(
        frame,
        text="TOTAL DE DESPESAS",
        font=("Arial", 16, "bold"),
        bg="light yellow",
        fg="#E05125"
    ).pack(pady=(15, 0))

    tk.Label(
        frame,
        text=f"R$ {total_despesas:.2f}",
        font=("Arial", 20, "bold"),
        bg="light yellow",
        fg="#E05125"
    ).pack()

    tk.Label(
        frame,
        text="SALDO ATUAL",
        font=("Arial", 16, "bold"),
        bg="light yellow",
        fg="#04233A"
    ).pack(pady=(15, 0))

    tk.Label(
        frame,
        text=f"R$ {saldo:.2f}",
        font=("Arial", 22, "bold"),
        bg="light yellow",
        fg="#04233A"
    ).pack()

    tk.Label(
        frame,
        text="QUANTIDADE DE MOVIMENTAÇÕES",
        font=("Arial", 14, "bold"),
        bg="light yellow"
    ).pack(pady=(20, 0))

    tk.Label(
        frame,
        text=str(quantidade),
        font=("Arial", 22, "bold"),
        bg="light yellow"
    ).pack()

    tk.Button(
        frame,
        text="VOLTAR",
        command=controle,
        width=25,
        height=2
    ).pack(pady=25)


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

    tk.Label(
        root,
        text="BEM VINDO AO\nCONTROLE DE GASTOS",
        font=("Helvetica", 20, "bold"),
        bg="#EFF0B8",
        fg="black"
    ).grid(row=0, column=0, pady=15)

    tk.Label(
        root,
        text="Usuário:",
        font=("Helvetica", 17, "bold"),
        bg="#EFF0B8",
        fg="black"
    ).grid(row=1, column=0, pady=5)

    entry_user = tk.Entry(root, width=25)
    entry_user.grid(row=2, column=0, ipady=8)

    tk.Label(
        root,
        text="Senha:",
        font=("Helvetica", 17, "bold"),
        bg="#EFF0B8",
        fg="black"
    ).grid(row=3, column=0, pady=5)

    entry_senha = tk.Entry(root, width=25, show="*")
    entry_senha.grid(row=4, column=0, ipady=8)

    tk.Button(
        root,
        text="ENTRAR",
        command=login,
        width=25,
        height=2,
        bg="#0CA120",
        fg="white"
    ).grid(row=5, column=0, pady=12)

    tk.Button(
        root,
        text="CRIAR CONTA",
        command=tela_criar_conta,
        width=25,
        height=2,
        bg="#2471A3",
        fg="white"
    ).grid(row=6, column=0, pady=5)

    tk.Button(
        root,
        text="SAIR",
        command=root.destroy,
        width=25,
        height=2,
        bg="#F31313",
        fg="white"
    ).grid(row=7, column=0, pady=5)


def tela_criar_conta():
    global entry_novo_usuario, entry_nova_senha

    limpar_root()

    root.geometry("400x400")
    root.configure(bg="#EFF0B8")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.9,
        relheight=0.9,
        anchor="center"
    )

    tk.Label(
        frame,
        text="CRIAR CONTA",
        font=("Helvetica", 22, "bold"),
        bg="light yellow",
        fg="black"
    ).pack(pady=20)

    tk.Label(
        frame,
        text="Novo usuário:",
        font=("Arial", 14),
        bg="light yellow"
    ).pack(pady=5)

    entry_novo_usuario = tk.Entry(
        frame,
        font=("Arial", 16)
    )
    entry_novo_usuario.pack(padx=20, fill="x")

    tk.Label(
        frame,
        text="Nova senha:",
        font=("Arial", 14),
        bg="light yellow"
    ).pack(pady=5)

    entry_nova_senha = tk.Entry(
        frame,
        font=("Arial", 16),
        show="*"
    )
    entry_nova_senha.pack(padx=20, fill="x")

    tk.Button(
        frame,
        text="CRIAR CONTA",
        command=criar_conta,
        width=25,
        height=2,
        bg="#0CA120",
        fg="white"
    ).pack(pady=15)

    tk.Button(
        frame,
        text="VOLTAR",
        command=tela_login,
        width=25
    ).pack()


#=============================#
#     TELA PRINCIPAL          #
#=============================#

def controle():
    limpar_root()

    root.geometry("1000x700")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.95,
        relheight=0.9,
        anchor="center"
    )

    tk.Label(
        frame,
        text=f"CONTROLE DE GASTOS\nUsuário: {usuario_logado}",
        font=("Helvetica", 25, "bold"),
        bg="light yellow",
        fg="#050B0F"
    ).pack(pady=20)

    conteudo = tk.Frame(frame, bg="light yellow")
    conteudo.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    conteudo.grid_columnconfigure(0, weight=1)
    conteudo.grid_columnconfigure(1, weight=1)
    conteudo.grid_rowconfigure(0, weight=1)

    frame_botoes = tk.Frame(
        conteudo,
        bg="light yellow"
    )
    frame_botoes.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=20,
        pady=10
    )

    tk.Button(
        frame_botoes,
        text="ADICIONAR RECEITA",
        command=tela_adicionar_receita,
        width=30,
        height=3,
        bg="#0CA120",
        fg="white"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="ADICIONAR DESPESA",
        command=tela_adicionar_despesa,
        width=30,
        height=3,
        bg="#E05125",
        fg="white"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="MOVIMENTAÇÕES",
        command=tela_movimentacoes,
        width=30,
        height=3,
        bg="#20D16A",
        fg="white"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="EXCLUIR MOVIMENTAÇÕES",
        command=tela_excluir_movimentacoes,
        width=30,
        height=3,
        bg="#D1D422",
        fg="black"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="RELATÓRIO",
        command=gerar_relatorio,
        width=30,
        height=3,
        bg="#D1D422",
        fg="black"
    ).pack(pady=12)

    tk.Button(
        frame_botoes,
        text="SAIR",
        command=sair,
        width=30,
        height=3,
        bg="#F31313",
        fg="white"
    ).pack(pady=12)

    frame_saldo = tk.Frame(
        conteudo,
        bg="white",
        relief="groove",
        bd=2
    )

    frame_saldo.grid(
        row=0,
        column=1,
        sticky="nsew",
        padx=20,
        pady=20
    )

    saldo = carregar_contas()[usuario_logado]["saldo"]

    tk.Label(
        frame_saldo,
        text="SALDO DISPONÍVEL",
        font=("Helvetica", 20, "bold"),
        bg="white",
        fg="#04233A"
    ).pack(pady=(70, 20))

    cor_saldo = "#0CA120" if saldo >= 0 else "#E05125"

    tk.Label(
        frame_saldo,
        text=f"R$ {saldo:.2f}",
        font=("Helvetica", 30, "bold"),
        bg="white",
        fg=cor_saldo
    ).pack(pady=20)


#=============================#
#   ADICIONAR RECEITA         #
#=============================#

def tela_adicionar_receita():
    global desc_entry, val_entry, dat_entry

    limpar_root()

    root.geometry("500x370")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.95,
        relheight=0.9,
        anchor="center"
    )

    tk.Label(
        frame,
        text="ADICIONAR RECEITA",
        font=("Arial", 22, "bold"),
        bg="light yellow"
    ).pack(pady=10)

    tk.Label(
        frame,
        text="Descrição:",
        font=("Arial", 13),
        bg="light yellow"
    ).pack()

    desc_entry = tk.Entry(
        frame,
        font=("Arial", 18),
        justify="center"
    )
    desc_entry.pack(fill="x", padx=20, pady=5)

    tk.Label(
        frame,
        text="Valor:",
        font=("Arial", 13),
        bg="light yellow"
    ).pack()

    val_entry = tk.Entry(
        frame,
        font=("Arial", 18),
        justify="center"
    )
    val_entry.pack(fill="x", padx=20, pady=5)

    tk.Label(
        frame,
        text="Data (DD/MM/AAAA):",
        font=("Arial", 13),
        bg="light yellow"
    ).pack()

    dat_entry = tk.Entry(
        frame,
        font=("Arial", 18),
        justify="center"
    )
    dat_entry.pack(fill="x", padx=20, pady=5)

    tk.Button(
        frame,
        text="ADICIONAR",
        font=("Arial", 15),
        command=adicionar_receita,
        bg="#0CA120",
        fg="white"
    ).pack(fill="x", padx=20, pady=8)

    tk.Button(
        frame,
        text="VOLTAR",
        command=controle
    ).pack(pady=5)


#=============================#
#   ADICIONAR DESPESA         #
#=============================#

def tela_adicionar_despesa():
    global desc_entry, val_entry, dat_entry

    limpar_root()

    root.geometry("500x370")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.95,
        relheight=0.9,
        anchor="center"
    )

    tk.Label(
        frame,
        text="ADICIONAR DESPESA",
        font=("Arial", 22, "bold"),
        bg="light yellow"
    ).pack(pady=10)

    tk.Label(
        frame,
        text="Descrição:",
        font=("Arial", 13),
        bg="light yellow"
    ).pack()

    desc_entry = tk.Entry(
        frame,
        font=("Arial", 18),
        justify="center"
    )
    desc_entry.pack(fill="x", padx=20, pady=5)

    tk.Label(
        frame,
        text="Valor:",
        font=("Arial", 13),
        bg="light yellow"
    ).pack()

    val_entry = tk.Entry(
        frame,
        font=("Arial", 18),
        justify="center"
    )
    val_entry.pack(fill="x", padx=20, pady=5)

    tk.Label(
        frame,
        text="Data (DD/MM/AAAA):",
        font=("Arial", 13),
        bg="light yellow"
    ).pack()

    dat_entry = tk.Entry(
        frame,
        font=("Arial", 18),
        justify="center"
    )
    dat_entry.pack(fill="x", padx=20, pady=5)

    tk.Button(
        frame,
        text="ADICIONAR",
        font=("Arial", 15),
        command=adicionar_despesa,
        bg="#E05125",
        fg="white"
    ).pack(fill="x", padx=20, pady=8)

    tk.Button(
        frame,
        text="VOLTAR",
        command=controle
    ).pack(pady=5)


#=============================#
#       MOVIMENTAÇÕES         #
#=============================#

def tela_movimentacoes():
    global inicio_entry, fim_entry, tabela_mov

    limpar_root()

    root.geometry("950x650")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.95,
        relheight=0.93,
        anchor="center"
    )

    tk.Label(
        frame,
        text="MOVIMENTAÇÕES",
        font=("Helvetica", 24, "bold"),
        bg="light yellow"
    ).pack(pady=15)

    frame_datas = tk.Frame(frame, bg="light yellow")
    frame_datas.pack(pady=5)

    tk.Label(
        frame_datas,
        text="Data inicial:",
        font=("Arial", 12, "bold"),
        bg="light yellow"
    ).grid(row=0, column=0, padx=5)

    inicio_entry = tk.Entry(
        frame_datas,
        font=("Arial", 13),
        width=15,
        justify="center"
    )
    inicio_entry.grid(row=0, column=1, padx=5)

    tk.Label(
        frame_datas,
        text="Data final:",
        font=("Arial", 12, "bold"),
        bg="light yellow"
    ).grid(row=0, column=2, padx=5)

    fim_entry = tk.Entry(
        frame_datas,
        font=("Arial", 13),
        width=15,
        justify="center"
    )
    fim_entry.grid(row=0, column=3, padx=5)

    tk.Button(
        frame_datas,
        text="FILTRAR",
        command=atualizar_movimentacoes
    ).grid(row=0, column=4, padx=10)

    tk.Label(
        frame,
        text="Deixe as datas em branco para mostrar todas as movimentações.",
        font=("Arial", 10),
        bg="light yellow"
    ).pack(pady=5)

    colunas = ("data", "tipo", "descricao", "valor")

    tabela_mov = ttk.Treeview(
        frame,
        columns=colunas,
        show="headings",
        height=16
    )

    tabela_mov.heading("data", text="Data")
    tabela_mov.heading("tipo", text="Tipo")
    tabela_mov.heading("descricao", text="Descrição")
    tabela_mov.heading("valor", text="Valor")

    tabela_mov.column("data", width=120, anchor="center")
    tabela_mov.column("tipo", width=120, anchor="center")
    tabela_mov.column("descricao", width=350, anchor="center")
    tabela_mov.column("valor", width=150, anchor="center")

    tabela_mov.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    tk.Button(
        frame,
        text="VOLTAR",
        command=controle,
        width=25,
        height=2
    ).pack(pady=10)

    atualizar_movimentacoes()


def atualizar_movimentacoes():
    for item in tabela_mov.get_children():
        tabela_mov.delete(item)

    movimentacoes = obter_movimentacoes_usuario()

    if movimentacoes is None:
        return

    resultado = filtrar_por_data(
        movimentacoes,
        inicio_entry.get(),
        fim_entry.get()
    )

    if resultado is None:
        return

    for indice, mov in resultado:
        tipo = mov["tipo"].upper()

        tabela_mov.insert(
            "",
            "end",
            values=(
                mov["data"],
                tipo,
                mov["descricao"],
                f'R$ {float(mov["valor"]):.2f}'
            )
        )


#=============================#
#    EXCLUIR MOVIMENTAÇÕES    #
#=============================#

def tela_excluir_movimentacoes():
    global tabela_excluir

    limpar_root()

    root.geometry("950x650")
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.95,
        relheight=0.93,
        anchor="center"
    )

    tk.Label(
        frame,
        text="EXCLUIR MOVIMENTAÇÃO",
        font=("Helvetica", 24, "bold"),
        bg="light yellow"
    ).pack(pady=15)

    tk.Label(
        frame,
        text="Selecione a movimentação que deseja excluir:",
        font=("Arial", 13),
        bg="light yellow"
    ).pack(pady=5)

    colunas = ("data", "tipo", "descricao", "valor")

    tabela_excluir = ttk.Treeview(
        frame,
        columns=colunas,
        show="headings",
        height=17
    )

    tabela_excluir.heading("data", text="Data")
    tabela_excluir.heading("tipo", text="Tipo")
    tabela_excluir.heading("descricao", text="Descrição")
    tabela_excluir.heading("valor", text="Valor")

    tabela_excluir.column("data", width=120, anchor="center")
    tabela_excluir.column("tipo", width=120, anchor="center")
    tabela_excluir.column("descricao", width=350, anchor="center")
    tabela_excluir.column("valor", width=150, anchor="center")

    tabela_excluir.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    tk.Button(
        frame,
        text="EXCLUIR SELECIONADA",
        command=excluir_movimentacao,
        width=30,
        height=2,
        bg="#E05125",
        fg="white"
    ).pack(pady=8)

    tk.Button(
        frame,
        text="VOLTAR",
        command=controle,
        width=25,
        height=2
    ).pack(pady=5)

    atualizar_tabela_exclusao()


def atualizar_tabela_exclusao():
    for item in tabela_excluir.get_children():
        tabela_excluir.delete(item)

    movimentacoes = carregar_movimentacoes()

    if movimentacoes is None:
        return

    for indice, mov in enumerate(movimentacoes):
        if mov.get("usuario") == usuario_logado:

            tabela_excluir.insert(
                "",
                "end",
                iid=str(indice),
                values=(
                    mov["data"],
                    mov["tipo"].upper(),
                    mov["descricao"],
                    f'R$ {float(mov["valor"]):.2f}'
                )
            )


#==========================#
#     JANELA PRINCIPAL     #
#==========================#

root = tk.Tk()

root.title("Controle de gastos")
root.config(bg="#EFF0B8")
root.geometry("1000x600")
root.resizable(False, False)

tela_login()

root.mainloop()
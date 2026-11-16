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

usuario_logado = None
tabela = None

#=================#
#     Funções     #
#=================#

def teste():
    print("teste")

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
    }

    salvar_contas(contas)

    messagebox.showinfo(
        "Conta criada",
        f"Conta de {nome} criada com sucesso!\n"
    )

    tela_login()

#===================#
#   NOVO PRODUTO    #
#===================#

def carregar_produtos():
    contas = carregar_contas()

    if usuario_logado not in contas:
        return []

    return contas[usuario_logado].get("produtos", [])

def atualizar_tabela():
    produtos = carregar_produtos()

    # Limpa a tabela
    for item in tabela.get_children():
        tabela.delete(item)

    # Insere os produtos
    for produto in produtos:
        tabela.insert(
            "",
            "end",
            values=(
                produto["codigo"],
                produto["descricao"],
                produto["categoria"],
                produto["quantidade"],
                f'R$ {produto["valor"]:.2f}'
            )
        )

def novo_produto():
    
    janela = tk.Toplevel(root)
    janela.title("Novo Produto")
    janela.geometry("450x500")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")

    janela.transient(root)
    janela.grab_set()

    # Centraliza a janela
    janela.update_idletasks()

    x = root.winfo_x() + (root.winfo_width() - 450) // 2
    y = root.winfo_y() + (root.winfo_height() - 500) // 2

    janela.geometry(f"+{x}+{y}")

    # Frame principal
    frame = tk.Frame(janela, bg="light yellow")
    frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.9,
        relheight=0.92,
        anchor="center"
    )

    tk.Label(
        frame,
        text="NOVO PRODUTO",
        font=("Helvetica", 20, "bold"),
        bg="light yellow"
    ).pack(pady=15)

    # DESCRIÇÃO
    tk.Label(
        frame,
        text="Descrição:",
        font=("Arial", 12, "bold"),
        bg="light yellow"
    ).pack(anchor="w", padx=20)

    entry_descricao = tk.Entry(frame, font=("Arial", 13))
    entry_descricao.pack(fill="x", padx=20, pady=5)

    # CATEGORIA
    tk.Label(
        frame,
        text="Categoria:",
        font=("Arial", 12, "bold"),
        bg="light yellow"
    ).pack(anchor="w", padx=20)

    entry_categoria = tk.Entry(frame, font=("Arial", 13))
    entry_categoria.pack(fill="x", padx=20, pady=5)

    # QUANTIDADE
    tk.Label(
        frame,
        text="Quantidade:",
        font=("Arial", 12, "bold"),
        bg="light yellow"
    ).pack(anchor="w", padx=20)

    entry_quantidade = tk.Entry(frame, font=("Arial", 13))
    entry_quantidade.pack(fill="x", padx=20, pady=5)

    # VALOR
    tk.Label(
        frame,
        text="Valor unitário (R$):",
        font=("Arial", 12, "bold"),
        bg="light yellow"
    ).pack(anchor="w", padx=20)

    entry_valor = tk.Entry(frame, font=("Arial", 13))
    entry_valor.pack(fill="x", padx=20, pady=5)

    # FUNÇÃO SALVAR
    def salvar_produto():

        descricao = entry_descricao.get().strip()
        categoria = entry_categoria.get().strip()
        quantidade = entry_quantidade.get().strip()
        valor = entry_valor.get().strip()

        # Verifica campos vazios
        if not descricao or not categoria or not quantidade or not valor:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos.",
                parent=janela
            )
            return

        # Valida quantidade
        try:
            quantidade = int(quantidade)

            if quantidade <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe uma quantidade inteira maior que zero.",
                parent=janela
            )
            return

        # Valida valor
        try:
            if "," in valor:
                valor = valor.replace(".", "").replace(",", ".")

            valor = float(valor)

            if valor < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe um valor válido.",
                parent=janela
            )
            return

        # Carrega contas
        contas = carregar_contas()

        # Inicializa produtos
        if "produtos" not in contas[usuario_logado]:
            contas[usuario_logado]["produtos"] = []

        produtos = contas[usuario_logado]["produtos"]

        # GERAÇÃO PERMANENTE DO CÓDIGO
        codigos_existentes = [
            int(p["codigo"])
            for p in produtos
            if str(p.get("codigo", "")).isdigit()
        ]

        maior_codigo = max(codigos_existentes, default=0)

        proximo_codigo = contas[usuario_logado].get("proximo_codigo")

        if proximo_codigo is None:
            proximo_codigo = maior_codigo + 1

        codigo = max(
            int(proximo_codigo),
            maior_codigo + 1
        )

        contas[usuario_logado]["proximo_codigo"] = codigo + 1

        # Cria produto
        produto = {
            "codigo": codigo,
            "descricao": descricao,
            "categoria": categoria,
            "quantidade": quantidade,
            "valor": valor
        }

        # Salva produto
        produtos.append(produto)

        salvar_contas(contas)

        # Atualiza Treeview
        atualizar_tabela()

        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado com sucesso!",
            parent=janela
        )

        janela.destroy()

    # BOTÕES
    tk.Button(
        frame,
        text="SALVAR PRODUTO",
        command=salvar_produto,
        width=25,
        height=2,
        bg="#0CA120",
        fg="white"
    ).pack(pady=15)

    tk.Button(
        frame,
        text="CANCELAR",
        command=janela.destroy,
        width=25,
        height=2
    ).pack()



#======================#
#   EXCLUIR PRODUTO    #
#======================#

#====================#
#   ALTERAR PRODUTO  #
#====================#

#==============#
#   FILTRAR    #
#==============#

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

    entry_novo_usuario = tk.Entry( frame, font=("Arial", 16))
    entry_novo_usuario.pack(padx=20, fill="x")

    tk.Label(frame, text="Nova senha:", font=("Arial", 14), bg="light yellow").pack(pady=5)

    entry_nova_senha = tk.Entry( frame, font=("Arial", 16), show="*")
    entry_nova_senha.pack(padx=20, fill="x")

    tk.Button(frame, text="CRIAR CONTA", command=criar_conta, width=25, height=2, bg="#0CA120", fg="white").pack(pady=15)

    tk.Button(frame, text="VOLTAR", command=tela_login, width=25).pack()

#=============================#
#     TELA PRINCIPAL          #
#=============================#


def controle():
    global tabela

    limpar_root()

    root.geometry("1400x800")
    root.resizable(False, False)
    root.configure(bg="#04233A")

    frame = tk.Frame(root, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95, anchor="center")

    # CONFIGURAÇÃO DAS LINHAS
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, minsize=80)
    frame.grid_rowconfigure(1, weight=1)

    # BARRA DE BOTÕES
    barra_botoes = tk.Frame(frame, bg="light yellow")
    barra_botoes.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

    tk.Button(barra_botoes, text="Novo produto", command=novo_produto, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Entrada", command=teste, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Excluir", command=teste, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Filtrar", command=teste, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Sair", command=sair, width=15, height=2).pack(side="left", padx=5)

    # ÁREA DA TABELA
    area_tabela = tk.Frame(frame, bg="white")
    area_tabela.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

    # COLUNAS
    colunas = ("codigo", "descricao", "categoria", "quantidade", "valor")

    tabela = ttk.Treeview(area_tabela, columns=colunas, show="headings")

    tabela.heading("codigo", text="Código")
    tabela.heading("descricao", text="Descrição")
    tabela.heading("categoria", text="Categoria")
    tabela.heading("quantidade", text="Quantidade")
    tabela.heading("valor", text="Valor")

    tabela.column("codigo", width=100, anchor="center")
    tabela.column("descricao", width=400, anchor="center")
    tabela.column("categoria", width=250, anchor="center")
    tabela.column("quantidade", width=150, anchor="center")
    tabela.column("valor", width=150, anchor="center")
    # SCROLLBAR
    scrollbar = ttk.Scrollbar(area_tabela, orient="vertical", command=tabela.yview)

    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # CARREGA PRODUTOS
    atualizar_tabela()

    
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
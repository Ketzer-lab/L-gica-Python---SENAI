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
    return contas.get(usuario_logado, {}).get("produtos", [])

def atualizar_tabela():
    tabela.delete(*tabela.get_children())
    for p in carregar_produtos():
        tabela.insert("", "end", values=(p["codigo"], p["descricao"], p["categoria"], p["quantidade"], f'R$ {p["valor"]:.2f}'))

def novo_produto():
    janela = tk.Toplevel(root)
    janela.title("Novo Produto")
    janela.geometry("450x500")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")
    janela.transient(root)
    janela.grab_set()

    janela.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() - 450) // 2
    y = root.winfo_y() + (root.winfo_height() - 500) // 2
    janela.geometry(f"+{x}+{y}")

    frame = tk.Frame(janela, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.92, anchor="center")

    tk.Label(frame, text="NOVO PRODUTO", font=("Helvetica", 20, "bold"), bg="light yellow").pack(pady=15)

    tk.Label(frame, text="Descrição:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_descricao = tk.Entry(frame, font=("Arial", 13))
    entry_descricao.pack(fill="x", padx=20, pady=5)

    tk.Label(frame, text="Categoria:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_categoria = tk.Entry(frame, font=("Arial", 13))
    entry_categoria.pack(fill="x", padx=20, pady=5)

    tk.Label(frame, text="Quantidade:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_quantidade = tk.Entry(frame, font=("Arial", 13))
    entry_quantidade.pack(fill="x", padx=20, pady=5)

    tk.Label(frame, text="Valor unitário (R$):", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_valor = tk.Entry(frame, font=("Arial", 13))
    entry_valor.pack(fill="x", padx=20, pady=5)

    # SALVAR PRODUTO
    def salvar_produto():
        descricao = entry_descricao.get().strip()
        categoria = entry_categoria.get().strip()
        quantidade = entry_quantidade.get().strip()
        valor = entry_valor.get().strip()

        if not all([descricao, categoria, quantidade, valor]):
            messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela)
            return

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe uma quantidade inteira maior que zero.", parent=janela)
            return

        try:
            valor = float(valor.replace(".", "").replace(",", ".") if "," in valor else valor)
            if valor < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe um valor válido.", parent=janela)
            return

        contas = carregar_contas()
        produtos = contas[usuario_logado].setdefault("produtos", [])

        # GERAÇÃO PERMANENTE DO CÓDIGO
        maior_codigo = max((int(p["codigo"]) for p in produtos if str(p.get("codigo", "")).isdigit()), default=0)
        codigo = max(int(contas[usuario_logado].get("proximo_codigo") or 1), maior_codigo + 1)
        contas[usuario_logado]["proximo_codigo"] = codigo + 1

        produtos.append({
            "codigo": codigo,
            "descricao": descricao,
            "categoria": categoria,
            "quantidade": quantidade,
            "valor": valor
        })

        salvar_contas(contas)
        atualizar_tabela()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!", parent=janela)
        janela.destroy()

    tk.Button(frame, text="SALVAR PRODUTO", command=salvar_produto, width=25, height=2, bg="#0CA120", fg="white").pack(pady=15)
    tk.Button(frame, text="CANCELAR", command=janela.destroy, width=25, height=2).pack()

#=============================#
#     MOVIMENTAÇÃO            #
#=============================#

def movimentacao():
    janela = tk.Toplevel(root)
    janela.title("Movimentação")
    janela.geometry("450x600")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")
    janela.transient(root)
    janela.grab_set()

    produtos = carregar_produtos()

    frame = tk.Frame(janela, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.95, anchor="center")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(3, weight=1)

    tk.Label(frame, text="SELECIONE O PRODUTO", font=("Helvetica", 17, "bold"), bg="light yellow").grid(row=0, column=0, pady=15)
    tk.Label(frame, text="Pesquisar por código ou descrição:", font=("Arial", 11, "bold"), bg="light yellow").grid(row=1, column=0, sticky="w", padx=10)

    entry_pesquisa = tk.Entry(frame, font=("Arial", 12))
    entry_pesquisa.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    lista = ttk.Treeview(frame, columns=("codigo", "descricao"), show="headings")
    lista.heading("codigo", text="Código")
    lista.heading("descricao", text="Descrição")
    lista.column("codigo", width=80, anchor="center")
    lista.column("descricao", width=270, anchor="center")
    lista.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

    def atualizar_lista(event=None):
        pesquisa = entry_pesquisa.get().strip().lower()
        lista.delete(*lista.get_children())

        for p in produtos:
            if pesquisa in str(p["codigo"]).lower() or pesquisa in p["descricao"].lower():
                lista.insert("", "end", values=(p["codigo"], p["descricao"]))

    def selecionar():
        selecionado = lista.selection()

        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um produto.", parent=janela)
            return

        codigo = int(lista.item(selecionado[0], "values")[0])
        produto = next((p for p in produtos if int(p["codigo"]) == codigo), None)

        if produto:
            janela.destroy()
            janela_movimentacao_produto(produto)

    entry_pesquisa.bind("<KeyRelease>", atualizar_lista)
    atualizar_lista()

    tk.Button(frame, text="SELECIONAR", command=selecionar, width=20, height=2, bg="#0CA120", fg="white").grid(row=4, column=0, pady=5)
    tk.Button(frame, text="CANCELAR", command=janela.destroy, width=20, height=2).grid(row=5, column=0, pady=5)


def janela_movimentacao_produto(produto):
    janela = tk.Toplevel(root)
    janela.title("Movimentação")
    janela.geometry("420x450")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")
    janela.transient(root)
    janela.grab_set()

    frame = tk.Frame(janela, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.95, anchor="center")

    tk.Label(frame, text="MOVIMENTAÇÃO", font=("Helvetica", 20, "bold"), bg="light yellow").pack(pady=15)
    tk.Label(frame, text=produto["descricao"], font=("Arial", 15, "bold"), bg="light yellow").pack(pady=5)
    tk.Label(frame, text=f"Estoque atual: {produto['quantidade']} unidades", font=("Arial", 12), bg="light yellow").pack(pady=5)

    tk.Label(frame, text="Tipo de movimentação:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20, pady=(15, 5))

    combo_tipo = ttk.Combobox(frame, values=["Entrada", "Saída"], state="readonly", font=("Arial", 13))
    combo_tipo.pack(fill="x", padx=20)
    combo_tipo.set("Entrada")

    tk.Label(frame, text="Quantidade:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20, pady=(15, 5))

    entry_quantidade = tk.Entry(frame, font=("Arial", 13), justify="center")
    entry_quantidade.pack(fill="x", padx=20)

    tk.Label(frame, text="Data (dd/mm/aaaa):", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20, pady=(15, 5))

    entry_data = tk.Entry(frame, font=("Arial", 13), justify="center")
    entry_data.pack(fill="x", padx=20)
    entry_data.insert(0, datetime.now().strftime("%d/%m/%Y"))

    def concluir():
        tipo = combo_tipo.get()
        data = entry_data.get().strip()

        try:
            quantidade = int(entry_quantidade.get())
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe uma quantidade inteira maior que zero.", parent=janela)
            return

        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Erro", "Informe uma data válida no formato dd/mm/aaaa.", parent=janela)
            return

        contas = carregar_contas()
        conta = contas[usuario_logado]
        produtos = conta.get("produtos", [])

        atual = next((p for p in produtos if int(p["codigo"]) == int(produto["codigo"])), None)

        if atual is None:
            messagebox.showerror("Erro", "Produto não encontrado.", parent=janela)
            return

        if tipo == "Entrada":
            atual["quantidade"] = int(atual["quantidade"]) + quantidade
        else:
            if quantidade > int(atual["quantidade"]):
                messagebox.showerror("Erro", "Estoque insuficiente.", parent=janela)
                return
            atual["quantidade"] = int(atual["quantidade"]) - quantidade

        conta.setdefault("movimentacoes", []).append({
            "codigo": atual["codigo"],
            "descricao": atual["descricao"],
            "tipo": tipo,
            "quantidade": quantidade,
            "data": data
        })

        salvar_contas(contas)
        atualizar_tabela()

        messagebox.showinfo("Sucesso", f"{tipo} registrada com sucesso!", parent=janela)
        janela.destroy()

    tk.Button(frame, text="CONFIRMAR MOVIMENTAÇÃO", command=concluir, width=27, height=2, bg="#0CA120", fg="white").pack(pady=20)
    tk.Button(frame, text="CANCELAR", command=janela.destroy, width=27, height=2).pack()
#======================#
#   EXCLUIR PRODUTO    #
#======================#


def excluir_produto():
    selecionado = tabela.selection()

    # VERIFICA SE ALGUM PRODUTO FOI SELECIONADO
    if not selecionado:
        messagebox.showwarning(
            "Atenção",
            "Selecione um produto para excluir."
        )
        return

    # PEGA O CÓDIGO DO PRODUTO SELECIONADO
    valores = tabela.item(selecionado[0], "values")
    codigo = int(valores[0])
    descricao = valores[1]

    # CONFIRMAÇÃO DA EXCLUSÃO
    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja realmente excluir o produto:\n\n"
        f"{descricao} (Código: {codigo})?"
    )

    if not confirmar:
        return

    # CARREGA AS CONTAS
    contas = carregar_contas()

    # PEGA OS PRODUTOS DO USUÁRIO LOGADO
    produtos = contas[usuario_logado].get("produtos", [])

    # REMOVE O PRODUTO PELO CÓDIGO
    produtos = [
        p for p in produtos
        if int(p["codigo"]) != codigo
    ]

    contas[usuario_logado]["produtos"] = produtos

    # SALVA NO JSON
    salvar_contas(contas)

    # ATUALIZA A TREEVIEW
    atualizar_tabela()

    messagebox.showinfo(
        "Sucesso",
        "Produto excluído com sucesso!"
    )


#====================#
#   ALTERAR PRODUTO  #
#====================#


def editar_produto(event=None):
    selecionado = tabela.selection()

    if not selecionado:
        return

    codigo = int(tabela.item(selecionado[0], "values")[0])

    produto = next((p for p in carregar_produtos() if int(p["codigo"]) == codigo), None)

    if produto is None:
        return

    janela = tk.Toplevel(root)
    janela.title("Editar Produto")
    janela.geometry("450x500")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")
    janela.transient(root)
    janela.grab_set()

    frame = tk.Frame(janela, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.95, anchor="center")

    tk.Label(frame, text="EDITAR PRODUTO", font=("Helvetica", 20, "bold"), bg="light yellow").pack(pady=15)

    # CÓDIGO
    tk.Label(frame, text="Código:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_codigo = tk.Entry(frame, font=("Arial", 13))
    entry_codigo.pack(fill="x", padx=20, pady=5)
    entry_codigo.insert(0, produto["codigo"])
    entry_codigo.config(state="readonly")

    # DESCRIÇÃO
    tk.Label(frame, text="Descrição:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_descricao = tk.Entry(frame, font=("Arial", 13))
    entry_descricao.pack(fill="x", padx=20, pady=5)
    entry_descricao.insert(0, produto["descricao"])

    # CATEGORIA
    tk.Label(frame, text="Categoria:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_categoria = tk.Entry(frame, font=("Arial", 13))
    entry_categoria.pack(fill="x", padx=20, pady=5)
    entry_categoria.insert(0, produto["categoria"])

    # QUANTIDADE
    tk.Label(frame, text="Quantidade:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_quantidade = tk.Entry(frame, font=("Arial", 13))
    entry_quantidade.pack(fill="x", padx=20, pady=5)
    entry_quantidade.insert(0, produto["quantidade"])

    # VALOR
    tk.Label(frame, text="Valor unitário (R$):", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_valor = tk.Entry(frame, font=("Arial", 13))
    entry_valor.pack(fill="x", padx=20, pady=5)
    entry_valor.insert(0, produto["valor"])

    # SALVAR ALTERAÇÕES
    def salvar():
        descricao = entry_descricao.get().strip()
        categoria = entry_categoria.get().strip()
        quantidade = entry_quantidade.get().strip()
        valor = entry_valor.get().strip()

        if not all([descricao, categoria, quantidade, valor]):
            messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela)
            return

        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe uma quantidade inteira maior ou igual a zero.", parent=janela)
            return

        try:
            valor = float(valor.replace(",", "."))
            if valor < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe um valor válido.", parent=janela)
            return

        contas = carregar_contas()
        produtos = contas[usuario_logado].get("produtos", [])

        atual = next((p for p in produtos if int(p["codigo"]) == codigo), None)

        if atual is None:
            messagebox.showerror("Erro", "Produto não encontrado.", parent=janela)
            return

        atual["descricao"] = descricao
        atual["categoria"] = categoria
        atual["quantidade"] = quantidade
        atual["valor"] = valor

        salvar_contas(contas)
        atualizar_tabela()

        janela.destroy()
        messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")

    tk.Button(frame, text="SALVAR ALTERAÇÕES", command=salvar, width=25, height=2, bg="#0CA120", fg="white").pack(pady=15)
    tk.Button(frame, text="CANCELAR", command=janela.destroy, width=25, height=2).pack()


#==============#
#   FILTRAR    #
#==============#

def filtrar():
    janela = tk.Toplevel(root)
    janela.title("Filtrar Produtos")
    janela.geometry("450x450")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")
    janela.transient(root)
    janela.grab_set()

    frame = tk.Frame(janela, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.95, anchor="center")

    tk.Label(frame, text="FILTRAR PRODUTOS", font=("Helvetica", 20, "bold"), bg="light yellow").pack(pady=15)

    # DESCRIÇÃO
    tk.Label(frame, text="Descrição:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)
    entry_descricao = tk.Entry(frame, font=("Arial", 13))
    entry_descricao.pack(fill="x", padx=20, pady=5)

    # CATEGORIA
    tk.Label(frame, text="Categoria:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)

    produtos = carregar_produtos()
    categorias = sorted(set(p["categoria"] for p in produtos), key=str.lower)

    combo_categoria = ttk.Combobox(frame, values=["Todas"] + categorias, state="readonly", font=("Arial", 12))
    combo_categoria.pack(fill="x", padx=20, pady=5)
    combo_categoria.set("Todas")

    # CÓDIGO
    tk.Label(frame, text="Intervalo de código:", font=("Arial", 12, "bold"), bg="light yellow").pack(anchor="w", padx=20)

    frame_codigo = tk.Frame(frame, bg="light yellow")
    frame_codigo.pack(fill="x", padx=20, pady=5)

    entry_inicio = tk.Entry(frame_codigo, font=("Arial", 13), justify="center")
    entry_inicio.pack(side="left", fill="x", expand=True)

    tk.Label(frame_codigo, text=" até ", bg="light yellow", font=("Arial", 12, "bold")).pack(side="left")

    entry_fim = tk.Entry(frame_codigo, font=("Arial", 13), justify="center")
    entry_fim.pack(side="left", fill="x", expand=True)

    # APLICAR FILTROS
    def aplicar():
        descricao = entry_descricao.get().strip().lower()
        categoria = combo_categoria.get()
        inicio = entry_inicio.get().strip()
        fim = entry_fim.get().strip()

        if bool(inicio) != bool(fim):
            messagebox.showwarning("Atenção", "Preencha os dois códigos.", parent=janela)
            return

        if inicio and fim:
            try:
                inicio = int(inicio)
                fim = int(fim)

                if inicio <= 0 or fim < inicio:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Erro", "Informe um intervalo de códigos válido.", parent=janela)
                return

        tabela.delete(*tabela.get_children())

        for p in carregar_produtos():
            codigo = int(p["codigo"])

            if descricao and descricao not in p["descricao"].lower():
                continue

            if categoria != "Todas" and categoria != p["categoria"]:
                continue

            if inicio and not inicio <= codigo <= fim:
                continue

            tabela.insert("", "end", values=(p["codigo"], p["descricao"], p["categoria"], p["quantidade"], f'R$ {p["valor"]:.2f}'))

        janela.destroy()

    # LIMPAR FILTROS
    def limpar():
        atualizar_tabela()
        janela.destroy()

    tk.Button(frame, text="APLICAR FILTROS", command=aplicar, width=25, height=2, bg="#0CA120", fg="white").pack(pady=15)
    tk.Button(frame, text="LIMPAR FILTROS", command=limpar, width=25, height=2).pack(pady=5)
    tk.Button(frame, text="CANCELAR", command=janela.destroy, width=25, height=2).pack(pady=5)

#=============================#
#       RELATÓRIO             #
#=============================#

def relatorio():
    janela = tk.Toplevel(root)
    janela.title("Relatório de Movimentações")
    janela.geometry("1050x650")
    janela.resizable(False, False)
    janela.configure(bg="#EFF0B8")
    janela.transient(root)
    janela.grab_set()

    frame = tk.Frame(janela, bg="light yellow")
    frame.place(relx=0.5, rely=0.5, relwidth=0.97, relheight=0.96, anchor="center")

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(3, weight=1)

    tk.Label(frame, text="RELATÓRIO DE MOVIMENTAÇÕES", font=("Helvetica", 20, "bold"), bg="light yellow").grid(row=0, column=0, pady=15)

    # PERÍODO
    frame_datas = tk.Frame(frame, bg="light yellow")
    frame_datas.grid(row=1, column=0, pady=10)

    tk.Label(frame_datas, text="Data inicial:", font=("Arial", 12, "bold"), bg="light yellow").pack(side="left", padx=5)

    entry_inicio = tk.Entry(frame_datas, font=("Arial", 12), width=12, justify="center")
    entry_inicio.pack(side="left", padx=5)

    tk.Label(frame_datas, text="Data final:", font=("Arial", 12, "bold"), bg="light yellow").pack(side="left", padx=5)

    entry_fim = tk.Entry(frame_datas, font=("Arial", 12), width=12, justify="center")
    entry_fim.pack(side="left", padx=5)

    # TABELA
    area_tabela = tk.Frame(frame, bg="white")
    area_tabela.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    colunas = ("codigo", "descricao", "tipo", "quantidade", "data")

    tabela_relatorio = ttk.Treeview(area_tabela, columns=colunas, show="headings")

    tabela_relatorio.heading("codigo", text="Código")
    tabela_relatorio.heading("descricao", text="Produto")
    tabela_relatorio.heading("tipo", text="Movimentação")
    tabela_relatorio.heading("quantidade", text="Quantidade")
    tabela_relatorio.heading("data", text="Data")

    tabela_relatorio.column("codigo", width=90, anchor="center")
    tabela_relatorio.column("descricao", width=350, anchor="center")
    tabela_relatorio.column("tipo", width=180, anchor="center")
    tabela_relatorio.column("quantidade", width=150, anchor="center")
    tabela_relatorio.column("data", width=150, anchor="center")

    tabela_relatorio.tag_configure("entrada", foreground="green")
    tabela_relatorio.tag_configure("saida", foreground="red")

    scrollbar = ttk.Scrollbar(area_tabela, orient="vertical", command=tabela_relatorio.yview)
    tabela_relatorio.configure(yscrollcommand=scrollbar.set)

    tabela_relatorio.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # RESUMO
    frame_resumo = tk.Frame(frame, bg="light yellow")
    frame_resumo.grid(row=4, column=0, pady=10)

    label_entradas = tk.Label(frame_resumo, text="Entradas: 0 unidades", font=("Arial", 12, "bold"), fg="green", bg="light yellow")
    label_entradas.pack(side="left", padx=25)

    label_saidas = tk.Label(frame_resumo, text="Saídas: 0 unidades", font=("Arial", 12, "bold"), fg="red", bg="light yellow")
    label_saidas.pack(side="left", padx=25)

    # APLICAR FILTRO
    def aplicar_filtro():
        inicio = entry_inicio.get().strip()
        fim = entry_fim.get().strip()

        if not inicio or not fim:
            messagebox.showwarning("Atenção", "Informe as duas datas.", parent=janela)
            return

        try:
            inicio = datetime.strptime(inicio, "%d/%m/%Y").date()
            fim = datetime.strptime(fim, "%d/%m/%Y").date()

            if fim < inicio:
                raise ValueError

        except ValueError:
            messagebox.showerror("Erro", "Informe um período válido no formato dd/mm/aaaa.", parent=janela)
            return

        tabela_relatorio.delete(*tabela_relatorio.get_children())

        contas = carregar_contas()
        historico = contas[usuario_logado].get("movimentacoes", [])

        total_entradas = 0
        total_saidas = 0

        movimentacoes_filtradas = []

        for m in historico:
            try:
                data = datetime.strptime(m["data"], "%d/%m/%Y").date()
            except (ValueError, KeyError):
                continue

            if inicio <= data <= fim:
                movimentacoes_filtradas.append((data, m))

        movimentacoes_filtradas.sort(key=lambda item: item[0])

        for data, m in movimentacoes_filtradas:
            tipo = m["tipo"]
            quantidade = int(m["quantidade"])

            if tipo == "Entrada":
                total_entradas += quantidade
                tag = "entrada"
            elif tipo == "Saída":
                total_saidas += quantidade
                tag = "saida"
            else:
                continue

            tabela_relatorio.insert(
                "",
                "end",
                values=(
                    m["codigo"],
                    m["descricao"],
                    tipo,
                    quantidade,
                    data.strftime("%d/%m/%Y")
                ),
                tags=(tag,)
            )

        label_entradas.config(text=f"Entradas: {total_entradas} unidades")
        label_saidas.config(text=f"Saídas: {total_saidas} unidades")

        if not movimentacoes_filtradas:
            messagebox.showinfo("Relatório", "Nenhuma movimentação encontrada nesse período.", parent=janela)

    # LIMPAR
    def limpar():
        entry_inicio.delete(0, "end")
        entry_fim.delete(0, "end")
        tabela_relatorio.delete(*tabela_relatorio.get_children())
        label_entradas.config(text="Entradas: 0 unidades")
        label_saidas.config(text="Saídas: 0 unidades")

    # BOTÕES
    frame_botoes = tk.Frame(frame, bg="light yellow")
    frame_botoes.grid(row=2, column=0, pady=5)

    tk.Button(frame_botoes, text="GERAR RELATÓRIO", command=aplicar_filtro, width=20, height=2, bg="#0CA120", fg="white").pack(side="left", padx=5)

    tk.Button(frame_botoes, text="LIMPAR", command=limpar, width=15, height=2).pack(side="left", padx=5)

    tk.Button(frame_botoes, text="FECHAR", command=janela.destroy, width=15, height=2).pack(side="left", padx=5)

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

    tk.Button(barra_botoes, text="Movimentação", command=movimentacao, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Excluir", command=excluir_produto, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Filtrar", command=filtrar, width=15, height=2).pack(side="left", padx=5)

    tk.Button(barra_botoes, text="Relatório", command=relatorio, width=15, height=2, bg="#2471A3", fg="white").pack(side="left", padx=5)

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

    # EDITAR PRODUTO COM DOIS CLIQUES
    tabela.bind("<Double-1>", editar_produto)

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
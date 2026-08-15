import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

#pip install Pillow -> No terminal
from PIL import Image, ImageTk

cor0 = "#FFFFFF" #White/Branco
cor1 = "#333333" #Black/Preto
cor2 = "#fcc058" #Orange/laranja
cor3 = "#fff873" #Yellow/Amarelo
cor4 = "#34eb3d" #Green/Verde
cor5 = "#e85151" #Red/Vermelho
fundo = "#3b3b3b" #Background/Fundo

#Cria a janela principal
janela = tk.Tk()
janela.title("Pedra, Papel, Tesoura")
janela.geometry("260x295")
janela.configure(bg=fundo)

#Cria os frames(quadrado preto e branco) que vão conter os elementos da interface
frame_cima = tk.Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=tk.NW)
frame_baixo = tk.Frame(janela, width=260, height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=tk.NW)

#Jogadores
app_pessoa = tk.Label(frame_cima, text="Jogador", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)
#Barra marcou pontos
app_pessoa_linha = tk.Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)
#Pontuação
app_pessoa_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)

#Separação da pontuação
app_vs = tk.Label(frame_cima, text=":", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)

#Computador
app_pc = tk.Label(frame_cima, text="PC", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc.place(x=200, y=70)
#Barra marcou pontos
app_pc_linha = tk.Label(frame_cima, text="", height=10, anchor="center", bg=cor5, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)
#Pontuação
app_pc_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=180, y=20)

#Barra de empate
app_empate = tk.Label(frame_cima, text="", width=225, anchor="center", bg=cor2, fg=cor0, font=("Ivy 10 bold"))
app_empate.place(x=0, y=95)

#Mostrar jogada PC
app_jogada_pc = tk.Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pc.place(x=190, y=10)

#Mostrar jogada player
app_jogada_pessoa = tk.Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pessoa.place(x=10, y=10)

app_vencedor = tk.Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_vencedor.place(x=5, y=60)

global escolha_pessoa
global escolha_pc
global pontos_pessoa
global pontos_pc
global rodadas
pontos_pessoa = 0
pontos_pc = 0
rodadas = 5

def end_game():
    pass

def teste_empate(escolha_pessoa, escolha_pc):
    return escolha_pessoa == escolha_pc

def teste_vitoria_pessoa(escolha_pessoa, escolha_pc):
    if (escolha_pessoa == "pedra" and escolha_pc == "tesoura") or (escolha_pessoa == "papel" and escolha_pc == "pedra") or (escolha_pessoa == "tesoura" and escolha_pc == "papel"):
        return True
    return False

def teste_vitoria_pc(escolha_pessoa, escolha_pc):
    if (escolha_pc == "pedra" and escolha_pessoa == "tesoura") or (escolha_pc == "papel" and escolha_pessoa == "pedra") or (escolha_pc == "tesoura" and escolha_pessoa == "papel"):
        return True
    return False


def move(movement):
    global pontos_pessoa
    global pontos_pc
    global rodadas

    opcoes = ["pedra", "papel", "tesoura"]

    app_pessoa_linha["bg"] = cor1
    app_pc_linha["bg"] = cor1
    app_empate["bg"] = cor1

    if rodadas > 0:
        print(rodadas)
        escolha_pc = random.choice(opcoes)
        app_jogada_pc["text"] = escolha_pc

        escolha_pessoa = movement
        app_jogada_pessoa["text"] = escolha_pessoa

    #Caso empate
    if teste_empate(escolha_pessoa, escolha_pc):
        app_empate["bg"] = cor3
    elif teste_vitoria_pessoa(escolha_pessoa, escolha_pc):
        pontos_pessoa += 10
        app_pessoa_linha["bg"] = cor4
        app_pc_linha["bg"] = cor5
    elif teste_vitoria_pc(escolha_pessoa, escolha_pc):
        pontos_pc += 10
        app_pc_linha["bg"] = cor4
        app_pessoa_linha["bg"] = cor5
    else:
        end_game() 

def start():
    global icon_papel
    global icon_pedra
    global icon_tesoura
    global btn_papel
    global btn_pedra
    global btn_tesoura

    #Configuração do frame de baixo
    icon_pedra = Image.open("./images/pedra.png")
    icon_pedra = icon_pedra.resize((50, 50), Image.Resampling.LANCZOS)
    icon_pedra = ImageTk.PhotoImage(icon_pedra)
    btn_pedra = tk.Button(frame_baixo, command=lambda: move("pedra"), width=50, height=50, image=icon_pedra, bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
    btn_pedra.place(x=15, y=60)

    icon_tesoura = Image.open("./images/tesoura.png")
    icon_tesoura = icon_tesoura.resize((50, 50), Image.Resampling.LANCZOS)
    icon_tesoura = ImageTk.PhotoImage(icon_tesoura)
    btn_tesoura = tk.Button(frame_baixo, command=lambda: move("tesoura"), width=50, height=50, image=icon_tesoura, bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
    btn_tesoura.place(x=100, y=60)

    icon_papel = Image.open("./images/papel.png")
    icon_papel = icon_papel.resize((50, 50), Image.Resampling.LANCZOS)
    icon_papel = ImageTk.PhotoImage(icon_papel)
    btn_papel = tk.Button(frame_baixo, command=lambda: move("papel"), width=50, height=50, image=icon_papel, bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
    btn_papel.place(x=185, y=60)

button_play = tk.Button(frame_baixo, text="Play", command=start, width=25, height=1, bg=cor1, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
button_play.place(x=20, y=120)

btn_quit = tk.Button(frame_baixo, text="Sair", command=quit, width=20, height=1, bg=cor1, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_quit.place(x=40, y=155)

janela.mainloop()
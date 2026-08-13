import tkinter as tk
from tkinter import NW, Label, ttk
from tkinter import messagebox

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
janela.geometry("260x280")
janela.configure(bg=fundo)

#Cria os frames(quadrado preto e branco) que vão conter os elementos da interface
frame_cima = tk.Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = tk.Frame(janela, width=260, height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#Jogadores
app_pessoa = Label(frame_cima, text="Jogador", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)
#Barra marcou pontos
app_pessoa_linha = Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)
#Pontuação
app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)

#Separação da pontuação
app_vs = Label(frame_cima, text=":", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)

#Computador
app_pc = Label(frame_cima, text="PC", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc.place(x=200, y=70)
#Barra marcou pontos
app_pc_linha = Label(frame_cima, text="", height=10, anchor="center", bg=cor5, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)
#Pontuação
app_pc_pontos = Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=180, y=20)

#Barra de empate
app_empate = Label(frame_cima, text="", width=225, anchor="center", bg=cor2, fg=cor0, font=("Ivy 10 bold"))
app_empate.place(x=0, y=95)

janela.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
janela.geometry("260x280")
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

#Configuração do frame de baixo
icon_pedra = Image.open("./images/pedra.png")
icon_pedra = icon_pedra.resize((50, 50), Image.Resampling.LANCZOS)
icon_pedra = ImageTk.PhotoImage(icon_pedra)
btn_pedra = tk.Button(frame_baixo, width=50, height=50, image=icon_pedra, bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_pedra.place(x=15, y=60)

icon_tesoura = Image.open("./images/tesoura.png")
icon_tesoura = icon_tesoura.resize((50, 50), Image.Resampling.LANCZOS)
icon_tesoura = ImageTk.PhotoImage(icon_tesoura)
btn_tesoura = tk.Button(frame_baixo, width=50, height=50, image=icon_tesoura, bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_tesoura.place(x=100, y=60)

icon_papel = Image.open("./images/papel.png")
icon_papel = icon_papel.resize((50, 50), Image.Resampling.LANCZOS)
icon_papel = ImageTk.PhotoImage(icon_papel)
btn_papel = tk.Button(frame_baixo, width=50, height=50, image=icon_papel, bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_papel.place(x=185, y=60)

button_play = tk.Button(frame_baixo, text="Play", width=30, height=1, bg=cor1, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat"
)
button_play.place(x=5, y=140)

janela.mainloop()
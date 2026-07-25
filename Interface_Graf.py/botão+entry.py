import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x400")

def button_command():                               #Função que define o comando do botão
    nome = entry.get()
    messagebox.showinfo("Nome Completo", nome)

label = tk.Label(root, text="Digite seu nome completo: ")           #É o que estará escrito dentro da janela
entry = tk.Entry(root)                                              #Define o entry
button = tk.Button(root, text="Mostrar", command=button_command)    #Cria o botão

label.pack()
entry.pack()
button.pack()

root.mainloop()
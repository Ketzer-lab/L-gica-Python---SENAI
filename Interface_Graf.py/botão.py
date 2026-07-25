import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def button_command1():              #Decide o titulo e as palavras dentro da janela criada pelo botão
    messagebox.showinfo(
        "Informação",
        "Você clicou no botão!"
    )

def button_command2():
    messagebox.showinfo(
        "Informação",
        "Você acabou de clicar no botão número 2!"
    )

button1 = tk.Button(            #Cria o botão
    root,
    text="    I     ",
    command=button_command1
    )

button2 =tk.Button(
    root,
    text="    II    ",
    command=button_command2
)

button1.pack()                  #Coloca o botão na janela
button2.pack()

root.mainloop()
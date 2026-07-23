import tkinter as tk

root = tk.Tk()  #Cria a janela principal

message = tk.Label(root, text="Hello, World!")  #Cria um rótulo como o texto "Hello, World!"

message.pack()  #Posicionao rótulo na janela

root.mainloop()     #Inicia o loop principal da interface grádica

# Aqui não funciona por causa de alguma configuração da máquina
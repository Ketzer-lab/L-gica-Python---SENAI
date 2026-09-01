import tkinter as tk

root = tk.Tk()  #Cria a janela principal
root.title("SENAI - Desenvolvimento de Sistemas")   #O título da janela

root.geometry("600x400+100+100")    #Dita o tamanho da janela

message = tk.Label(root, text="Hello, World!")  #Cria um rótulo como o texto "Hello, World!"

message.pack()  #Posicionao rótulo na janela

root.mainloop()     #Inicia o loop principal da interface grádica
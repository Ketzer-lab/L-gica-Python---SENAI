import tkinter as tk

root = tk.Tk()

root.geometry("400x300")

root.resizable(False, False)    #Impede que a janela seja ampliada manualmente com o cursor

root.minsize(300, 200)          #Tamanho minimo da janela
root.maxsize(800, 600)          #Tamanho maximo da janela

root.attributes('-alpha', 0.5)  #Define a opacidade da janela

root.mainloop()
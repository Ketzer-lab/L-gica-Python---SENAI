from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="light green")

canvas.create_polygon(200, 60, 250, 140, 150, 140, fill= "light blue", outline="black")
canvas.create_rectangle(240, 140, 160, 220, fill= "pink", outline="black")
canvas.create_rectangle(210, 180, 190, 220, fill= "brown", outline="black")
canvas.create_rectangle(210, 130, 190, 110, fill= "yellow", outline="black")

canvas.pack()
janela.mainloop()
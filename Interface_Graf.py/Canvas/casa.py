from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="light green")

canvas.create_polygon(200, 60, 250, 140, 150, 140, fill= "light blue", outline="black")
canvas.create_rectangle(240, 140, 160, 220, fill= "pink", outline="black")
canvas.create_rectangle(210, 180, 190, 220, fill= "brown", outline="black")
canvas.create_rectangle(210, 130, 190, 110, fill= "yellow", outline="black")
canvas.create_polygon(130, 220, 130, 200, 110, 180, 45, 180, 45, 220, fill="red", outline="black")
canvas.create_oval(45, 210, 75, 240, fill="black")
canvas.create_oval(90, 210, 120, 240, fill="black")
canvas.create_polygon(130, 220, 250, 140, 150, 140, fill= "light blue", outline="black")

canvas.pack()
janela.mainloop()
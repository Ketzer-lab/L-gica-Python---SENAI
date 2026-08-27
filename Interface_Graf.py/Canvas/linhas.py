from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="light green")

canvas.create_line(10, 10, 10, 200, fill="red")
canvas.create_line(10, 10, 200, 200, fill="black")
canvas.create_line(10, 10, 200, 10, fill="blue")

canvas.pack()
janela.mainloop()
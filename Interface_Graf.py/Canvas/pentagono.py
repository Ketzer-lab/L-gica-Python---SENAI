from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="light green")

canvas.create_polygon(
    10, 100,
    60, 50,
    110, 100,
    85, 150,
    35, 150,
    fill= "light blue",
    outline="black"
)


canvas.pack()
janela.mainloop()
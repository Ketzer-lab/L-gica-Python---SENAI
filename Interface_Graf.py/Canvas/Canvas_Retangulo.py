from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="light green")

canvas.create_rectangle(
    80, 70, 300, 250,
    fill='light blue',
    outline='black'
)

canvas.pack()
janela.mainloop()
from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=500, height=400, bg="white")

# Resistor
canvas.create_rectangle(
    60, 190, 420, 250,
    fill='light yellow',
    outline='black'
)

# Banda 1
canvas.create_rectangle(
    130, 190, 160, 250,
    fill='black',
    outline='black'
)

# Banda 2
canvas.create_rectangle(
    190, 190, 220, 250,
    fill='black',
    outline='black'
)

# Multiplicador
canvas.create_rectangle(
    250, 190, 280, 250,
    fill='black',
    outline='black'
)


# Tolerância
canvas.create_rectangle(
    330, 190, 360, 250,
    fill='black',
    outline='black'
)

canvas.pack()
janela.mainloop()
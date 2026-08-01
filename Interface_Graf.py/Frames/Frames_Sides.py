import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="black")

frame = tk.Frame(root, width=420, height=220)
frame.pack(padx=10, pady=10)

a_frame = tk.Frame(frame, width=190, height=190, bg="red")
a_frame.pack(side="top", padx=10, pady=10)

b_frame = tk.Frame(frame, width=190, height=190, bg="yellow")
b_frame.pack(padx=10, pady=10)

c_frame = tk.Frame(frame, width=190, height=190, bg="green")
c_frame.pack(side="bottom", padx=10, pady=10)

root.mainloop()
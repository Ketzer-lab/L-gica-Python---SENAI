import tkinter as tk

root = tk.Tk(); root.title("SENAI - Desenvolvimento de Sistemas"); root.config(bg="white"); root.geometry("300x400")

label_login = tk.Label(root, text="Faça seu login", bg="white"); label_login.pack(ipady=5, fill="x")

imagem = tk.PhotoImage(file="profile.png").subsample(3, 3)
label_imagem = tk.Label(root, image=imagem, bg="white"); label_imagem.image = imagem; label_imagem.pack()

label_usuario = tk.Label(root, text="Usuário:", bg="white"); label_usuario.pack(anchor="w")
entry_usuario = tk.Entry(root); entry_usuario.pack()

label_senha = tk.Label(root, text="Senha:", bg="white"); label_senha.pack(anchor="w")
entry_senha = tk.Entry(root); entry_senha.pack()

botao = tk.Button(
    root,
    text="      Entrar      ",
    background="light cyan"
)
botao.pack()

caixinha = tk.Checkbutton(
    root,
    text="Lembrar-me",
    bg="white"
    )
caixinha.pack(side="left")

esqueceu = tk.Label(root, text="Esqueceu sua senha?", bg="white"); esqueceu.pack(side="right")

root.mainloop()
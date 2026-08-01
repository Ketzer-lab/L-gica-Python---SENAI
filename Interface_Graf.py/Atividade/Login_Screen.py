import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="white")
root.geometry("400x600")

label_login = tk.Label(root, text="Faça seu login")
label_login.pack()

imagem = tk.PhotoImage(file="profile.png")
label_imagem = tk.Label(root, image=imagem)
label_imagem.image = imagem
label_imagem.pack()

label_usuario = tk.Label(root, text="Usuário:")
label_usuario.pack(anchor="w")
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack(anchor="w")
entry_senha = tk.Entry(root)
entry_senha.pack()

botao = tk.Button(
    root,
    text="      Entrar      "
)
botao.pack()

caixinha = tk.Checkbutton(
    root,
    text="Lembrar-me"
    )
caixinha.pack(side="left")

esqueceu = tk.Label(root, text="Esqueceu sua senha?")
esqueceu.pack(side="right")

root.mainloop()
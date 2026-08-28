import tkinter as tk

# Canvas em estilo pixel-art/isométrico inspirado na imagem enviada.
# Não usa nenhuma imagem externa: tudo é desenhado com polígonos e retângulos.

LARGURA = 500
ALTURA = 650

janela = tk.Tk()
janela.title("Personagem em Pixel Art - Canvas")
janela.resizable(False, False)

canvas = tk.Canvas(
    janela,
    width=LARGURA,
    height=ALTURA,
    bg="white",
    highlightthickness=0
)
canvas.pack()

# ------------------------------------------------------------------
# Funções auxiliares
# ------------------------------------------------------------------

def poligono(pontos, cor):
    canvas.create_polygon(pontos, fill=cor, outline=cor)

def retangulo(x1, y1, x2, y2, cor):
    canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline=cor)

# ------------------------------------------------------------------
# Personagem
# ------------------------------------------------------------------
# A figura é formada por blocos com pequenas diferenças de tom para
# dar a aparência 3D da referência.

# =========================
# CABEÇA / CABELO
# =========================

# Parte superior do cabelo/cabeça
poligono([
    (175, 75), (275, 45), (375, 105),
    (375, 205), (325, 235), (175, 195)
], "#4b2d18")

# Topo do cabelo
poligono([
    (175, 75), (275, 45), (375, 105),
    (275, 135), (175, 105)
], "#3b2514")

# Lado direito do cabelo
poligono([
    (275, 135), (375, 105), (375, 205),
    (325, 235), (275, 210)
], "#241a14")

# Rosto
poligono([
    (175, 105), (275, 135), (275, 210),
    (225, 235), (125, 175), (125, 105)
], "#a86f4d")

# Sombra lateral do rosto
poligono([
    (225, 135), (275, 135), (275, 210),
    (225, 235)
], "#8b563b")

# Franja/cabelo
poligono([
    (175, 75), (275, 45), (275, 115),
    (225, 135), (175, 120)
], "#3d2817")

# Cabelo lateral esquerdo
retangulo(125, 105, 160, 160, "#4a2c18")
retangulo(160, 85, 190, 125, "#4a2c18")

# Olho esquerdo
retangulo(145, 132, 160, 147, "#d9d9d9")
retangulo(160, 137, 172, 151, "#3a67a5")

# Olho direito
retangulo(210, 145, 225, 160, "#d9d9d9")
retangulo(225, 150, 237, 164, "#3a67a5")

# Nariz
retangulo(190, 157, 204, 177, "#8e5a3e")

# Boca
retangulo(175, 183, 225, 195, "#6e3e2d")
retangulo(185, 183, 215, 188, "#c58a68")

# =========================
# PESCOÇO
# =========================
retangulo(190, 220, 245, 255, "#8b563b")

# =========================
# CAMISETA TURQUESA
# =========================

# Tronco
poligono([
    (165, 235), (245, 255), (325, 225),
    (350, 385), (285, 420), (160, 380)
], "#11a9a4")

# Frente da camiseta
poligono([
    (165, 235), (245, 255), (245, 405),
    (160, 380)
], "#0c9b98")

# Lado direito da camiseta
poligono([
    (245, 255), (325, 225), (350, 385),
    (285, 420), (245, 405)
], "#08aaa8")

# Gola
poligono([
    (190, 238), (245, 255), (270, 245),
    (245, 275), (205, 265)
], "#087f7d")

# =========================
# BRAÇO ESQUERDO
# =========================

# Manga
poligono([
    (165, 235), (125, 245), (105, 305),
    (145, 325), (180, 290)
], "#0da29e")

# Braço
poligono([
    (105, 300), (145, 320), (145, 475),
    (95, 455), (85, 340)
], "#9b6245")

# Sombra do braço esquerdo
poligono([
    (125, 315), (145, 320), (145, 475),
    (120, 465)
], "#7e4d38")

# =========================
# BRAÇO DIREITO
# =========================

# Manga direita
poligono([
    (300, 235), (350, 220), (395, 270),
    (365, 320), (320, 295)
], "#0fa6a3")

# Braço direito
poligono([
    (365, 300), (405, 275), (430, 425),
    (390, 470), (350, 430)
], "#9b6245")

# Sombra
poligono([
    (405, 275), (430, 425), (390, 470),
    (380, 330)
], "#7c4c37")

# =========================
# CALÇA
# =========================

# Perna esquerda
poligono([
    (160, 375), (225, 395), (225, 565),
    (150, 565), (150, 430)
], "#33227e")

# Perna direita
poligono([
    (225, 395), (285, 405), (300, 565),
    (225, 565)
], "#21165d")

# Detalhe da cintura
poligono([
    (160, 375), (225, 395), (285, 405),
    (275, 430), (220, 420), (160, 405)
], "#241968")

# =========================
# SAPATOS
# =========================

poligono([
    (150, 550), (225, 550), (225, 580),
    (145, 580), (135, 570)
], "#303030")

poligono([
    (225, 550), (300, 550), (310, 580),
    (225, 580)
], "#202020")

# Pequenos detalhes para reforçar o visual pixelado
retangulo(130, 330, 145, 390, "#a96d4e")
retangulo(360, 340, 375, 400, "#a96d4e")

janela.mainloop()
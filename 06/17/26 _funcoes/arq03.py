altura = int(input("Altura do quadrilátero: "))
largura = int(input("Largura do quadrilátero: "))

print(f'+{largura*'-'}+')

for _ in range(altura):
    print(f'|{largura*" "}|')

print(f'+{largura*'-'}+')
from Conversoes import celsius_fahrenheit, metros_quilometros

def main() -> None:
    # Exemplos de uso
    C = 25
    m = 1500
    print(f"{C} °C = {celsius_fahrenheit(C): .2f} °F")
    print(f"{m} m = {metros_quilometros(m): .3f} Km")

# Ponto de entrada do programa
# Só executa main() se este arquivo for o script principal
if __name__ == "__main__":
    main()

print("")

import Conversoes

def main() -> None:
    # Exemplos de uso
    C = 25
    m = 1500
    print(f"{C} °C = {Conversoes.celsius_fahrenheit(C): .2f} °F")
    print(f"{m} m = {Conversoes.metros_quilometros(m): .3f} Km")

# Ponto de entrada do programa
# Só executa main() se este arquivo for o script principal
if __name__ == "__main__":
    main()
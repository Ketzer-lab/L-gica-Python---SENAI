senha = input("Digite uma senha: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in senha:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if not ch.isalnum():
        has_special = True

errors = []
if len(senha) < 8:
    errors.append("Minimo 8 caracteres.")
if not has_upper:
    errors.append("Pelo monos uma letra maiuscula")
if not has_lower:
    errors.append("Pelo monos uma letra minuscula")
if not has_digit:
    errors.append("Pelo menos um numero>")


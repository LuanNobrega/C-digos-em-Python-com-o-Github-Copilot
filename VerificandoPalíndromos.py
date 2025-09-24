# Solicita uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e transforma em minúsculas (para evitar diferenças de maiúsculas/minúsculas)
palavra_formatada = palavra.replace(" ", "").lower()

# Inverte a string
invertida = palavra_formatada[::-1]

# Verifica se é palíndromo
if palavra_formatada == invertida:
    print(f"A palavra '{palavra}' é um PALÍNDROMO!")
else:
    print(f"A palavra '{palavra}' NÃO é um palíndromo.")
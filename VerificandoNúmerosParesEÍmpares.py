# Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se é par ou ímpar usando o operador módulo
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
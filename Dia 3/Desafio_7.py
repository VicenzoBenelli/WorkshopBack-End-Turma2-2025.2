#Codigo incorreto:
'''def validar_idade(idade)
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))'''''


# 1) Valores fora do intervalo 0-120 ou entradas não numéricas causam ValueError com mensagens de erro específicas.

# 2) Codigo Corrigido
def valida_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")
    return f"Idade válida: {idade}"

while True:
    try:
        idade = int(input("Digite sua idade: "))
        resultado = valida_idade(idade)
        print(resultado)
        break
    except ValueError as e:
        print(f"Erro: {e}")
        print("Por favor, tente novamente.\n")
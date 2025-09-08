# Codigo Incorreto:
'''dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")'''''

# 1) Chaves inexistentes no dicionário (como "endereco" ou "telefone") causam KeyError, enquanto chaves existentes ("nome", "idade", "cidade") funcionam corretamente.

# 2) Codigo Corrigido:
dados = {
    "nome": "Isaac",  
    "idade": 25,  
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

try:
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    print(f"Erro: A chave '{chave}' não existe no dicionário.")

valor = dados.get(chave, "Chave não encontrada")
print(f"Usando get(): O valor da chave '{chave}' é: {valor}")
#Codigo incorreto: 
''''numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])'''

# 1) Valores de input não apresentam problemas até o numero 2

# 2) Codigo corrigido:

numeros = [10, 20, 30]

while True:
 try:
    indice = int(input("Digite um índice para acessar a lista: ")) 
    print(numeros[indice])
    break
 except IndexError:
   print(f"Digite um valor entre 0 e {len(numeros) - 1}")

# 3) try-except utlizado dentro de um looping que força o usuario a digitar um numero dentro range array






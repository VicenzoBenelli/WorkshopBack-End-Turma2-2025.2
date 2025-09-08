#Codigo incorreto: 
'''def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")'''

# 1) Problemas identificados: ValueError, ZeroDvisionError


# 2) Codigo corrigido:

def dividir(a, b):
     return a / b
    
while True:

 try:
  num1 = input("Digite o primeiro número: ")
  num2 = input("Digite o segundo número: ")

  resultado = dividir(int(num1), int(num2))
  print(f"Resultado: {resultado}")
  break

 except ZeroDivisionError:
    print("Erro: Não é possivel dividir por 0 !")
 
 except ValueError:
   try:
    a_float = float(num1)
    b_float = float(num2)
   
    resultado = a_float / b_float

    print(f"Resultado: {resultado:.2f}")
    break
   
   except ValueError:
     print("Digite valores numericos !")


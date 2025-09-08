#Codigo incorreto: 
'''def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)'''

# 1) erro: TypeError: unsupported operand type(s) for +: 'int' and 'str', causado devido a manipulação e soma de strings de diferentes tipos 
# 2) Codigo corrigido:

def somar(a, b):
    try:
     return a + b
    
    except TypeError:
       
       a_int = int(a)
       b_int = int(b)

       return a_int + b_int
       

resultado = somar(10, "5")
print(resultado)

# 3) try-except utilizado para desviar o fluxo e transformar as variaveis em tipos semelhantes 
# # CONSTANTE

# def calculadora_v1(num1, num2, operador):

#     match (operador):
#         case "1":
#             print(f"Resultado da adição: {num1+num2}")
#         case "2":
#             print(f"Resultado da subtração: {num1-num2}")
#         case "3":
#             print(f"Resultado da multiplicação: {num1*num2}")
#         case "4":
#             if num2!=0:
#                 print(f"Resultado da divisão: {num1/num2}")
#             else:
#                 print("Dividiu por zero? Errou feio!")
#         case _ :
#             print(f"Informe um número de operador válido.")

# calculinho = calculadora_v1(333, 555, operador = "1") # a constante pode ser aqui ou na criação da função

# # VARIÁVEL

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# operador = input("Informe a operação desejada: 1 - adição, 2 - subtração, 3 - multiplicação, 4 - divisão: ")

# def calculadora_v1():

#     match (operador):
#         case "1":
#             print(f"Resultado da adição: {num1+num2}")
#         case "2":
#             print(f"Resultado da subtração: {num1-num2}")
#         case "3":
#             print(f"Resultado da multiplicação: {num1*num2}")
#         case "4":
#             if num2!=0:
#                 print(f"Resultado da divisão: {num1/num2}")
#             else:
#                 print("Dividiu por zero? Errou feio!")
#         case _ :
#             print(f"Informe um número de operador válido.")

# calculadora_v1()

# RETURN

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operador = input("Informe a operação desejada: 1 - adição, 2 - subtração, 3 - multiplicação, 4 - divisão: ")

def calculadora_v1():

    match (operador):
        case "1":
            resultado = num1+num2
        case "2":
            resultado = num1-num2
        case "3":
            resultado = num1*num2
        case "4":
            if num2!=0:
                resultado = num1/num2
            else:
                resultado = "Dividiu por zero? Errou feio!"
        case _ :
            resultado = "Informe um número de operador válido."

    return resultado

print(calculadora_v1)
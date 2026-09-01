# _____________________________________________________
# VEARIÁVEIS E TIPOS DE DADOS
# _____________________________________________________


nome = "Maria"
idade = 30
preco = 19.99
esta_matriculada = True
notas = [8.0, 7.5]  
aluno = ("Maria", 30)   
disciplinas = {"Python", "Lógica"}  
cadastro = {"nome": "Maria", "idade": 30}   


print(type(nome))
print(type(idade))
print(type(preco))
print(type(esta_matriculada))


nota_1 = 2
nota_2 = 4

media = (nota_1 + nota_2) / 2

print("===== RESULTADO =====")

print(f"Primeira nota: {nota_1:.1f}")
print(f"Segunda nota: {nota_2:.1f}")
print(f"Media: {media:.1f}")
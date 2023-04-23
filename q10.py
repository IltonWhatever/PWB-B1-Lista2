# 10- Escreva um programa em Python que leia uma lista de números e imprima apenas os números pares da lista
lista = []
tam = int(input("Digite o tamanho da lista: "))
for n in range(tam):
  lista.append(int(input("Digite o {0}º numero: ".format(n+1))))

print("\nMenor numero da Lista: ",min(lista))
print("Maior numero da Lista: ",max(lista))

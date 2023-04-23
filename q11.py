# 11- Escreva um programa em Python que leia uma lista de números e imprima apenas os números ímpares da lista.
def pares(lista):
  for n in range(len(lista)):
    if lista[n] %2 == 0:
      print(lista[n])
lista = []
tam = int(input("Digite o tamanho da lista: "))
for n in range(tam):
  lista.append(int(input("Digite o {0}º numero: ".format(n+1))))

pares(lista)

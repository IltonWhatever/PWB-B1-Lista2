# 12- Escreva um programa em Python que leia uma lista de números e imprima a soma dos números.
def soma(lista):
  aux = 0
  for n in range(len(lista)):
    aux += lista[n]
  return aux

lista = []
tam = int(input("Digite o tamanho da lista: "))
for n in range(tam):
  lista.append(int(input("Digite o {0}º numero: ".format(n+1))))

soma(lista)

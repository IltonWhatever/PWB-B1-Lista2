# 9- Escreva um programa em Python que leia uma lista de números e imprima a média dos números.
def mediaLista(lista):
  aux = 0
  for n in range(len(lista)):
    aux += lista[n]
  return aux/len(lista)

lista = []
tam = int(input("Digite o tamanho da lista: "))
for n in range(tam):
  lista.append(int(input("Digite o {0}º numero: ".format(n+1))))

mediaLista(lista)

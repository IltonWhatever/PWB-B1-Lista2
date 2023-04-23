# 13- Escreva um programa em Python que leia uma lista de números e imprima a lista em ordem crescente.
lista = []
tam = int(input("Digite o tamanho da lista: "))
for n in range(tam):
  lista.append(int(input("Digite o {0}º numero: ".format(n+1))))
print("Lista ordenada:",sorted(lista))

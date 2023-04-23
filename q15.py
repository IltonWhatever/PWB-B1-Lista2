# 15- Escreva um programa em Python que leia uma lista de números e um número x e imprima se o número x está na lista.
lista = []
tam = int(input("Digite o tamanho da lista: "))
for n in range(tam):
  lista.append(int(input("Digite o {0}º numero: ".format(n+1))))
alvo = int(input("Digite o numero para ser procurado na lista: "))

for n in range(len(lista)):
  if alvo == lista[n]:
    print(f"Numero {alvo} encontrado na lista, sua posição é a {n+1}°")

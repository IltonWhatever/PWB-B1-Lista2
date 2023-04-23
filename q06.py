# 6- Escreva um programa em Python que leia um número inteiro e imprima a tabuada desse número (de 1 a 10).
numero = int(input("Digite um numero: "))
for n in range(1,11):
  print(f"{numero} x {n} = {numero*n}")

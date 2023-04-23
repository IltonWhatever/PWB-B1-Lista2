# 7- Escreva um programa em Python que leia um número inteiro e imprima a sequência de Fibonacci até esse número.
# Interativo
numero = int(input("Digite um numero: "))
aNum = 0 # Numero Anterior
dNum = 1 # Numero Posterior
find = 0 # Variavel Auxiliar
for n in range(numero):
  # Casos bases
  if n==0:
    print(0)
  elif n==1:
    print(1)
  else:
    find = aNum + dNum
    aNum = dNum
    dNum = find
    print(find)
    
# Recursivo
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Digite um numero: "))

for val in range(1,n+1):
  print(fib(val))

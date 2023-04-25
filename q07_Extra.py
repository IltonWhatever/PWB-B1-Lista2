# Outra forma de resolver a 7º questão por meio de lista.
def fiboLista(tam):
  fibo = [0,1]
  inicio = 0
  while len(fibo) != tam:
    fibo.append((fibo[inicio]+fibo[inicio+1]))
    inicio += 1
  if tam == 1:
    print(fibo[0])
  elif tam == 2:
    print(fibo[1])
  else:
    print(fibo)

fiboLista(30)

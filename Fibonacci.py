def Fibonacci(position):
  if position <= 1:
    return position
  else:
    return Fibonacci(position-1) + Fibonacci(position-2)

pos = int(input("Qual posição da Sequencia de Fibonacci você quer descobrir? "))

print("O valor correspondente a posição {} é {}!" .format(pos, Fibonacci(pos)))
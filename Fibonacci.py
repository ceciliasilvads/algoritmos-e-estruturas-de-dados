def fibonacci(position):
  if position <= 1:
    return position
  else:
    return fibonacci(position-1) + fibonacci(position-2)

pos = int(input("Qual posição da Sequencia de Fibonacci você quer descobrir? "))

print("O valor correspondente a posição {} é {}!" .format(pos, fibonacci(pos)))
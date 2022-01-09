def Fatorial(number):
    if number == 0:
        return 1
    else:
        return number * Fatorial(number-1)

int_number = int(input("Número que deseja descobrir o fatorial: "))

print(Fatorial(int_number))
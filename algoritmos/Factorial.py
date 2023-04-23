def fatorial(number):
    if number == 0:
        return 1
    else:
        return number * fatorial(number-1)


if __name__ == '__main__':
    int_number = int(input("Número que deseja descobrir o fatorial: "))
    print(fatorial(int_number))
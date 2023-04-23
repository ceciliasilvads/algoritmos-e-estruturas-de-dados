def soma(n, m):
    return n + m

def subtracao(n, m):
    return n - m

def multiplicacao(n , m):
    if (m == 0):
        return "O denominador não pode ser 0"
    else: 
        return n * m

def divisao(n , m):
    return n / m

if __name__ == '__main__':
    print(multiplicacao(soma(3,3),subtracao(20,18)))
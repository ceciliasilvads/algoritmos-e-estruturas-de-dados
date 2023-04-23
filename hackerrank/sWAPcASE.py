def swap_case(s):
    frase = ''
    for i in s:
        if i == i.upper():
            frase += i.lower()
        else:
            frase += i.upper()
    return frase

if __name__ == '__main__':
    s = input('Digite um frase:')
    result = swap_case(s)
    print(result)
def split_and_join(line):
    split = line.split(" ")
    joined = "-".join(split)
    return joined

if __name__ == '__main__':
    line = input("Digite um frase:")
    result = split_and_join(line)
    print(result)
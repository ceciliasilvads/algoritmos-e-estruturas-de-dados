import random

def showQuotes():
    qtd_itens = int(input("Número de frases que deseja: "))
    f = open("RandomQuotes\Quotes.txt")
    quotes = f.read().splitlines()
    size = len(quotes)
    f.close()
    
    for i in range(0, qtd_itens):
	    print('"%s"' %quotes[random.randint(0, size)])

if __name__== "__main__":
  	showQuotes()
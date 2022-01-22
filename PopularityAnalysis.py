def popularityAnalysis(data):
    crescer = True
    reduzir = True

    for i in range(len(data)-1):
        print(i+1)
        if data[i] > data[i+1]:
            crescer = False
        
        if data[i] < data[i+1]:
            reduzir = False

    return crescer or reduzir

if __name__ == '__main__':
    nuns = [1, 2, 3, 4, 5]
    print(popularityAnalysis(nuns))
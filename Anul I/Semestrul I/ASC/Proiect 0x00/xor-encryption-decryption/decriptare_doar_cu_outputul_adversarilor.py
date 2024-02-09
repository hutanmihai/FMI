inputfile = open("outputul_adversarilor", 'rb')

def ParsingFile(file):
    codedText=file.read()
    return codedText
codedText = ParsingFile(inputfile)

# formam o multime de coduri ascii ale caracterelor ce apar in diferite texte literare
inputulnostru = open("text_mare_literatura_romana_custom.txt", 'r')
ptmultime = inputulnostru.read()
lista = [ord(x) for x in ptmultime]
multime = set(lista)
print(multime)

# aceasta este lista cu codurile ascii din outputul echipei adverse in format zecimal
ls = [int(codedText[i]) for i in range(len(codedText))]

for k in range(10,16): # stiind ca lungimea cheii poate fi de la 10 pana in 15 caractere vom rula primul cod cu acest for.
    # in urma rezultatului analizat am observat ca 12 e lungimea cheii si singurul caracter posibil din cheie este t.
    # dupa aceasta observatie modificam k in range (12,13) pentru a ne lua numai variantele pe lungimea cheii 12.

    # aceasta parte ne ajuta la afisarea mai curata a rezultatelor
    print('\n')
    print("##################################################################")
    print('\n')
    print(k)
    print('\n')
    print("##################################################################")
    print('\n')

    for x in range(48, 58): # cifre
        print(chr(x),end=' : ')
        contor = 0
        for y in range(0, len(ls), k): #aici modifcam 0-ul cu cifre de la 0 la lungimeacheii-1 dupa ce aflu lungimea cheii
            caracter = x ^ ls[y]
            if caracter in multime:
                print(chr(caracter), end=' ')
            else:
                contor = 1
                break

        print()
        if contor == 1:
            print(f"{chr(x)} Nu este bun!")
        else:
            print(f"{chr(x)} Este bun!")
        print()

    for x in range(65, 91):
        print(chr(x),end=' : ')
        contor = 0
        for y in range(0, len(ls), k): #aici modifcam 0-ul cu cifre de la 0 la lungimeacheii-1 dupa ce aflu lungimea cheii
            caracter = x ^ ls[y]
            if caracter in multime:
                print(chr(caracter), end=' ')
            else:
                contor = 1
                break

        print()
        if contor == 1:
            print(f"{chr(x)} Nu este bun!")
        else:
            print(f"{chr(x)} Este bun!")
        print()

    for x in range(97, 123):
        print(chr(x),end=' : ')
        contor = 0
        for y in range(0, len(ls), k): #aici modifcam 0-ul cu cifre de la 0 la lungimeacheii-1 dupa ce aflu lungimea cheii
            caracter = x ^ ls[y]
            if caracter in multime:
                print(chr(caracter), end=' ')
            else:
                contor = 1
                break

        print()
        if contor == 1:
            print(f"{chr(x)} Nu este bun!")
        else:
            print(f"{chr(x)} Este bun!")
        print()
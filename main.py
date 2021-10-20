def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def last_digit(x):
    '''
    determina daca ultima cifra dintr un nr. este egala cu o cifra citita de la tastatura
    :param x: nr. intreg
    :return: True daca ultima cifra dintr un nr. este egala cu o cifra citita de la tastatura, False in caz contrar
    '''
    cifra =int(input("Dati cifra:"))
    while(x!=0):
        cifra1=x%10
        if cifra1==cifra:
            return True
        return False



def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l



def all_negative_numbers(l):
    '''
    determina elementele negative, nenule din lista
    :param l: lista de nr. intregi
    :return: o lista continand elementele negative nenule din ea
    '''
    rezultat = []
    for x in l:
        if x<0:
            rezultat.append(x)
    return rezultat


def test_all_negative_numbers():
    assert all_negative_numbers([12,-1,4,-8])==[-1,-8]
    assert all_negative_numbers([2,5,6,-1,-9,0,-7])==[-1,-9,-7]


def minim_with_last_digit(l):
    '''
    afiseaza cel mai mic nr. din lista care are ultima cifra egala cu o cifra citita de la tastatura
    :param l: lista de nr. intregi
    :return: cel mai mic nr. din lista care are ultima cifra egala cu o cifra citita de la tastatura
    '''
    rezultat = []
    for x in l:
        minim=x
        for i in range(2,len(l)):
            if last_digit(x) and x<min:
                minim=x
                rezultat.append(x)
    return rezultat


def test_minim_with_last_digit():
    assert minim_with_last_digit([1,23,53,24])==23


def number_superprime(l):
    '''
    afiseaza nr. superprime din lista
    :param l: lista de nr. intregi
    :return: toate nr. superprime din lista
    '''
    rezultat=[]
    for x in l:
        while(x>0):



def main():
    l = []
    while True:
        print("1. Citire lista:")
        print("2. Afisare nr. negative nenule:")
        print("3.Afisare cel mai mic nr. care are ultima cifra egala cu o cifra citita de la tastatura:")
        print("4. Afisarea tuturor nr. din lista care sunt superprime:")
        print("5. Afisarea lista in care nr. >0 au fost inlocuite cu CMMDC al lor, iar cele negative cu cifrele lor in ordine inversa:")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(all_negative_numbers(l))
        elif optiune == "3":
            print(minim_with_last_digit(l,8))
        elif optiune == "4":
            print(last_digit(x))
        elif optiune == "":
            break
        else:
            print("Optiune gresita! Reincercati!")

main()

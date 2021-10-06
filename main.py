import math
#Problema 6 // verificare palindrom
def is_palindrome(n) -> bool:

    '''
    Verificare palindrom
    :param n: introducem numarul pe care il verificam daca este palindrom sau nu
    :return: o sa se returneze True daca este palindrom,False in caz contrar
    :i,j:capetele numarului ,inceput,respectiv sfarsit
    '''

    i = 0
    j = len(n) - 1
    while i <= j :
        if n[i] != n[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def test_is_palindrome():

    assert is_palindrome('121') ==True
    assert is_palindrome('123') == False
    assert is_palindrome('555') == True
    assert is_palindrome('2233') == False
    assert is_palindrome('226622') == True

test_is_palindrome()

#Problema 8 //transforma numarul din baza 10 in baza 2
def get_base_2(n:str):
    '''
    Transforma numarul din baza 10 in baza 2
    :param n:numarul pe care vrem sa-l convertim din baza 10 in baza 2
    output: ans- variabila in care apare numarul convertit
    '''
    ans = ""
    n = int(n)
    while n > 0 :
        if n % 2 == 0:
            ans = '0' +ans
        else:
            ans = '1' +ans
        n = n // 2
    return ans

def test_get_base_2():
    assert get_base_2('12') == '1100'
    assert get_base_2('13') == '1101'
    assert get_base_2('100') == '1100100'
    assert get_base_2('77') == '1001101'
    assert get_base_2('6') == '110'


test_get_base_2()

#Problema 12 //afiseaza patratele perfecte dintr-un interval inchis.

def get_perfect_squares(a, b):
    '''
    Cautam toate patratele perfecte din intervalul [a,b]
    - a, b, intregi, capetele intervalului
    -lst, lista patratlor perfecte
    '''
    radacina = int(math.sqrt(a))
    lst = []
    if radacina * radacina < a:
        radacina = radacina + 1
    while radacina <= math.sqrt(b):
        lst.append(radacina * radacina)
        radacina = radacina + 1
    return lst

def test_get_perfect_squares():
    assert get_perfect_squares(1, 9) == [1, 4, 9]
    assert get_perfect_squares(3, 25) == [4, 9, 16, 25]

def main():

    while True:
        print('1.Verificam daca numarul dat este sau nu palindrom.')
        print('2.Fac conversie din baza 10 in baza 2.')
        print('3.Afisez toate patratele perfecte dintr-un interval inchis')

        optiune = input ("Alegeti problema:")
        if optiune == '1':
            numar = input('Dati numarul care se cere sa fie verificat: ')
            ans = is_palindrome(numar)
            if ans:
                print ("Numarul este un palindrom.")
            else:
                print("Numarul nu este un palindrom.")

        elif optiune == '2':
            x = input('Convertesc numarul: ')
            get_base_2(x)
            print(get_base_2(x))

        elif optiune == '3':
            a = int(input("Dati inceput de interval: "))
            b = int(input("Dati sfarsit de interval: "))
            test_get_perfect_squares()
            print(get_perfect_squares(a, b))

        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')

if __name__ == '__main__':
    main()

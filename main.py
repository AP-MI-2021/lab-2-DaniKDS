import math
#Problema 6 // verificare palindrom
def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i <= j :
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def test_is_palindrome():

    assert isPalindrome('ana')
    assert isPalindrome('mar') == False
    assert isPalindrome('mouse') == False
    assert isPalindrome('maam')
    assert isPalindrome('bal') == False

test_is_palindrome()

#Problema 8 //transforma numarul din baza 10 in baza 2
def get_base_2(n:str):
    n = int(n)
    ans = ""
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

def is_perfect(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return True
    return False

def get_perfect_squares(start: int, end: int):
    for i in range( start , end +1 ):
        if is_perfect(i):
            print(f'Numarul {i} este patrat perfect')
        else:
            print(f'Numarul {i} nu este patrat perfect')

def test_get_perfect_squares():
    assert is_perfect(4) == True
    assert is_perfect(16) == True
    assert is_perfect(7) == False

def main():

    while True:
        print('1.Verificam daca numarul dat este sau nu palindrom.')
        print('2.Fac conversie din baza 10 in baza 2.')
        print('3.Afisez toate patratele perfecte dintr-un interval inchis')

        optiune = input ("Alegeti problema:")
        if optiune == '1':
            cuvant = input('Dati cuvantul care se cere sa fie verificat: ')
            ans = isPalindrome(cuvant)
            if ans:
                print ("Cuvantul este un palindrom.")
            else:
                print("Cuvantul nu este un palindrom.")

        elif optiune == '2':
            x = input('Convertesc numarul: ')
            get_base_2(x)
            print(get_base_2(x))

        elif optiune == '3':
            start = input('Stanga :')
            end = input('Dreapta :')
            get_perfect_squares(int(start) , int(end))

        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')
if __name__ == '__main__':
    main()
main()

import random

# to do: repair the problem of loosing when you have one life, regardless of the result
# to do: when you type again the same letter there is no warning

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'

slowa = words.split(' ')
ilosc_slow = len(slowa)
numer_slowa = random.randint(0,ilosc_slow-1)
slowo = slowa[numer_slowa]

dlugosc_slowa = len(slowo)
do_zgadniecia = list('_')*dlugosc_slowa
zycia = 5
print(do_zgadniecia)
' '.join(do_zgadniecia)

def weryfikacja(x, y, z):

    if not '_' in x:
        print('Wygrałeś!')
        return ''.join(x)

    litera = input("Podaj literę, masz {} żyć ".format(y))

    if y == 1:
        print('Przegrałeś')
        return None
    if litera.isalpha():
        if litera in z:
            i = 0
            while i < len(z):
                if z[i] == litera:
                    x[i] = litera
                    print(' '.join(x))
                    i+=1
                    continue
                else:
                    i+=1
                    continue
            if i == len(z):
                return weryfikacja (x, y, z)
        else:
            print("Tej litery tu nie ma")
            print(y-1)
            return weryfikacja(x, y-1, z)
    else:
        print("To nie jest litera, tracisz życie")
        return weryfikacja(x, y-1, z)

weryfikacja(do_zgadniecia, zycia, slowo)
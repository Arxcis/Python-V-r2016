
def tell_bokstaver_tegn(streng):

    bokstaver = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
                 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
                 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                 'y': 0, 'z': 0, " ": 0, '.': 0, ',': 0, 'æ': 0,
                 'ø': 0, 'å':0}


    for i in streng:
        char = i.lower()
        bokstaver[char] = bokstaver.get(char, 0) + 1


    for i in range(97, 123):
        bokstav = chr(i)
        bokstav_verdi = bokstaver[bokstav]
        print(str(bokstav) + "  :    " + str(bokstav_verdi))

    for i in ['æ', 'ø', 'å', ' ', '.', ',']:
        bokstav_verdi = bokstaver[i]
        print(str(i) + "  :    " + str(bokstav_verdi))




a = "Lisa gikk til skolen. Tripp trip trippp, det sa. I den tynne kjolen , trippet hun så glaD. "

tell_bokstaver_tegn(a)

input()
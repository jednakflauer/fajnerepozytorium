import random
import math
print(math.floor(2.5))
dziennik=["jou", "kolega", "daje rade"]
gierka=[]
gierka2=[]
wynik = 0
wynik2 = 0

while True:

    print("nacisnij q aby wyswietlic dziennik")
    print("nacisnij w aby usunac wpis")
    print("nacisnij e aby dodac wpis")
    print("nacisnij r uzyc ulta")
    print("nacisnij f aby zagrac w gierke")
    print("nacisnij d aby zagrac w ciezkiego marcina")
    print("nacisnij s aby byc szefem i wyswietlic dziennik od tylu bo umiesz programowac")
    print("nacisnij x aby zajrzec do muzgu kosiary")

    wybor = input()

    if wybor == "q":
        print(dziennik)
    elif wybor == "w":
        print("ktory wpis?")
        ktory = int(input())
        ktory2 = ktory - 1
        dziennik.pop(ktory2)
    elif wybor == "e":
        print("jaki to wpis?")
        wpis = input()
        dziennik.append(wpis)
    elif wybor == "r":
        for i in range(100):
            print("DEMACIA!!!!!!!")
    elif wybor == "f":
        print("podaj 3 numerki do gierki (0-99)")
        for i in range(3):
            numerki = int(input())
            gierka.append(numerki)
        for i in range(3):
            numerki2 = random.randint(0,99)
            gierka2.append(numerki2)
        for i in gierka:
            wynik += i
        for j in gierka2:
            wynik2 += j
        darkest = random.randint(-99,99)
        if wynik2 <= 100:
            wynik2 += darkest
        elif wynik2 >= 200:
            wynik2 += darkest
        print("tw wynik:", wynik, "wynik kompa:", wynik2)

    elif wybor == "d":
        print("zasady - jesli podasz numerek wiekszy lub mniejszy o 4 od wyniku marcina - \ndostajesz punkcik. jesli nie, marcin dostaje punkcik >:)\nkocham darkest dungeon wiec jest tez element losowy pozdro\n\npodaj swoje imie aby przejsc dalej...")
        imie = input()
        print("walcz z marcinem! wrrrrrr\npodaj cyfre, a nastepnie wcisnij enter aby walczyc!!!")
        rzuty = []
        rzuty2 = []
        cziter = False
        for i in range(3):
            darkest = random.randint(-2,2)
            darkest2 = random.randint(-2,2)
            gracz = int(input())
            if gracz >= 10:
                cziter = True
            komp = random.randint(0,9)
            gracz = gracz + darkest
            komp = komp + darkest2
            if gracz >= komp + 4:
                wynik += 1
            elif gracz <= komp - 4:
                wynik += 1
            else:
                wynik2 += 1
            gierka.append(gracz)
            gierka2.append(komp)
            rzuty.append(darkest)
            rzuty2.append(darkest2)
        if cziter == True:
            print("nie czituj czituchu!! masz bana")
            break
        print("koniec tego pieknego starcia umiejetnosci i intelektu\n",imie,":", gierka, "\n marcin:", gierka2, "\n\nod losu otrzymali...\n",imie,":",rzuty,"\n marcin:", rzuty2, "\n\nostateczny wynik:\n",imie,":", wynik, "\n Marcin:", wynik2)

        wynik = 0
        wynik2 = 0
        gierka.clear()
        gierka2.clear()
    
    elif wybor == "s":
        print(dziennik)

    elif wybor == "x":
        znaki = "1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,/<>?:|[]                                                                                                                                                      kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooossssssssssssssssssssssssssssssssssssssssssssssiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        string = ""
        
        for i in range(10000):
            literka = random.choice(znaki)
            string = string + literka
        print(string)
    elif wybor == "g":
        lancuch = "Kognitywistyka - dziedzina nauki zajmująca się obserwacją i analizą działania zmysłów, mózgu i umysłu, w szczególności ich modelowaniem. Na jej określenie używane są też pojęcia: nauki kognitywne (ang. Cognitive Sciences)[1] bądź nauki o poznaniu. Kognitywistyka jest nauką interdyscyplinarną, znajduje się na pograniczu wielu dziedzin: psychologii poznawczej, neurobiologii, filozofii umysłu, sztucznej inteligencji, lingwistyki oraz logiki i fizyki. Główne obszary badawcze w obrębie tej dziedziny to reprezentacja wiedzy, język, uczenie się, myślenie, percepcja, świadomość, podejmowanie decyzji oraz inteligencja (tzw. inteligencja kognitywna). Konferencja MIT - 11 września 1956 roku (m.in. Claude E. Shannon, Allen Newell, Herbert A. Simon, Noam Chomsky, George Miller): \"dzień, w którym kognitywistyka wyskoczyła z łona cybernetyki i stała się szanowanym, interdyscyplinarnym przedsięwzięciem realizowanym na swój własny rachunek\" (George Miller, 1979). Kognitywistyka jako samodzielna dziedzina nauki wyodrębniła się w 1975 roku w Stanach Zjednoczonych. W 1976 roku zaczęto wydawać kwartalnik \"Cognitive Science\". Program badaczy kognitywistyki został przedstawiony w tym samym roku przez Allena Newella oraz Herberta Simona w artykule Informatyka jako badania empiryczne[2]. Kognitywistyka symboliczna nie jest dobrze zdefiniowana w naukowej literaturze światowej i koncentruje się na symbolicznym modelowaniu uświadamianych abstrakcyjnych funkcji myślowych uznawanych za takie same u wszystkich ludzi i dotyczy: samoświadomości (metakognitywistyka, ang. metacognition), kognitywnego podejmowania decyzji (cognitive decision-making) i inteligencji socjo-kognitywistycznej/kognitywnej jako uniwersalnych własności jednostki, grupy, organizacji ludzkich i robotów. Tego typu działalność naukowa prowadzi do rozwoju nowego podejścia integrującego paradygmaty teorii systemów, inżynierii, nauk społecznych i kognitywistyki, tzw. inżynierii socjokognitywistycznej (lub socio-kognitywistycznej) rozwijanej przez Adama Marię Gadomskiego w ramach meta-teorii TOGA[3]. Od strony zastosowanych technologii kognitywistyka symboliczna koncentruje się na rozbudowie tzw. baz wiedzy (KB - knowledge base) i budowie skomplikowanych Systemów Bazujących na Wiedzy (Knowledge Base System), które to realizują różne funkcje uważane za charakterystyczne dla systemów inteligentnych. Jednym z ważnych, a nierozwiązanych jeszcze wystarczająco problemów kognitywistyki jest definicja świadomości, czyli zdolności syntezy i myślenia o własnym myśleniu. Kognitywistyka subsymboliczna bazuje głównie na wyjaśnianiu procesów myślowych w mózgu ludzkim opartych na własnościach sieci neuronowych. Coraz popularniejszym paradygmatem kognitywistyki subsymbolicznej staje się nauka, w której łączy się wzorce i modele pochodzące z tradycyjnych nauk o poznawaniu, psychologii, neurobiologii i wielu innych subdyscyplin nauk przyrodniczych. Jednym z najbardziej znanych specjalistów w tej dziedzinie w Polsce jest Włodzisław Duch."
        lancuch = lancuch.lower()
        nowylancuch = ""
        lista = []
        slowo = ""
        lista = lancuch.split(" ")
        for literka in lancuch:
            if literka == "ą":
                nowylancuch += "a"
            elif literka == "ć":
                nowylancuch += "c"
            elif literka == "ę":
                nowylancuch += "e"
            elif literka == "ł":
                nowylancuch += "l"
            elif literka == "ó":
                nowylancuch += "o"
            elif literka == "ź":
                nowylancuch += "z"
            elif literka == "ż":
                nowylancuch += "z"
            else:
                if not literka.isdigit():
                    nowylancuch += literka
        
        for i in lista:
            if i == "":
                lista.remove(i)

        licznikslow = {}
        for slowo in lista:
            if slowo in licznikslow:
                licznikslow[slowo] += 1
            else:
                licznikslow[slowo] = 1

        print(nowylancuch)
        print(lancuch.lower())
        print(lista)
        print(licznikslow)

        #is.alpha

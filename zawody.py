imiona = ["marcin", "marek", "mariusz"]
zawody = ["zarobas", "hustler", "szef"]

while True:
    print("jaki zawud")
    zawud = input()
    if zawud == "zarobas":
        print(imiona[0])
    elif zawud == "hustler":
        print(imiona[1])
    elif zawud == "szef":
        print(imiona[2])
    elif zawud == "x":
        print("podaj co")
        co1 = input()
        imiona.append(co1)
        print("co z czym")
        co2 = input()
        zawody.append(co2)
    elif zawud == "v":
        print("wybierz delikwneta")
        delikwent = int(input())
        print(imiona[delikwent], zawody[delikwent])
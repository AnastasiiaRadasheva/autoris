from MyModule import *

while True:
    print("Valikud:")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5 - Lõpetamine")

    valik = input("Valige toiming (1/2/3/4/5): ")

    if valik == "1":
        registreeri()

    elif valik == "2":
        kasutaja = sisselogimine()

    elif valik == "3":
        muuda_andmeid()

    elif valik == "4":
        unusta_parool()

    elif valik == "5":
        print("Programmi lõpetamine...")
        break

    else:
        print(" Vale valik! Proovi uuesti.")
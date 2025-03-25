import random

login_list = ["gh"]
parool_list = ["9"]

def log(login: str) -> bool:
    """Kontrollib, kas kasutajanimi on süsteemis."""
    return login in login_list

def login_parool(login: str, parool: str) -> bool:
    """Kontrollib, kas parool vastab kasutajanimele."""
    if login in login_list:
        i = login_list.index(login)
        return parool_list[i] == parool
    return False

def genereeri_parool():
    """Genereerib juhusliku 8-tähelise parooli."""
    str0 = "!#¤%&/()=?"
    str1 = '1234567890'
    str2 = 'qwertyuiopüõasdfghjklöäzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    return ''.join(random.choice(str4) for _ in range(8))

def parooli_kontroll(parool: str) -> bool:
    """Kontrollib, kas parool on vähemalt 8 tähemärki pikk."""
    return len(parool) >= 8

def registreeri():
    """Registreerib uue kasutaja."""
    while True:
        login = input("Sisestage uus kasutajanimi: ")
        if log(login):
            print("See kasutajanimi on juba hõivatud! Proovige uuesti.")
        else:
            break
    login_list.append(login)

    valik = input("Kas soovite parooli genereerida? (jah/ei): ").lower()
    
    if valik == "jah":
        uus_parool = genereeri_parool()
        print(f"Teie uus parool on: {uus_parool}")
    else:
        while True:
            uus_parool = input("Sisestage oma parool (vähemalt 8 tähemärki): ")
            if parooli_kontroll(uus_parool):
                break
            print("Parool peab olema vähemalt 8 tähemärki pikk!")

    parool_list.append(uus_parool)
    print("Registreerimine edukas!")

def sisselogimine():
    """Kasutaja saab sisse logida."""
    login = input("Sisestage oma kasutajanimi: ")

    if login in login_list:
        i = login_list.index(login)
        while True:
            parool = input("Sisestage oma parool: ")
            if parool_list[i] == parool:
                print("Sisselogimine edukas!")
                return login  # Tagastab sisse logitud kasutajanime
            else:
                print("Vale parool! Proovi uuesti.")
    else:
        print("Sellist kasutajat pole!")
    return None

def muuda_andmeid():
    """Lubab muuta kasutajanime või parooli."""
    login = input("Sisestage oma kasutajanimi: ")

    if login in login_list:
        i = login_list.index(login)
        print("Mida soovite muuta?")
        print("1 - Kasutajanimi")
        print("2 - Parool")
        valik = input("Valige (1/2): ")

        if valik == "1":
            uus_nimi = input("Sisestage uus kasutajanimi: ")
            if uus_nimi in login_list:
                print("See kasutajanimi on juba võetud!")
            else:
                login_list[i] = uus_nimi
                print("Kasutajanimi edukalt muudetud!")

        elif valik == "2":
            uus_parool = input("Sisestage uus parool (vähemalt 8 tähemärki): ")
            if parooli_kontroll(uus_parool):
                parool_list[i] = uus_parool
                print("Parool edukalt muudetud!")
            else:
                print("Parool peab olema vähemalt 8 tähemärki pikk!")

        else:
            print("Vale valik!")
    else:
        print("Sellist kasutajat pole süsteemis!")

def unusta_parool():
    """Võimaldab kasutajal parooli taastada."""
    login = input("Sisestage oma kasutajanimi: ")

    if login in login_list:
        i = login_list.index(login)
        valik = input("Kas soovite ise uue parooli luua või lasta see genereerida? (I/G): ").lower()

        if valik == "g":
            uus_parool = genereeri_parool()
            print(f"Teie uus parool on: {uus_parool}")
        else:
            while True:
                uus_parool = input("Sisestage uus parool (vähemalt 8 tähemärki): ")
                if parooli_kontroll(uus_parool):
                    break
                print("Parool peab olema vähemalt 8 tähemärki pikk!")

        parool_list[i] = uus_parool
        print("Teie parool on edukalt muudetud!")
    else:
        print("Sellist kasutajanime pole süsteemis!")
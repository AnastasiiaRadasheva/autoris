import random
import smtplib, ssl
from email.message import EmailMessage
import os

FILENAME = "module1.txt"

login_list = []
parool_list = []

def lae_kasutajad_failist():
    """Laeb olemasolevad kasutajad failist mällu."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            for rida in f:
                if "-" in rida:
                    login, parool = rida.strip().split("-", 1)
                    login_list.append(login)
                    parool_list.append(parool)

def salvesta_kasutajad_faili():
    """Salvestab kõik kasutajad faili."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        for login, parool in zip(login_list, parool_list):
            f.write(f"{login}-{parool}\n")

def saada_kiri(kellele, teema, html_sisu):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    kellelt = 'eha20082@gmail.com'
    salasõna = 'pjuj tvvc ogta dxkb'

    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = kellelt
    msg['To'] = kellele
    text_sisu = "Tere! Kui sa ei näe seda kirja õigesti, palun lülita sisse HTML kuvamine."
    msg.set_content(text_sisu)
    msg.add_alternative(html_sisu, subtype='html')

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(kellelt, salasõna)
            server.send_message(msg)
            print("Email saadetud edukalt!")
    except Exception as e:
        print(f"Viga e-kirja saatmisel: {e}")

def registreeri():
    while True:
        kellele = input('Mis on sinu epost? ')
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
    salvesta_kasutajad_faili()
    print("Registreerimine edukas!")

    teema = 'Uue konto loomine'
    html_sisu = f"""\
    <html><body>
    <h1>Uue konto loomine edukas!</h1>
    <p>Tere {login},</p>
    <p>Kasutajanimi: {login}</p>
    <p>Parool: {uus_parool}</p>
    </body></html>
    """
    saada_kiri(kellele, teema, html_sisu)

def log(login: str) -> bool:
    return login in login_list

def login_parool(login: str, parool: str) -> bool:
    if login in login_list:
        i = login_list.index(login)
        return parool_list[i] == parool
    return False

def genereeri_parool():
    str0 = "!#¤%&/()=?"
    str1 = '1234567890'
    str2 = 'qwertyuiopüõasdfghjklöäzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    return ''.join(random.choice(str4) for _ in range(8))

def parooli_kontroll(parool: str) -> bool:
    return len(parool) >= 8

def sisselogimine():
    login = input("Sisestage oma kasutajanimi: ")
    if login in login_list:
        i = login_list.index(login)
        while True:
            parool = input("Sisestage oma parool: ")
            if parool_list[i] == parool:
                print("Sisselogimine edukas!")
                return login
            else:
                print("Vale parool! Proovi uuesti.")
    else:
        print("Sellist kasutajat pole!")
    return None

def muuda_andmeid():
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
        salvesta_kasutajad_faili()
    else:
        print("Sellist kasutajat pole süsteemis!")

def unusta_parool():
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
        salvesta_kasutajad_faili()
    else:
        print("Sellist kasutajanime pole süsteemis!")

# Laadime olemasolevad kasutajad mällu
lae_kasutajad_failist()

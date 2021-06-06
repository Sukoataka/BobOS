import random
import time as t
import os


nee = ["nee", "neen", "NEE", "NEEN" , "n", "N", "Nee", "Neen", "No", "no", "NO"]
ja = ["ja", "jaa", "JA", "JAA", "jep", "jup", "y", "Y", "j", "Ja", "Jup", "Jep", "yes", "YES", "yess", "Yess", "YESS", "Yes", "J"]
afsluiten = ["Sluit af", "afsluiten", "Exit", "exit", "EXIT", "Aflsuiten", "AFSLUITEN","sluit af", "SLUIT AF"]

PW_karakters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#@abcdefghijklmnopqrstuvwxyz!#@!#@"
PW_random_karakter = random.randint(0, len(PW_karakters))

def passwordGen():
    for i in range(20):
        print("\n")
    print("Je wachtwoord moet minimaal 8 karakters bevatten!")
    for i in range(2):
        print("\n")


    newPw = True

    while newPw:
        platform = input("Voor welk platform is dit wachtwoord?: ")
        if platform in afsluiten:
            t.sleep(0.5)
            for i in range(20):
                print("\n")
            return 0
        else:
            try:
                lengte_pw = int(input("Hoeveel karakters moet je wachtwoord bevatten?: "))
                wachtwoord = "" 
                if lengte_pw < 8:
                    print("Je wachtwoord moet 8 karakters bevatten!\n\n")
                else:
                    for i in range(0, lengte_pw):
                        wachtwoord = wachtwoord + PW_karakters[random.randint(0,( len(PW_karakters) - 1))]
                    path = os.getcwd()
                    savedPwPath = str(f"{path}\passwords.txt")
                    for i in range(20):
                        print("\n")
                    print(f"Je nieuwe wachtwoord voor {platform} is: {wachtwoord}!\nJe kan alles terugvinden in {savedPwPath}")
                    for i in range(2):
                        print("\n")
                    with open("passwords.txt", 'a') as f:
                        f.write(f"{platform}: {wachtwoord}\n")
                    t.sleep(4)
                    restart_loop = True
                    while restart_loop:
                        restart = input("Wil je nog een wachtwoord ingeven?: ")
                        if restart in ja:
                            for i in range(20):
                                print("\n")
                            t.sleep(2)
                            restart_loop = False
                        elif restart in nee:
                            for i in range(20):
                                print("\n")
                            print("Oke, we sluiten de wachtwoordgenerator af!")
                            for i in range(2):
                                print("\n")
                            t.sleep(3)
                            restart_loop = False
                            newPw = False
                        else:
                            print("Geen geldig antwoord!")
            except:
                for i in range(20):
                    print("\n")
                print("ERROR: Je moet een getal invoeren!")
                for i in range(2):
                    print("\n")
                    t.sleep(2)

if __name__ == "__main__":
    passwordGen()
            


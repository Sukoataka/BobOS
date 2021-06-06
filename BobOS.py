import base64
import time as t
import os
import getpass
from datetime import *
import webbrowser
from bobPwGenerator import passwordGen
from bobCalc import *

OSversion = ""
with open("updated.txt", "r") as f:
    lines = f.readlines()
    OSversion = lines[0]

OSname = "BobOS"
OSpath = os.path.abspath(__file__)
loginFile = "usernamePwEncrypted.key"


nee = ["nee", "neen", "NEE", "NEEN" , "n", "N", "Nee", "Neen", "No", "no", "NO"]
ja = ["ja", "jaa", "JA", "JAA", "jep", "jup", "y", "Y", "j", "Ja", "Jup", "Jep", "yes", "YES", "yess", "Yess", "YESS", "Yes", "J"]


def osIdle():
    try:
        for i in range(20):
            print("\n")
        print("Login is gelukt...\nSluit NIET af!")
        for i in range(2):
            print("\n")
        t.sleep(3)
        for i in range(20):
            print("\n")

        afsluiten = ["Sluit af", "afsluiten", "Exit", "exit", "EXIT", "Aflsuiten", "AFSLUITEN","sluit af", "SLUIT AF"]
        helpCommand = ["help", "Help", "HELP", "?", "?h", "?help", "?Help", "?HELP"]
        time = ["time", "Time", "TIME", "Hoe laat", "hoelaat", "Tijd", "tijd", "TIJD"]
        restart = ["restart", "Restart"]
        changeUserInfo = ["changeUserInfo", "changeuserinfo", "ChangeUserInfo", "CHANGEUSERINFO", "Verandergegevens", "verandergegevens", "VeranderGegevens", "veranderGegevens", "VERANDERGEGEVENS"]
        generatePassword = ["generatepassword", "GeneratePassword", "GENERATEPASSWORD", "Maakwachtwoord", "maakwachtwoord", "MAAKWACHTWOORD", "genpw", "Genpw", "GenPw", "GenPW", "pwgen", "Pwgen", "PWgen", "PWGEN"]
        website = ["Website", "website", "WEBSITE", "openwebsite", "OpenWebsite", "Openwebsite", "openWebsite", "OPENWEBSITE", "Openurl", "openurl", "OpenUrl", "OPENURL"]
        calculate = ["Calculate", "Calc", "calculate", "calc", "CALCULATE", "CALC", "rekenmachine", "Rekenmachine", "REKENMACHINE", "Bereken", "bereken", "BEREKEN", "reken", "Reken", "REKEN"]
        commands = [" Exit\n","Help\n", "Restart\n", "Tijd\n", "Verandergegevens\n", "Maakwachtwoord\n", "Openurl\n", "Update\n", "Calc"]
        update = ["Update", "UPDATE", "update"]

        def OS_help():
            for i in range(20):
                print("\n")
            print("Hieronder vind u een lijst van alle commando's: \n")
            commandsString = ' '.join(map(str, commands))
            print(commandsString)
            for i in range(1):
                print("\n")
            t.sleep(1.25)

        BobOS_on = True
        while BobOS_on:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{current_time}")
            command_input = input(f"{OSname} >>> ")
            command = command_input.lower()
            if command in afsluiten:
                exit_loop = True
                while exit_loop:
                    exit_sure = input("Ben je zeker dat je wilt afsluiten?: ")
                    if exit_sure in ja:
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        for i in range(20):
                            print("\n")
                        print(f"Even geduld, we sluiten {OSname} af...\nVersie: {OSversion}\nTijd: {current_time}")
                        for i in range(3):
                            print("\n")
                        t.sleep(3.25)
                        exit_loop = False
                        BobOS_on = False
                        exit_sure = False
                        
                    elif exit_sure in nee:
                        for i in range(20):
                            print("\n")
                        print(f"Oke, we loggen je niet uit...")
                        for i in range(3):
                            print("\n")
                        t.sleep(2)
                        exit_loop = False
                    elif exit_sure == "& C:/Users/32474/AppData/Local/Programs/Python/Python39/python.exe c:/Users/32474/OneDrive/Bureaublad/School/Informatica/Python/BobOS/BobOS.py":
                        os.system(f"python {OSpath}")
                        return 0
                    else:
                        for i in range(20):
                            print("\n")
                        print(f"U kan alleen antwoorden met (ja/nee)")
                        for i in range(3):
                            print("\n")
                        t.sleep(2)

            elif command == "& C:/Users/32474/AppData/Local/Programs/Python/Python39/python.exe c:/Users/32474/OneDrive/Bureaublad/School/Informatica/Python/BobOS/BobOS.py":
                os.system(f"python {OSpath}")
                return 0
            elif command in helpCommand:
                OS_help()

            elif command in time:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                for i in range(20):
                    print("\n")
                print(f"Het is nu {current_time}")
                for i in range(2):
                    print("\n")
                t.sleep(1.25)

            elif command in restart:
                restart_loop = True
                while restart_loop:
                    restart_sure = input("Ben je zeker dat je wilt restarten?: ")
                    if restart_sure in ja:
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        for i in range(20):
                            print("\n")
                        print(f"Even geduld, we starten {OSname} opnieuw op\nVersie: {OSversion}\nTijd: {current_time}")
                        for i in range(2):
                            print("\n")
                        t.sleep(3.25)
                        os.system(f"python {OSpath}")
                        return 0
                    elif restart_sure in nee:
                        for i in range(20):
                            print("\n")
                        print(f"Oke, we restarten niet!")
                        for i in range(3):
                            print("\n")
                        t.sleep(2)
                        restart_loop = False
                        restart_sure = False
                    else:
                        for i in range(20):
                            print("\n")
                        print(f"U kan alleen antwoorden met (ja/nee)")
                        for i in range(3):
                            print("\n")
                        t.sleep(2)

            elif command in changeUserInfo:
                for i in range(20):
                    print("\n")
                regNewUsername = input("Oke, kies een username: ")
                regNewUsernameBytes = regNewUsername.encode("ascii")
                regNewUsernameBase = base64.b64encode(regNewUsernameBytes)
                regNewPw = input(f"Oke, je nieuwe username is nu {regNewUsername}. Wat wil je als wachtwoord? (Als je hetzelfde wilt als je hebt, typ dan hier je wachtwoord dat je al hebt!): ")
                regNewPwBytes = regNewPw.encode("ascii")
                regNewPwBase = base64.b64encode(regNewPwBytes)

                with open(loginFile, "w") as f:
                    f.write(f"{regNewUsernameBase}{regNewPwBase}")

                print(f"Je username is nu {regNewUsername} en je wachtwoord is nu {regNewPw}.\n")
                t.sleep(3)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                for i in range(20):
                    print("\n")
                print(f"Even geduld, we starten {OSname} opnieuw op om de gegevens op te slaan!\nVersie: {OSversion}\nTijd: {current_time}")
                for i in range(2):
                    print("\n")
                t.sleep(3.25)
                os.system(f"python {OSpath}")
                return 0

            elif command in generatePassword:
                t.sleep(1.25)
                passwordGen()
            
            elif command in website:
                site = input("Geef de website in die je wilt bezoeken (vergeet .com enzo niet!): ")
                webbrowser.open(f"https://{site}")
                command = "//"
                for i in range(20):
                    print("\n")
                print(f"De website {site} is geladen!")
                for i in range(2):
                    print("\n")
                t.sleep(2)

            elif command in calculate:
                for i in range(20):
                    print("\n")
                print("Rekenmachine start op...")
                for i in range(2):
                    print("\n")
                    t.sleep(2)
                calculator()

            elif command in update:
                for i in range(20):
                    print("\n")
                print("Even geduld we zoeken naar updates...")
                for i in range(2):
                    print("\n")
                t.sleep(5)

                with open("updated.txt", "r") as f:
                    lines = f.readlines()
                if lines[0] != OSversion:
                    restart_loop = True
                    while restart_loop:
                        restart_sure = input("Ben je zeker dat je wilt updaten?: ")
                        if restart_sure in ja:
                            for i in range(20):
                                print("\n")
                            print("...")
                            t.sleep(5)
                            for i in range(2):
                                print("\n")
                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            for i in range(20):
                                print("\n")
                            print(f"Even geduld, we starten {OSname} opnieuw op\nVersie: {OSversion}\nTijd: {current_time}")
                            for i in range(2):
                                print("\n")
                            t.sleep(3.25)
                            os.system(f"python {OSpath}")
                            return 0
                        elif restart_sure in nee:
                            for i in range(20):
                                print("\n")
                            print(f"Oke, we restarten niet!")
                            for i in range(3):
                                print("\n")
                            t.sleep(2)
                            restart_loop = False
                            restart_sure = False
                        else:
                            for i in range(20):
                                print("\n")
                            print(f"U kan alleen antwoorden met (ja/nee)")
                            for i in range(3):
                                print("\n")
                            t.sleep(2)
                else:
                    for i in range(20):
                        print("\n")
                    print(f"Je hebt al de laatste versie van BobOS!\nVersie: {OSversion}")
                    for i in range(2):
                        print("\n")
                    t.sleep(3)

            else:
                print("\n\n")
    except:
        for i in range(20):
            print("\n")
        print("FATALE ERROR")
        for i in range(2):
            print("\n")
        t.sleep(3)
        os.system(f"python {OSpath}")
        return 0 


def osStart():
    for i in range(20):
        print("\n")
    print(f"Even geduld, we loggen je in...\nSluit NIET af!")
    for i in range(2):
        print("\n")
    t.sleep(3)
    osIdle()
    

def login():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    for i in range(20):
        print("\n")
    print(f"Even geduld, we starten {OSname} op...\nVersie: {OSversion}\nTijd: {current_time}")
    for i in range(2):
        print("\n")
    t.sleep(5)
    loginLoop = True
    while loginLoop:
        login = input("Heb je al een account?: ")
        if login in ja:
            loggingIn = "y"
            tries = 0
            while loggingIn == "y":
                username = input("Wat is je username?: ")
                usernameAscii = username.encode("ascii")
                usernameB64 = base64.b64encode(usernameAscii)
                pw = getpass.getpass(prompt='Wat is je wachtwoord?: ', stream=None)
                pwAscii = pw.encode("ascii")
                pwB64 = base64.b64encode(pwAscii)
                usernamePwB64 = f"{usernameB64}{pwB64}"

                with open(loginFile, "r") as f:
                    lines = f.readlines()
                    try:
                        if lines[0] == usernamePwB64:
                            loggingIn = "n"
                            loginLoop = False
                            osStart()
                            return 0
                        else:
                            tries = tries+1
                            t.sleep(2)
                            if tries == 4:
                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                for i in range(20):
                                    print("\n")
                                print(f"Je hebt teveel keer proberen in te loggen!\nJe moet nu 1 minuut wachten!\nTijd: {current_time}")
                                for i in range(2):
                                    print("\n")
                                t.sleep(60)
                                for i in range(20):
                                    print("\n")
                                print(f"Even geduld, we starten {OSname} opnieuw op\nVersie: {OSversion}\nTijd: {current_time}")
                                for i in range(2):
                                    print("\n")
                                t.sleep(3.25)
                                os.system(f"python {OSpath}")
                                return 0
                            elif tries > 4:
                                os.system(f"python {OSpath}")
                                return 0
                            else:
                                print("\nJe username of wachtwoord is FOUT!")
                                print("Probeer het opnieuw of registreer opnieuw door opnieuw op te starten!\n")
                                print(f"Je zit op poging {tries}/3!\n")
                                t.sleep(1)
                    except:
                        for i in range(20):
                            print("\n")
                        print("FATALE ERROR")
                        for i in range(2):
                            print("\n")
                        t.sleep(4)
                        return 0

        elif login in nee:
            regUsername = input("Oke, kies een username: ")
            regUsernameBytes = regUsername.encode("ascii")
            regUsernameBase = base64.b64encode(regUsernameBytes)
            regPw = input(f"Oke, je username is nu {regUsername}. Wat wil je als wachtwoord?: ")
            regPwBytes = regPw.encode("ascii")
            regPwBase = base64.b64encode(regPwBytes)

            with open(loginFile, "w") as f:
                f.write(f"{regUsernameBase}{regPwBase}")

            print(f"Je username is nu {regUsername} en je wachtwoord is nu {regPw}.\n")
            t.sleep(3)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            for i in range(20):
                print("\n")
            print(f"Even geduld, we starten {OSname} opnieuw op om de gegevens op te slaan!\nVersie: {OSversion}\nTijd: {current_time}")
            for i in range(2):
                print("\n")
            t.sleep(3.25)
            os.system(f"python {OSpath}")
            return 0
        elif login == "& C:/Users/32474/AppData/Local/Programs/Python/Python39/python.exe c:/Users/32474/OneDrive/Bureaublad/School/Informatica/Python/BobOS/BobOS.py":
            os.system(f"python {OSpath}")
            loginLoop = False
            return 0
        else:
            print("Je hebt geen geldig antwoord gegeven.")
            t.sleep(3)
            for i in range(20):
                print("\n")



if __name__ == "__main__":
    login()
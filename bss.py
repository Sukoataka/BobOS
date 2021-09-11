import time as t
import random

nee = ["nee", "neen", "NEE", "NEEN", "n", "N", "Nee", "Neen", "No", "no", "NO"]
ja = ["ja", "jaa", "JA", "JAA", "jep", "jup", "y", "Y", "j", "Ja",
      "Jup", "Jep", "yes", "YES", "yess", "Yess", "YESS", "Yes", "J"]


def bssMain():

    for i in range(20):
        print("\n")

    options = ["blad", "steen", "schaar"]

    while True:
        userInput = input("Blad, steen of schaar?: ")
        userInput = userInput.lower()
        randomInt = random.randint(0, 2)
        if userInput not in options:
            print("\nGebruik: blad, steen of schaar\n")
        else:
            compInput = options[randomInt]
            t.sleep(0.5)
            if compInput == "blad" and userInput == "schaar":
                print(f"\nProficat! Je hebt gewonnen, jij koos {userInput} en de computer koos {compInput}!\n")
            elif compInput == "steen" and userInput == "blad":
                print(f"\nProficat! Je hebt gewonnen, jij koos {userInput} en de computer koos {compInput}!\n")
            elif compInput == "schaar" and userInput == "steen":
                print(f"\nProficat! Je hebt gewonnen, jij koos {userInput} en de computer koos {compInput}!\n")
            elif compInput == userInput:
                print(f"\nAi jammer! Je hebt gelijk gespeeld met de computer, jij koos {userInput} en de computer koos {compInput}!\n")
            else:
                print(f"\nAi jammer! Je hebt verloren, jij koos {userInput} en de computer koos {compInput}!\n")
            while True:
                anotherTime = input("Wil je nog een keer spelen? (Y/N): ")
                t.sleep(1.25)
                for i in range(20):
                    print("\n")
                if anotherTime in ja:
                    break
                elif anotherTime in nee:
                    print("\nOke, tot de volgende keer...")
                    return 0
                else:
                    continue


if __name__ == "__main__":
    bssMain()

import time as t
import random

def casinoMain():
    for i in range(20):
        print("")

    nee = ["nee", "neen", "NEE", "NEEN", "n", "N", "Nee", "Neen", "No", "no", "NO"]
    ja = ["ja", "jaa", "JA", "JAA", "jep", "jup", "y", "Y", "j", "Ja","Jup", "Jep", "yes", "YES", "yess", "Yess", "YESS", "Yes", "J"]

    blackjack = ["blackjack", "bj", "21"]


    def BJ21Game(sessionBet, totalBet, money):
        print("IT WORKS")

    def sesBet(sessionBet, totalBet, money, game):
        t.sleep(2)

        for i in range(20):
            print("")

        print(f"Je overgebleven geld bedraagt: {money}\nJe hebt {totalBet} euro meegenomen\nJe gebruikt {sessionBet}\nJe hebt nog {totalBet - sessionBet} over voor deze sessie.\n")

        veranderen = ["change", "veranderen", "verander"]
        spelen = ["spelen", "speel", "play"]

        while True:
            betSure = input("Wil je spelen of je inzet veranderen?: ").lower()
            if betSure in spelen:
                if game in blackjack:
                    BJ21Game(sessionBet, totalBet, money)
                    break
            elif betSure in veranderen:
                gameMain(game, totalBet, money)
                break
        return 0



    def gameMain(game, totalBet, money):
        t.sleep(2)
        for i in range(20):
            print("")
        
        while True:
            try:
                while True:
                    sessionBet = int(input("Hoeveel wil je deze sessie gebruiken?: "))

                    if sessionBet > totalBet:
                        for i in range(3):
                            print("")

                        print(f"Geef een geheel getal lager dan {totalBet} in aub!")
                        t.sleep(1.75)

                        for i in range(3):
                            print("")

                        continue

                    elif sessionBet <= 0:
                        for i in range(3):
                            print("")
                        print(f"Geef een geheel getal hoger dan 0 in aub!")
                        t.sleep(1.75)
                        for i in range(3):
                            print("")
                        continue

                    else:
                        sesBet(sessionBet, totalBet, money, game)
                        return 0  
            except ValueError:
                continue
        

    def whichGame():
        while True:
            money = 1000
            print("Beschikbare games: Blackjack")
            game = input("Welke game wil je spelen?: ").lower()

            if game in blackjack:
                t.sleep(1)
                for i in range(20):
                    print("")
                print(f"We starten {game} op...")
                print("\n\n")
                t.sleep(2)
                for i in range(7):
                    print("\n")
                
                while True:
                    try:
                        while True:
                            print(f"Je hebt {money} euro thuis liggen.")
                            totalBet = int(input("Hoeveel geld wil je meedoen van thuis?: "))

                            if totalBet > money:
                                for i in range(3):
                                    print("")

                                print(f"Geef een geheel getal lager dan {money} in aub!")
                                t.sleep(1.75)

                                for i in range(3):
                                    print("")

                                continue

                            elif totalBet <= 0:
                                for i in range(3):
                                    print("")
                                print(f"Geef een geheel getal hoger dan 0 in aub!")
                                t.sleep(1.75)
                                for i in range(3):
                                    print("")
                                continue

                            else:
                                money = money - totalBet
                                gameMain(game, totalBet, money)
                                break
                        break  
                    except ValueError:
                        continue
            else:
                for i in range(20):
                    print("\n")

                continue

            break

    whichGame()

if __name__ == "__main__":
    casinoMain()
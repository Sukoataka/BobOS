import time as t
import math

nee = ["nee", "neen", "NEE", "NEEN" , "n", "N", "Nee", "Neen", "No", "no", "NO"]
ja = ["ja", "jaa", "JA", "JAA", "jep", "jup", "y", "Y", "j", "Ja", "Jup", "Jep", "yes", "YES", "yess", "Yess", "YESS", "Yes", "J"]

t.sleep(1)

def anotherCalc():
    t.sleep(1.5)
    anotherCalcLoop = True
    while anotherCalcLoop:
        anotherCalculation = input("\nWil je nog een berekening doen?: ")
        if anotherCalculation in ja:
            for i in range(20):
                print("\n")
            t.sleep(1.5)
            calculator()
            return 0
        elif anotherCalculation in nee:
            for i in range(20):
                print("\n")
            print("Even geduld, we sluiten de rekenmachine af...")
            for i in range(2):
                print("\n")
            t.sleep(2.25)
            for i in range(20):
                print("\n")
            return 0
        else:
            for i in range(20):
                print("\n")
            print("ERROR: je kan alleen antwoorden met ja/nee!")
            for i in range(2):
                print("\n")
            t.sleep(2)

def calculator():
    try:
        newNumber  = True
        while newNumber:   
            num1 = float(input("Geef je eerste nummer in: "))
            operator = input("Geef een operator in (+, -, *, :, **, //): ")
                
            if operator == "+":
                num2  = float(input("Geef je tweede nummer in: "))
                result = num1 + num2
                for i in range(20):
                    print("\n")
                print(f"De uitkomst is: {result}")
                for i in range(2):
                    print("\n")
                anotherCalc()
                return 0
            elif operator == "-":
                num2  = float(input("Geef je tweede nummer in: "))
                result = num1 - num2
                for i in range(20):
                    print("\n")
                print(f"De uitkomst is: {result}")
                for i in range(2):
                    print("\n")
                anotherCalc()
                return 0
            elif operator == "*":
                num2  = float(input("Geef je tweede nummer in: "))
                result = num1 * num2
                for i in range(20):
                    print("\n")
                print(f"De uitkomst is: {result}")
                for i in range(2):
                    print("\n")
                anotherCalc()
                return 0
            elif operator == "/":
                num2  = float(input("Geef je tweede nummer in: "))
                result = num1 / num2
                for i in range(20):
                    print("\n")
                print(f"De uitkomst is: {result}")
                for i in range(2):
                    print("\n")
                anotherCalc()
                return 0
            elif operator == "**":
                num2  = float(input("Tot de hoeveelste macht?: "))
                result = num1**num2
                for i in range(20):
                    print("\n")
                print(f"De uitkomst is: {result}")
                for i in range(2):
                    print("\n")
                anotherCalc()
                return 0
            elif operator == "//":
                result = math.sqrt(num1)
                for i in range(20):
                    print("\n")
                print(f"De uitkomst is: {result}")
                for i in range(2):
                    print("\n")
                anotherCalc()
                return 0 
            else:
                for i in range(20):
                    print("\n")
                print("Er is een error opgedoken! Probeer het opnieuw!")
                for i in range(2):
                    print("\n")
                t.sleep(2)
                        
    except:
        for i in range(20):
            print("\n")
        print("FATALE ERROR")
        for i in range(2):
            print("\n")
        t.sleep(4)
        return 0

if __name__ == "__main__":
    calculator()

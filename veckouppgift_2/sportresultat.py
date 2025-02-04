# uppgift: sportresultat

def main():
    print("Matchen är över, nu ska vi räkna ut resultatet!")

    # Frågar användaren om antal mål för båda lagen
    tottenham_mal = int(input("Hur många mål gjorde Tottenham? "))
    liverpool_mal = int(input("Hur många mål gjorde Liverpool? "))

    # Jämför resultaten och skriver ut matchens utfall
    if tottenham_mal > liverpool_mal:
        diff = tottenham_mal - liverpool_mal
        print(f"Tottenham vann med {diff} mål!")
    elif liverpool_mal > tottenham_mal:
        diff = liverpool_mal - tottenham_mal
        print(f"Liverpool vann med {diff} mål!")
    else:
        print("Matchen slutade oavgjort!")


if __name__ == "__main__":
    main()



# uppgift: kvittouträknaren

def kvittoutraknare():
    print("Välkommen till Kvittokompis! Skriv 'quit' eller 'avsluta' för att avsluta.")
    total = 0

    while (belopp := input("Skriv in ett belopp: ").strip().lower()) not in ["quit", "avsluta"]:
        try:
            total += float(belopp)
        except ValueError:
            print("Felaktigt värde, försök igen.")

    personer = int(input("Hur många är ni? ") or 1)
    dricks = float(input("Hur många procent dricks? (Tryck Enter för 10%) ") or 10)
    total_med_dricks = total * (1 + dricks / 100)

    print(f"Totalt: {total_med_dricks:.2f} kr, {total_med_dricks / personer:.2f} kr per person.")
    print("Välkommen åter!")


if __name__ == "__main__":
    kvittoutraknare()
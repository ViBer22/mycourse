# uppgift 2: Balder

def kontrollera_langd():
    """Frågar användaren om längd och avgör om de får åka Balder."""
    while True:
        try:
            langd = int(input("Ange din längd i cm: "))
            break  # Avsluta loopen om inmatningen är korrekt
        except ValueError:
            print("Felaktig inmatning! Ange endast siffror.")

    if langd >= 130:
        print("✅ Du får åka Balder!")
    else:
        print("❌ Du får inte åka Balder.")

kontrollera_langd()

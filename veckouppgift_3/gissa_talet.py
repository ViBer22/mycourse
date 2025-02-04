# uppgift : gissa talet

import random

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")
secret = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input("Gissa: "))
    guess_count += 1

    if guess == secret:
        print(f"Det är rätt!! Du gjorde det på {guess_count} gissningar.")
        break
    else:
        # Determine if guess is too high or low
        if guess < secret:
            message = "Nej, det är för lågt!"
        else:
            message = "Nej, det är för högt!"

        # Check proximity
        if abs(guess - secret) <= 5:
            message += " Nu börjar det brännas!"

        print(message)
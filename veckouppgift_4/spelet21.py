# uppgift : spelet 21

import random

def sum_exceeds_21():
    total = 0
    num = 0
    while total <= 21:
        num += 1
        total += num
    print(f"Första talet som gör summan större än 21 är: {num}")


def random_sum_exceeds_21():
    total = 0
    while total <= 21:
        card = random.randint(1, 13)
        total += card
    print(f"Första slumpade talet som gör summan större än 21 är: {card}")


def play_game():
    player_total = 0
    computer_total = 0

    print("Välkommen till 21-spelet!")

    while True:
        choice = input("Vill du ta ett nytt kort? (ja/nej): ")
        if choice.lower() == "ja":
            card = random.randint(1, 13)
            player_total += card
            print(f"Du drog {card}, din totala summa är nu {player_total}")
            if player_total > 21:
                print("Du förlorade! Din summa översteg 21.")
                return
        else:
            break

    while computer_total < 17:
        card = random.randint(1, 13)
        computer_total += card

    print(f"Datorns totala summa är {computer_total}")

    if computer_total > 21 or player_total > computer_total:
        print("Grattis, du vann!")
        return 1
    elif player_total == computer_total:
        print("Oavgjort!")
        return 0.5
    else:
        print("Datorn vann!")
        return 0


# Testa funktionerna
sum_exceeds_21()
random_sum_exceeds_21()

total_wins = 0
total_games = 3

for i in range(total_games):
    print(f"\n--- Spel {i + 1} ---")
    total_wins += play_game() or 0

print(f"\nDu vann totalt {total_wins} av {total_games} spel!")


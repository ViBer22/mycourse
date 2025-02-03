# uppgift 1: skapa projekt och synka med GitHub

name = "Viktoria"
print(f"This program was made by {name}")


# uppgift 1: diskutera i gruppen med förbättringar

ticket_price = 100
pocket_money = 200
change = pocket_money - ticket_price
print(f"Det blir {change} kronor över.")

discount = 200 - 100 / 2
print(f"Hälften är: {discount}")


#uppgift 3: använda variabler och datatyper.

# 1a. Använd input för att be användaren om ett heltal:

tal1 = int(input("Ange ett heltal: "))
print(f"Du angav: {tal1}")

# 1b. Fråga användaren efter ett annat heltal och skriv ut summan:

tal2 = int(input("Ange ett till heltal: "))
summa = tal1 + tal2
print(f"Summan av {tal1} och {tal2} är {summa}")

# 2a. Räkna ut rabatten på jackan:

jacka_pris = 2000
rea_procent = 50
slut_pris = jacka_pris * (1 - rea_procent / 100)
print(f"Jackan kostar {slut_pris} kr efter rea.")

# 2b. Gör om programmet så att användaren kan skriva in en procentsats:

jacka_pris = 2000
rea_procent = float(input("Ange rea i procent: "))
slut_pris = jacka_pris * (1 - rea_procent / 100)
print(f"Jackan kostar {slut_pris} kr efter {rea_procent}% rea.")

# uppgift 4: Fler övningar

# 1a. Beräkna tiden för resan mellan Stockholm och Göteborg:

distance = 470  # km
speed = float(input("Ange hastighet i km/h: "))
time_hours = distance / speed
print(f"Det tar {time_hours:.2f} timmar att köra från Stockholm till Göteborg.")

# 1b. Svara i minuter istället för timmar:

time_minutes = time_hours * 60
print(f"Det tar {time_minutes:.2f} minuter att köra från Stockholm till Göteborg.")

# 1c. Svara i hela timmar och minuter:

hours = int(time_hours)
minutes = int((time_hours - hours) * 60)
print(f"Det tar {hours} timmar och {minutes} minuter att köra från Stockholm till Göteborg.")

# 2. Beräkna längden på hypotenusan:

import math

side1 = float(input("Ange längden på den första sidan: "))
side2 = float(input("Ange längden på den andra sidan: "))
hypotenuse = math.sqrt(side1**2 + side2**2)
print(f"Längden på hypotenusan är {hypotenuse:.2f}.")

# 3a. Skriv ut dagens datum:

from datetime import date

today = date.today()
print(f"Dagens datum är: {today}")

# 3b. Skriv ut datumet om 7 dagar:

from datetime import timedelta

future_date = today + timedelta(days=7)
print(f"Om 7 dagar är det: {future_date}")


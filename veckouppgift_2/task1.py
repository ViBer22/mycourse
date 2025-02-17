# uppgift 1: Diskutera i grupp

is_member = False
level1 =100
level2 = 300
discount =0

price =input ("Välkomen, köp något dyrt:")
price = float(price)
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabbat.")
    discount = discount +10
if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabbat.")
    discount = +25

final_price = price*(100-discount)/100
print("Efter rabbater blir priset…" +final_price)

'''
 Code Review

Syftet med koden
Syftet verkar vara att ge rabatt baserat på köpesumman.
Om en kund handlar för mer än 100 får de 10% rabatt (nivå 1), och om de handlar för minst 300 får de 25% rabatt (nivå 2).
Det slutliga priset beräknas genom att subtrahera rabatten från det ursprungliga priset.
'''

level_1 = 100
level_2 = 300

is_member = False
member_discount = 5 if is_member else 0

try:
    price = float(input("Välkommen! Ange priset på varan: "))
    if price < 0:
        print("Priset kan inte vara negativt!")
        exit()
except ValueError:
    print("Felaktig inmatning! Ange ett nummer.")
    exit()

if price >= level_2:
    discount = 25
elif price > level_1:
    discount = 10
else:
    discount = 0

total_discount = discount + member_discount

final_price = round(price * (100 - total_discount) / 100, 2)

if discount > 0:
    print(f"Grattis! Du har fått {discount}% rabatt.")
if is_member:
    print(f"Som medlem får du ytterligare {member_discount}% rabatt!")

print(f"Efter rabatter blir priset: {final_price} kr")

'''
Förbättringar :
fixat rabattlogiken - kunden får endast den högsta rabatten, ingen stapling
lagt till medlemsrabatt - extra 5% rabatt för medlemmar om is_member = True
felhantering för inmatning - programmet kraschar inte om användaren matar in fel värde
rundar priset till två decimaler -  snyggare utskrift
'''
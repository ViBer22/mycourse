# uppgift: miniräknare

# 1. Fråga efter tre tal
t1 = float(input("Ange tal 1: "))
t2 = float(input("Ange tal 2: "))
t3 = float(input("Ange tal 3: "))

# 2. Beräkna summan och skriv ut
summa = t1 + t2 + t3
print(f"Summan är: {summa}")

# 3. Hitta det största talet
if t1 >= t2 and t1 >= t3:
    print(f"Störst tal är: {t1}")
elif t2 >= t1 and t2 >= t3:
    print(f"Störst tal är: {t2}")
else:
    print(f"Störst tal är: {t3}")

# 4. Kontrollera om två tal är lika eller alla tre lika
if t1 == t2 == t3:
    print("Alla tre tal är lika.")
elif t1 == t2 or t1 == t3 or t2 == t3:
    print("Två tal är lika.")
else:
    print("Inga tal är lika.")

# 5. Hitta det mellersta talet
if t1 == t2 == t3 or t1 == t2 or t2 == t3 or t1 == t3:
    print("Inget mellersta tal.")
else:
    sorted_tal = sorted([t1, t2, t3])
    print(f"Det mellersta talet är: {sorted_tal[1]}")

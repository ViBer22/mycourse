# uppgift: Öva på loppar och listor

# 1a
answer = 0
for i in range(1, 11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

# 1b
sum_1_to_100 = sum(range(1, 101))
print("Summan av talen 1 till 100 är: " + str(sum_1_to_100))

# 1c
sum_while = 0
num = 1
while num <= 100:
    sum_while += num
    num += 1
print("Summan av talen 1 till 100 med while-loop är: " + str(sum_while))

# 2
num_list = [1, -2, 3, -2, 4, -3]
sum_list = sum(num_list)
print("Summan av listans element är: " + str(sum_list))

# 3a
movies = ["Nyckeln till frihet", "Den gröna milen", "Tillbaka till framtiden", "Coco"]
print(movies)

# 3b
movies.append("Fellowship of the ring")
print(movies)

# 3c
movies.insert(0, "The two towers")
print(movies)

# 3d
fellowship_index = movies.index("Fellowship of the ring")
print("Fellowship of the ring har index: " + str(fellowship_index))

# 3e
movies.remove("Tillbaka till framtiden")
fellowship_index_after = movies.index("Fellowship of the ring")
print("Efter borttagning har Fellowship index: " + str(fellowship_index_after))

# 3f
print("Längden på listan är: " + str(len(movies)))

# 3g
movies.reverse()
print("Listan baklänges:", movies)

# 3h
movies.sort()
print("Listan i bokstavsordning:", movies)



# uppgift : to do list (att göra-lista)

print("** Enkel Todo-lista **")
todo_list = []

while True:
    print("\n1. Visa lista")
    print("2. Lägg till uppgift")
    print("3. Ta bort uppgift")
    print("4. Avsluta")

    val = input("Välj meny: ")

    if val == '1':
        if not todo_list:
            print("Listan är tom")
        else:
            print("Din att-göra-lista:")
            for nr, uppgift in enumerate(todo_list, 1):
                print(f"{nr}. {uppgift}")

    elif val == '2':
        ny = input("Skriv ny uppgift: ")
        todo_list.append(ny)
        print(f"La till '{ny}'")

    elif val == '3':
        if not todo_list:
            print("Listan är redan tom")
        else:
            print("Vilken uppgift vill du ta bort?")
            for nr, uppgift in enumerate(todo_list, 1):
                print(f"{nr}. {uppgift}")

            try:
                bort = int(input("Nummer: ")) - 1
                if 0 <= bort < len(todo_list):
                    removed = todo_list.pop(bort)
                    print(f"Tog bort '{removed}'")
                else:
                    print("Ogiltigt nummer")
            except:
                print("Måste vara ett nummer")

    elif val == '4':
        print("Hejdå!")
        break

    else:
        print("Ogiltigt val, försök igen")
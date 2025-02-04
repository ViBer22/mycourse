# uppgift: figurer med loopar

figures = ["a","b","c","d"]

for figure in figures:
    print("**************************")

    if figure == "a":
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if x == 1:
                    s += "#"
                else:
                    s += "."
            print(s)

    if figure == "b":
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if x == y:
                    s += "#"
                else:
                    s += "."
            print(s)

    if figure =="c":
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if 3 <= x <= 5:
                    s += "#"
                else:
                    s += "."
            print(s)

    if figure =="d":
        for y in range(1, 7):
            s = ""
            if y == 3:
                s = "#" * 8
            else:
                s = "..#....."
            print(s)
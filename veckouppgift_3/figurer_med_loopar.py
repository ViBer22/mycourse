# uppgift: figurer med loopar

figures = ["a","b","c","d","e"]

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

    if figure == "d":
        for y in range(1, 7):
            s = ""
            if y == 3:
                s = "#" * 8
            else:
                s = "..#....."
            print(s)
    if figure == "e":
        for y in range(6):
            s = ""
            for x in range(8):
                if (y == 0 and x in [4, 5]) or \
                        (y == 1 and x == 4) or \
                        (y == 2 and x in [3, 4]) or \
                        (y == 3 and x in [2, 4]) or \
                        (y == 4 and x in [1, 4]) or \
                        (y == 5 and x in [0, 4]):
                    s += "#"  #
                else:
                    s += "."
            print(s)


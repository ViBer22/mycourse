# functions.py

def my_function(name):
    print(f"{name} är en riktig testautomatiserare")

def eko(text, count=2):
    print(text * count)

def loop_example():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
    print(y)

def last(lst):
    return lst[-1] if lst else None

def cut_edges(lst):
    return lst[1:-1] if len(lst) > 2 else []

def increase(x):
    x += 1
    return x

def average(x, y):
    return (x + y) / 2

def pretty_print(lst):
    if not lst:
        print("Listan är tom.")
    else:
        print(f"Listan har {len(lst)} element:")
        for i, item in enumerate(lst, start=1):
            print(f"{i}. {item}")



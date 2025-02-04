# uppgift : temperaturomvandling

def convert_temperature(value, unit):
    if unit == 'C':
        converted = 1.8 * value + 32
        print(f"Det blir {converted:.1f} grader Fahrenheit.")
    else:
        converted = (value - 32) / 1.8
        print(f"Det blir {converted:.1f} grader Celsius.")

    if converted < 10:
        print("Ta på dig vinterkläder!")
    elif converted >= 20:
        print("Packa badkläder!")


def main():
    unit = input("Skriv 'C' för Celsius eller 'F' för Fahrenheit: ").strip().upper()
    if unit in ['C', 'F']:
        value = float(input(f"Skriv in en temperatur i grader {unit}: "))
        convert_temperature(value, unit)
    else:
        print("Felaktig inmatning. Vänligen ange 'C' eller 'F'.")


if __name__ == "__main__":
    main()

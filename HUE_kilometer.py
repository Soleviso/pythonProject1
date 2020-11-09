user_name = input("Vorname: ")
print("Hallo " + user_name + ", Willkommen bei unserem Converter von Kilometer in Meilen!")

while True:
    num1 = input('Kilometer: ')
    ans = float(num1) / 1.6
    print(ans)

    choice = input("Möchtest du eine weitere Umrechnung machen? (j/n): ")

    if choice.lower() != "j" and choice.lower() != "ja":
        break


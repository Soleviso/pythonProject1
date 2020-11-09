user_name = input("Vorname: ")

mood = input("Hallo " + user_name + ", wie geht's dir heute? ")

if mood == "gut drauf":
    print("wunderbar, weiter so!")
elif mood == "mittel":
    print("Das wird heute noch besser!")
elif mood == "nicht gut":
    print("Kopf hoch, du schaffst das!")
else:
    print("Die Stimmung kenn ich nicht, aber du schaffst den Tag!")
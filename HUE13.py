import json

class Tier():
   def __init__(self, tierart,rufname, farbe, alter, gewicht):
       self.tierart = tierart
       self.rufname = rufname
       self.farbe = farbe
       self.alter = alter
       self.gewicht = gewicht

Ferdy = Tier ("Katze", "Ferdy", "rot", 9, 6.5)
Nera = Tier ("Hund", "Nera", "schwarz", 6, 14)

user_tierart = input("Tierart: ")
user_rufname = input("Rufname: ")
user_farbe = input("Fellfarbe: ")
user_alter = input("Alter: ")
user_gewicht = input("Gewicht: ")

print("Das sind unsere beliebtesten Haustiere!")
user_tierart = input("Tierart: ")
user_rufname = input("Rufname: ")
user_farbe = input("Fellfarbe: ")
user_alter = input("Alter: ")
user_gewicht = input("Gewicht: ")

with open("haustier.txt", "r") as haustier_file:
    haustier_list = json.loads(haustier_file.read())
    print("Unsere beliebtesten Tiere: " + str(haustier_list))

user_haustier = Tier(tierart=user_tierart, rufname=user_rufname, farbe=user_farbe, alter=user_alter,
                            gewicht=user_gewicht)

for haustier_dict in haustier_file:
    print(str(haustier_dict["user_tierart"]) + " Tierart, Name: " + haustier_dict.get("user_rufname") + " Farbe: " +haustier_dict["user_farbe"])

print("Dein Haustier ist in unser best-of Liste!")
print("Haustier Liste: {0}".format(user_haustier.__dict__))




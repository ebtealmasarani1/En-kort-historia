hero_name = input("Vem ska historien handla om? ")
hero_age = int(input("Hur gammal är hen? "))
place = input("Vilken plats börjar resan på? ")
item = input("Vilket föremål tar hjälten ha med sig? ")
gold = int(input("Hur många guldmyntar har hjälten? "))

print()
print("Det här är historien om", hero_name + ".")
print(hero_name, "är", hero_age, "år gammal och börjar sin resa i", place + ".")
print(hero_name, "har med sig",item, "och", gold, "guldmynt.")

print()
hero_age = hero_age + 10
print ("Tio år senare är ", hero_name, hero_age, "år gammal. ")

print()

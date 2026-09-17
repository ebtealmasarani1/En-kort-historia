hero_name = input("Vem ska historien handla om? ")
hero_age = int(input("Hur gammal är hen? "))
place = input("Vilken plats börjar resan på? ")
item = input("Vilket föremål tar hjälten ha med sig? ")
gold = int(input("Hur många guldmyntar har hjälten? "))

print()
print()
print("Det här är historien om", hero_name + ".")
print(hero_name, "är", hero_age, "år gammal och börjar sin resa i", place + ".")
print(hero_name, "har med sig",item, "och", gold, "guldmynt.")


print()
hero_age = hero_age + 3
print ("Tre år senare är ", hero_name, hero_age, "år gammal. ")


print()
choice = input("Framför hjälten finns en mystisk dörr, ska hjälten öppna den? (Ja eller Nej) ")

if choice == "Ja":
    print(hero_name, "öppnar försiktig dörren. ")
    print("Där inne hittadde hjälten 10 guldmyntar")
    gold = gold + 10
else:
    print(hero_name, "bestämmer sig för att gå vidare. ")

print("Hjälten har nu", gold, "guldmyntar")


print()
if gold >= 15:
    choice = input("En svärdhandlare har ett magisk svärd. Vill du köpa det för 10 guldmyntar? (ja/nej) ")

    if choice == "ja":
        print(hero_name, "köper det magiska svärdet.")
        gold = gold - 10
    else:
        print(hero_name, "köper inte svärdet.")

else:
    print("Hjälten har inte tillräckligt med guld för svärdet.")

print("Hjälten har", gold, "guldmyntar kvar.")


print()
choice = input("Hjälten kommer fram till en korsning. Ska hen gå vänster eller höger? (vänster/höger)")

if choice == "vänster":
    print(hero_name, "väljer den mörka vägen.")
    gold = gold + 5
else:
    print(hero_name, "väljer den ljusa vägen.")
    gold = gold + 2

print("Efter vägen har hjälten", gold, "guldmynt.")


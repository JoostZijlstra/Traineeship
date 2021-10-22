from random import choice, randint

# Welkomsttekst
print("Henry de kat verstopt zich en houdt de verhuizing op. Vind hem, zodat je verder kan gaan met de verhuizing.")

# Initialisatie
aantal_dozen = 5
doos_met_kat = randint(1, aantal_dozen)
ronde_nummer = 0
kat_gevonden = False


# De functie die kijkt of de speler de juiste doos kiest of niet. Bij juiste doos return: -1, anders nieuwe positie kat.
def open_doos(poging, doos_met_kat, aantal_dozen):
    if poging == doos_met_kat:
        return -1
    
    elif doos_met_kat ==1:
        doos_met_kat += 1
        return doos_met_kat

    elif doos_met_kat == aantal_dozen:
        doos_met_kat -=1
        return doos_met_kat

    else:
        verplaatsing = int(choice([-1,1]))
        doos_met_kat += verplaatsing
        return doos_met_kat


# Stel ja-nee vraag aan participant (gestolen van raad_een_dier)
def niet_nogmaals(vraag):
    antwoord = input(vraag + ' ')
    return is_nee(antwoord)

def is_nee(tekst):
    if tekst.lower().startswith('n'):
        return True
    else:
        return False



# Herhaal het spel totdat de speler de kat heeft gevonden of de speler wil stoppen met raden.
while not kat_gevonden:
    ronde_nummer += 1
    print("Ronde", 
        ronde_nummer,
        ": in welke doos zit Henry de kat? Kies uit nummers 1 t/m 5.")

    poging = int(input())

    doos_met_kat = open_doos(poging, doos_met_kat, aantal_dozen)

    if doos_met_kat == -1: # -1 is de waarde van een succesvolle poging
        kat_gevonden == True
        print("Gefeliciteerd! Gelukkig zat er geen gifgas in de verhuisdozen en is Henry ongedeerd.")
        break
    else:
        print("Henry zat hier niet en heeft zich verplaatst.")
    
    
    if niet_nogmaals('Nogmaals proberen? (ja/nee?))'):
        break


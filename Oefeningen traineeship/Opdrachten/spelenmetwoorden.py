# Spelen met woorden

bestand_met_woorden = open("woorden.txt", "rt") # alleen-lezen van tekst
# lijst_met_woorden = bestand_met_woorden.readlines()
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

# langste_woord = ""
# for woord in lijst_met_woorden:
#   if len(woord) > len(langste_woord):
#     langste_woord = woord

# print(langste_woord)

for woord in lijst_met_woorden:
  omgekeerd_woord = woord[::-1]
  lengte_woord = len(woord)
  is_geen_afkorting = woord.islower() #checkt dat woord niet uit hoofdletters bestaat

  if woord == omgekeerd_woord and lengte_woord > 2 and is_geen_afkorting:
    print(woord, "is een palindroom.")
    
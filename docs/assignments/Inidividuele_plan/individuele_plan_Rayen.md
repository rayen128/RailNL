# Individuele Plan - Rayen

## Uiteindelijke Functionaliteit

Ik wil een plant-propagation-based algrotime gaan maken!! De bedoeling is dat ik, uiteindelijk in 1.5 weken, de complete structuur en berekingen voor dit algoritme heb staan.

Mijn idee nu is dat:

1. X-aantal hill-climbers tegelijkertijd gaan runnen om de '1ste generatie' te creëren.
2. Deze allemaal vervolgens, op basis van score, tussen 'slecht' en 'goed' worden gecategoriseerd/beoordeeld.
3. Vervolgens een berekening wordt gemaakt, op basis van stap 2, 'hoeveel' en 'hoever' de kinderen van alle states komen.
4. Deze kinderen worden vervolgens allemaal, op basis van hun ouder, gemaakt.
--> Kies de x-aantal beste en ga terug naar 2 en herhaal!

## Wat moet er nog geschreven worden

Door mij:

- Alle methodes en functionaliteiten rondom de berekeningen van 'hoever' en 'hoeveel' kinderen gemaakt gaan worden.
- Sowieso een manier om 2-dimensionale verandering (=vector) aan te geven ivm veranderingen. Ik denk erover om dit zo te doen:

  - Een methode te schrijven die 'likeness' tussen 2 states quantificeert. Dit is een manier om de 'afstand' (=hoeveel) van een state verandering te bepalen.
  - Manieren om, op basis van specifieke heuristieken, deze verandering een '(goede) richting' te geven. Mijn idee hierover is dat je een set aan methodes schrijft die (psuedo-random) een verandering in een state maken waarbij een specifieke heuristiek wordt verbeterd (bijv. eind-station worden ver uit elkaar gezet).

Door Lieke/Gert:

- Hill-Climber Algoritmes
- Methodes om states randomly te veranderen.
- Heuristieken om rekening mee te kunnen houden en richting aan verandering te geven.

## Hoe sluit het aan

Mijn code gaat totaal gebruik maken van zowel de door mij geschreven basic-algoritme class, de iteratieve (Hill Climber) algoritme class die Lieke gaat schrijven en alle heuristieken die Gert gaat schrijven. Mijn algoritme wordt namelijk een child-class van Lieke's Hill-Climber, die weer een child-class is van de basic-algoritme class waarin alle heuristieken van Gert staan. Op deze manier zal mijn onderdeel aansluiten op die van de rest.

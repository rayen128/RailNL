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

## Wat is anders uitgelopen?

Mijn algehele opzet van de PPA (beschreven in uiteindelijke functionaliteit) is precies geworden zoals bedacht. Ik heb een initial populatie van Hill-Climbers, deze worden vervolgens gecategoriseerd op basis van hun score, op basis hiervan wordt een afstand en aantal runners bepaald en op basis daarvan wordt weer een hele reeks aan kinderen gemaakt. Voor zover alles ging zoals gepland.

De precieze implementatie is echter wel een stuk anders gegaan (met ook een hoop vallen en opstaan). Vanwege het (erg) discrete-karakter van ons probleem (RailNL) heb ik het idee van een 'afstands-vector' moeten laten varen en dit anders gedaan. Het was namelijk erg moeilijk, erg obscuur en vooral ook niet zo goed werkend om het karakter/de eigenschappen van een state te 'mappen' op een 2 dimensionale manier.

Ik heb echter wel ideeën van dit idee gebruikt. Zo heb ik wel nog een 'likeness' functie die 2 states vergelijkt geschreven. Maar ipv. het originele idee kijkt deze (simpelweg) in hoeverre de routes van states, en dan specifiek de connecties in deze routes, overeen komen. 'Afstand' is dus nu ook gedefineerd als 'hoeveelheid connecties' anders. Dit is een stuk concreter, sneller en vooral makkelijk te beargumenteren.

Verder is het implementeren van de heuristieken maar tot op een zekere hoogte gelukt. Het is uiteindelijk wel gelukt om te implementeren om een limiet te stellen aan 'hoeveel heen en weer' er mag worden gegaan binnen 1 route. De resultaten hiervan gaan we (mogelijk) behandelen in de presentatie. Echter is door de tijdsplanning, voornamelijk omdat de andere experimenten en functionaliteiten langer duurden dan verwacht, het hier bij gebleven. Zowel Gert als ik zijn er niet meer aan toe gekomen om (samen) de heuristieken in de PPA te implementeren. Dit is echter wel heel jammer omdat de basis hiervoor wel al door Gert geschreven is. Maar aan de andere kant heeft het er (impliciet) ook voor gezorgd dat we iets meer gefocust te werk zijn/konden gaan.

Daarnaast heb ik wel ook nog wat extra's. Zo heb ik geïmplementeert dat er 3 manieren zijn om de initial populatie te maken (valid, random of hill-climbers). Dit stuk code leunt voornamelijk op de code van Gert en Lieke. Daarnaast heb ik ook nog 3 manieren om de generaties te filteren (na comments van Quinten). Dit kan gewoon door de beste te selecteren (best) of 2 tournament-style filters (random & sequential).

## Git-links

1. [Start PPA](https://github.com/Hachenberger02/AHRailNL/commit/20b91e9ca1d156dd7bb68a33ba448d5a9a9fe942)
2. [PDF van onderzoek toegevoegd :D](https://github.com/Hachenberger02/AHRailNL/commit/827bcae6e03737ae7a151816a6de5f3ea9cf2fd3)
3. [Start van code](https://github.com/Hachenberger02/AHRailNL/commit/f16263e5b34f73c13f39a5ef708a4c143260052e)
4. [Baby-stapjes](https://github.com/Hachenberger02/AHRailNL/commit/c6f3e46dce51b8c43d4e56814bd42d0ca0796443)
5. [PPA met rest van de code gestroomlijnt](https://github.com/Hachenberger02/AHRailNL/commit/526c31f7a5c6b361a80578b0a5becaa345d4ace0)
6. [Maar een kleine aanpassing](https://github.com/Hachenberger02/AHRailNL/commit/a6c103c13fa234fbe9050975d8b49e1cf43a4317)
7. [Start van runners maken](https://github.com/Hachenberger02/AHRailNL/commit/6a3e5161fe79e01dc3e18527eac1e7fc6a88b08d)
8. [Big steps naar 1ste versie](https://github.com/Hachenberger02/AHRailNL/commit/3f4da6cd44f7940d952844b34f3477a7b38ed72d)
9. [Hill-Climber geïmplementeerd & Code gestructureerd](https://github.com/Hachenberger02/AHRailNL/commit/bc8c4488463e8af3e9296deb8218e81b2b83f745)
10. [Debug & Experiment](https://github.com/Hachenberger02/AHRailNL/commit/e341b09b314aba3825f11e44a00f6b05cc608a13)
11. [PPA finalization](https://github.com/Hachenberger02/AHRailNL/commit/2c73c3789d33054244ad4ffacd495f80d4881512)
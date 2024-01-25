# AHRailNL
Voor Holland (Noord- en Zuid-Holland) of voor Nederland moet een lijnvoering gemaakt worden. Deze moet zo efficiënt mogelijk zijn, terwijl alle connecties tussen stations worden bereden. Hiervoor implementeren wij verschillende algoritmen, en vergelijken deze met elkaar.

## Vereisten
Om deze code te runnen zijn een aantal dingen nodig. Deze kunnen worden geïnstalleerd met pip:
```bash
pip install -r requirements.txt
```

## Gebruik
De algoritmen kunnen worden voor de case van Holland gerund door het volgende command:

```bash
python main.py holland
```
Of voor de case van Nederland met dit command:

```bash
python main.py netherlands
```

## Structuur
In dit project zijn de volgende mappen belangrijk:
- **code**: alle code van het project
    - **code/algorithms**: de algoritmen
    - **code/classes**: de classes die samen de datastructuur vormen
    - **code/visualisation**: de code die een state of resultaten kan visualiseren
- **data**: alle data in het project
    - *.geojson files*: bestanden voor visualisatie
    - *routes en stations csv files*: in te lezen data voor de case
- **docs**: alle documenten in het project
    - **docs/assignments**: documenten voor opdrachten
    - **docs/presentation**: de slides voor de eindpresentatie van het project
- **experiments**: scripts voor de uitgevoerde experimenten

## Algoritmen
De algoritmen die wij hebben geïmplementeerd, zijn:
- **Baseline algoritmen**: random algoritmen om een baseline te creëren
- **Random algoritme**: random algoritme die een valid state creëert.
- **Hill climber algoritme**: algoritme die naar een lokaal optimum in de statespace 'loopt'.
- **Plant propagation algoritme (PPA)**: algoritme die het principe van plant propagation nabootst.
- **Simulated annealing**: algoritme die het principe van annealing bij staal nabootst.

## Verdere documentatie
Verdere belangrijke documentatie:
- [definitions.md](docs/definitions.md): uitleg van de gebruikte terminologie.
- [styleguide.md](docs/styleguide.md): conventies over de layout van de code.
- [usage_state.md](docs/usage_state.md): overview van het gebruik van de datastructuur

## Future work
De volgende experimenten kunnen nog worden uitgevoerd, om het onderzoek te verbeteren:
- **Aantal iteraties hill climber**: het aantal iteraties bepalen dat het hill climber algoritme nodig heeft om een lokaal optimum te vinden.
- **Temperatuur simulated annealing**: de optimale starttemperatuur en afkoeling van het simulated annealing algoritme bepalen.
- **Implementatie van heuristieken**: onderzoeken welke combinatie van heuristieken een algoritme beter maakt
- **Vergelijkingen tussen algoritmen**: vergelijking van score, runtime en aantal iteraties tussen verschillende algoritmen, om een conclusie te kunnen trekken over het 'beste' algoritme.

## Auteurs
- Lieke Zeldenrijk
- Rayen Oaf
- Gert Hakkenberg
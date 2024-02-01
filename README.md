# AHRailNL
Voor Holland (Noord- en Zuid-Holland) of voor Nederland moet een lijnvoering gemaakt worden. Deze moet zo efficiënt mogelijk zijn, terwijl alle connecties tussen stations worden bereden. Hiervoor implementeren wij verschillende algoritmen, en vergelijken deze met elkaar.

## Vereisten
Om deze code te runnen zijn een aantal packages nodig. Deze kunnen worden geïnstalleerd met pip:

```bash
pip install -r requirements.txt
```

## Gebruik
Een voorbeeld van een algoritme kan gerund worden door het aanroepen van main.py. Hierbij is het eerste argument de case, en het tweede argument het algoritme. Vervolgens wordt, afhankelijk van het algoritme, om input gevraagd voor de configuratie van het algoritme. Het gebruik van `main.py` werkt als volgt:

```bash
python main.py [holland|netherlands] [hillclimber|hillclimber_restart|simulated_annealing|plant_propagation]
```
Hierin zijn de opties weergegeven voor ieder van de argumenten. Voor een snelle run van een algoritme kan het volgende voorbeeld genomen worden:

```bash
python main.py holland hillclimber
```

Na het runnen van het algoritme zal in de terminal de best gevonden configuratie worden weergegeven, met de score, en de uitkomst van een check50-check van het resultaat. Daarnaast zal een visualisatie daarvan worden geladen in de browser.

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
- [slides presentatie](docs/presentation/slides.html): slides voor de eindpresentatie van het project.
- [definitions.md](docs/definitions.md): uitleg van de gebruikte terminologie.
- [styleguide.md](docs/styleguide.md): conventies over de layout van de code.
- [usage_state.md](docs/usage_state.md): overview van het gebruik van de datastructuur

## Future work
De volgende experimenten kunnen nog worden uitgevoerd, om het onderzoek te verbeteren:
- **Implementatie van heuristieken**: het implementeren van meer heuristieken kan de algoritmen mogelijk verbeteren. Er kan onderzocht worden hoe deze heuristieken het best helpen om een sneller/beter resultaat te vinden.
- **Onderzoek naar parameters van plant propagation**: de parameters van het plant propagation-algoritme kunnen nog meer worden gefinetuned, om zo tot betere resultaten te komen.

## Auteurs
- Lieke Zeldenrijk
- Rayen Oaf
- Gert Hakkenberg
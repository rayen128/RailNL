# Baseline

### De Sociale Wetenschappers

## Intro

Wij hebben 3 random algoritmes geschreven. Elk van deze kiest willekeurig een startconnectie voor alle routes en plakt hier vervolgens willekeurige connecties aan vast. De verschillen tussen de 3 algoritmes zijn:

- **Algoritme 1**: Altijd 1 route. Mag oneindig lang. Stopt als alle connecties gereden zijn.
- **Algoritme 2**: (Mogelijk) oneindig veel routes. Mogen timeframe niet overschrijden. Stopt als alle connecties gereden zijn.
- **Algoritme 3**: Altijd 7 routes. Deze mogen timeframe niet overschrijden. Stopt als er 7 routes van maximale lengtes zijn.

## Results

(Afgerond op 2 decimalen)
| Algoritme | Mean | SD | Min | Max |
| ---------:|:----:|:--:|:---:|:---:|
| Algoritme 1 | 5975 | 2101.81 | -13600 | 9025 |
| Algoritme 2 | 5373.78 | 1804.37 | -12228 | 8636 |
| Algoritme 3 | 6017.65 | 928.35 | 1616 | 8463 |
| Totaal | 5788.94 | 1712.13 | -13600 | 9025 |


| Algoritme 1              | Algoritme 2 | Algoritme 3 |
| :----------------: | :------: | :----: |
| <img alt='Histogram Algoritme 1 (Holland)' src='figures_baseline_holland/scores_van_algoritme_1_holland.png' width=350>        |   <img alt='Histogram Algoritme 2 (Holland)' src='figures_baseline_holland/scores_van_algoritme_2_holland.png' width=350>   | <img alt='Histogram Algoritme 3 (Holland)' src='figures_baseline_holland/scores_van_algoritme_3_holland.png' width=350> |



Histogram totaal            |  Boxplot alle algoritmen
:-------------------------:|:-------------------------:
  <img alt='Histogram Algoritme 2 (Holland)' src='figures_baseline_holland/scores_van_alle_algoritmes_holland.png' width=350> |  <img alt='Boxplot (Holland)' src='figures_baseline_holland/boxplot_holland.png' width=350>


## Conclusies

### 'Wat is goed?'
Het gemiddelde van alle scores is ``5788.95``. Dit is een goede graadmeter voor een *MINIMALE* score. De standaarddeviatie is echter groot en de (negatieve) uitschieters zijn extreem (zie minimale scores en de boxplots). Het gemiddelde is dus maar beperkt representatief voor wat 'goed' is.

Om dit in kaart te brengen gebruiken we de scores van de daadwerkelijk correcte oplossingen. Deze zitten allemaal tussen de ``8300-8600``. Dit wordt ons streven.

<img alt='All Solved Scores' src='ranking_solved.png' width=750>

### Hoe Uniform?

De simpelste en meest voor de hand liggende conclusie is dat onze steekproef **niet** uniform is. Ten eerste heeft elk van onze algoritmes een vorm van bias doormiddel van de toegevoegde constraints. Dit maakt de steekproef dus niet *compleet* willekeurig en dus niet compleet uniform/representatief.

Dat hebben we echter geprobeerd te compenseren door 3 verschillende algoritmes toe te passen. Deze zijn net op een andere manier willekeurig. Daardoor brengen we een groter gedeelte van de state space in kaart.

<u>Conclusie</u>: Onze huidige steekproef is niet volledig uniform en beschrijft dus niet de complete state space. Aangezien een volledig uniforme steekproef niet haalbaar is en wij wel maatregelen hebben genomen om deze steekproef uniformer te maken, is dit in onze ogen geen probleem. Met andere woorden: de steekproef is niet compleet, maar wel voldoende representatief.
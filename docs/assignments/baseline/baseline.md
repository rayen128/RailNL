# Baseline

### De Sociale Wetenschappers

## Intro

Wij hebben 3 random algoritmes geschreven. Elk van deze kiest willekeurig een start-connectie voor alle routes en plakt hier vervolgens willekeurige connecties aan. De verschillen tussen de 3 algoritmes zijn:

- **Algoritme 1**:  Altijd 1 route. Mag oneindig lang. Stopt als alle connecties gereden zijn.
- **Algoritme 2**: (kan) Oneindig veel routes. Mogen time-frame niet overschrijden. Stopt als alle connecties gereden zijn.
- **Algoritme 3**: Altijd 7 routes. Deze mogen time-frame niet overschrijden. Stopt als 7 routes van maximale lengtes bestaan.

## Results

--> Afgerond op 2 decimalen

- **Algoritme 1**
    - *Mean*= 5975
    - *Standard Deviation*= 2101.81
    - *Min score*= -13600
    - *Max score*= 9025

<img alt='Histogram Algoritme 1 (Holland)' scr='/figures_baseline_holland/scores_van_algoritme_1_holland.png'>

- **Algoritme 2**
    - *Mean*= 5373.78
    - *Standard Deviation*= 1804.368479607147
    - *Min score*= -12228
    - *Max score*= 8636

![Histogram Algoritme 2 (Holland)](/AHRailNL/docs/assignments/baseline/figures_baseline_holland/Scores%20van%20algoritme%202%20Holland.png)

- **Algoritme 3**
    - *Mean*= 6017.65
    - *Standard Deviation*= 928.35
    - *Min score*= 1616
    - *Max score*= 8463

![Histogram Algoritme 3 (Holland)](/AHRailNL/docs/assignments/baseline/figures_baseline_holland/Scores%20van%20algoritme%203%20Holland.png)

- **Totaal**
    - *Mean*= 5788.94
    - *Standard Deviation*= 1712.13
    - *Min score*= -13600
    - *Max score*= 9025

![Histogram alle Algoritmes  (Holland)](/AHRailNL/docs/assignments/baseline/figures_baseline_holland/Scores%20van%20alle%20algoritmes%20Holland.png)

![Boxplot alle Algoritmes (Holland)](/AHRailNL/docs/assignments/baseline/figures_baseline_holland/Boxplot.png)

## Hoe Uniform is onze sample?
Punten te benoemen:
-	We hebben bias (doormiddel van wel/niet toegevoegde constraints) dus niet compleet uniform.

-	Hebben 3 verschillende algoritmes, die elk net anders random zijn, om dit te compenseren. Dit zal iets compenseren, maar zeker niet compleet.

-	Daarnaast hebben we een (relatief) gelimiteerde hoeveelheid (30.000) verschillende states gerund. De 30.000 is (echt enorm) veel kleiner dan onze berekende state-space. 

-	Conclusie: Het is niet compleet uniform, dit is denken wij niet realistisch en ook niet persé nodig. Echter is het hopelijk wel een beetje representabel door de measures die wij genomen hebben.


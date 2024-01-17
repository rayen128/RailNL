# Baseline

### De Sociale Wetenschappers

## Intro

Wij hebben 3 random algoritmes geschreven. Elk van deze kiest willekeurig een start-connectie voor alle routes en plakt hier vervolgens willekeurige connecties aan. De verschillen tussen de 3 algoritmes zijn:

- **Algoritme 1**:  Altijd 1 route. Mag oneindig lang. Stopt als alle connecties gereden zijn.
- **Algoritme 2**: (kan) Oneindig veel routes. Mogen time-frame niet overschrijden. Stopt als alle connecties gereden zijn.
- **Algoritme 3**: Altijd 7 routes. Deze mogen time-frame niet overschrijden. Stopt als 7 routes van maximale lengtes bestaan.

## Results

(Afgerond op 2 decimalen)

| Alg 1              | Alg 2 | Alg 3 |
| :---------------- | :------: | ----: |
| <img alt='Histogram Algoritme 1 (Holland)' src='figures_baseline_holland/scores_van_algoritme_1_holland.png' width=350>        |   <img alt='Histogram Algoritme 2 (Holland)' src='figures_baseline_holland/scores_van_algoritme_2_holland.png' width=350>   | <img alt='Histogram Algoritme 3 (Holland)' src='figures_baseline_holland/scores_van_algoritme_3_holland.png' width=350> |

- **Algoritme 1**
    - *Mean*= ``5975``
    - *Standard Deviation*= ``2101.81``
    - *Min score*= ``-13600``
    - *Max score*= ``9025``

- **Algoritme 2**
    - *Mean*= ``5373.78``
    - *Standard Deviation*= ``1804.37``
    - *Min score*= ``-12228``
    - *Max score*= ``8636``

- **Algoritme 3**
    - *Mean*= ``6017.65``
    - *Standard Deviation*= ``928.35``
    - *Min score*= ``1616``
    - *Max score*= ``8463``

- **Totaal**
    - *Mean*= ``5788.94``
    - *Standard Deviation*= ``1712.13``
    - *Min score*= `-13600`
    - *Max score*= ``9025``

Histogram             |  Boxplot
:-------------------------:|:-------------------------:
  <img alt='Histogram Algoritme 2 (Holland)' src='figures_baseline_holland/scores_van_alle_algoritmes_holland.png' width=350> |  <img alt='Boxplot (Holland)' src='figures_baseline_holland/boxplot_holland.png' width=350>


## Conclusies

### 'Wat is goed'?

Het gemiddelde van totale scores is ``5788.95``. Dit is in ieder geval een goede graadmeter om te bepalen wat ons (toekomstige) algoritme *MINIMAAL* moet gaan behalen. 

### Hoe Uniform?

Punten te benoemen:
-	We hebben bias (doormiddel van wel/niet toegevoegde constraints) dus niet compleet uniform.

-	Hebben 3 verschillende algoritmes, die elk net anders random zijn, om dit te compenseren. Dit zal iets compenseren, maar zeker niet compleet.

-	Daarnaast hebben we een (relatief) gelimiteerde hoeveelheid (30.000) verschillende states gerund. De 30.000 is (echt enorm) veel kleiner dan onze berekende state-space. 

-	Conclusie: Het is niet compleet uniform, dit is denken wij niet realistisch en ook niet persé nodig. Echter is het hopelijk wel een beetje representabel door de measures die wij genomen hebben.


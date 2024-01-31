---
marp : true
theme: gaia
class: invert
paginate: true
---
<!-- _paginate: skip -->
<br>
<br>
<br>

# Sociale Wetenschappers
Lieke | Rayen | Gert

---
## Case: RailNL
- Routes maken
- Constraints
<br>

- Doel: zo efficiënt mogelijke lijnvoering

![bg right](assets/empty_state.png)

---
## Terminologie
- **Connecties**: spoorverbinding tussen twee stations
![bg right](assets/empty_state_holland.png)

---

## Terminologie
- **Connecties**
<br>

- **Route**: combinatie van connecties tussen stations

![bg right](assets/route.png)

---
## Terminologie
- **Connecties**
<br>

- **Route** 
<br>

- **State**: lijnvoering op bepaald moment

![bg right](assets/valid_state.png)

---
## Holland

#### Input

- 28 connecties
- 22 stations 
<br> 
 
#### Constraints
- Maximaal 7 routes
- Timeframe van 120 minuten

![bg right](assets/empty_state_holland.png)

---
## Nederland
#### Input

- 89 connecties
- 61 stations 
<br> 

#### Constraints
- Maximaal 20 routes
- Timeframe van 180 minuten

![bg right](assets/empty_state.png)

---
## Het probleem
- Doelfunctie
- Constraints
- Statespace

---
## Het probleem - doelfunctie
```python
K = p * 10000 - (T * 100 + Min)
```

- 10.000 als alle connecties gebruikt zijn
    - -100 voor elke route
    - -totaal aantal minuten

---
## Het probleem - constraints
- Maximum routes
- Timeframe

![bg right](assets/empty_state.png)

---
## Het probleem: statespace
- Alle mogelijke routes
- Alle mogelijke combinaties van routes
- Grote statespace
- Veel lokale optima

![bg right](assets/empty_state_holland.png)

---
<!-- _paginate: skip -->

<br>
<br>
<br>
<br>

# Algoritmen & Methoden


---

## Baseline

- Holland
  - Realistisch: ``8300-8600``
  - Maximum : ``9219``
<br>
- NL: 
  - Realistisch: ``+/- 4000``
  - Maximum: ``7549``


---

(Overzicht van alle algoritme)

---

## Heuristieken

- Aan de voorkant
  - Geïsoleerde stations
- Bij evaluatie van scores
  - Plus- en minpunten
  - Meervoudig gebruik connecties

![bg right](assets/empty_state_holland.png)

---

## LRA

- Voor het maken van een **valide state**


- Maakt nieuwe routes tot *valide state*

- Voegt connecties toe tot *timeframe* is bereikt

- Geeft voorrang aan *ongebruikte connecties*

![bg right](assets/lra_gif.gif)

---

## Hill-climber
- Maak start-state

- Maak aanpassing
    - Verwijderen connectie
    - Toevoegen connectie
    - Verwijderen route
    - Toevoegen route

- Vergelijk score


---


## Plant propagation - Overview

- Genetic Algorithm
- Hill-Climbers

![width:600 bg right](assets/PPA/strawberry_plant.png)

---
## Plant propagation - runners
- Ver en weinig vs. dichtbij en veel
- Afstand
- Richting
  - Heuristieken

---

## Resulaten


---
## Resultaten - Hill Climber

- High-scores
  - Holland: ``9200``
  - NL: ``6500``


---

## Resultaten - Hill Climber

- Heavy vs. Light  

[assets/plots_def/histo_hill_climber_netherlands_random_heavy.png]
[assets/plots_def/histo_hill_climber_netherlands_random_light.png]
--> TODO: deze op schaal 0 - 4000

---
## Resultaten - Hill Climber

- Random vs. valid

[assets/plots_def/histo_hill_climber_holland_random_heavy.png] 

[assets/plots_def/histo_hill_climber_holland_random_light.png]



---

## Resultaten - Hill Climber

- Random vs. valid
- Disclaimer: valid duurt lang bij grote state-space
 


---

## Resultaten - Simulated Annealing

- 200 beste temperatuur
- Log vs. Linear vs. Expo
 


---

## Resultaten - Simulated Annealing

- Log vs. Linear vs. Expo
 
TODO: grafiek met beste scores van de 3 coolingschemes

---

## Resultaten - Simulated Annealing

- Logaritmisch
 
TODO: line_plaatje valid 200 logaritmisch (wel/niet NL) 

---
## Resultaten - Plant Propagation

- Filters
- Parameters
- heuristiek
- valid vs. random
- verandering is niet goed

---

<!-- _paginate: skip -->
---

# Extra Info

--- 
## State Space - Formule

![width:500](assets/state_space/formule_trajecten.png)

![width:500](assets/state_space/formule_state_space.png)

--- 
## State space - deel 1

![width:500](assets/state_space/Deel_1_1.png)
![width:500](assets/state_space/deel_1_2.png)

---

## State space - deel 2
![width:500](assets/state_space/deel_2.png)

---

## Baseline - Holland
Histogram totaal            |  Boxplot alle algoritmen
:-------------------------:|:-------------------------:
  ![height:500 width:550](assets/baseline/scores_van_alle_algoritmes_holland.png) | ![height:500 width:550](assets/baseline/boxplot.png)

---

## Baseline Holland  - Results Table

![width:1000](assets/baseline/baseline_results_table.png)


---

## Baseline Holland - Algorithm Histograms
| Algoritme 1              | Algoritme 2 | Algoritme 3 |
| :----------------: | :------: | :----: |
| ![width:350](assets/baseline/scores_van_algoritme_1_holland.png) | ![width:350](assets/baseline/scores_van_algoritme_2_holland.png) | ![width:350](assets/baseline/scores_van_algoritme_3_Holland.png)

--- 
## Baseline Holland - Solved State Results

![width:1200px](assets/baseline/ranking_solved.png)

---

## Baseline NL - Histogram & Boxplot

TODO:

---


## Baseline NL - Solved States Results

TODO:

---

## PPA - Uitleg

Originale Paper            |  ChatGPT
:-------------------------:|:-------------------------:
  ![height:500 width:550](assets/PPA/PPA_paper_uitleg.png) | ![height:500 width:550](assets/PPA/ChatGPT_uitleg_PPA.png)

  ---
## PPA - Fitness Functions

![height:400 width:550](assets/PPA/tanh_graph.png)

![width:550](assets/PPA/tanh_function.png)

---
## PPA - Other Functions

![width:400](assets/PPA/fitness_function.png)

![width:400](assets/PPA/distance_function.png)

![width:400](assets/PPA/runner_function.png)

---

## UML

![width:800 bg center](assets/UML.png)

---
## Simulated Annealing - Results

TODO: opvullen

---

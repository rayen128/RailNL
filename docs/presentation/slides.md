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
  - Baseline: ``8300-8600``
  - Maximum : ``9219``
<br>
- NL: 
  - Baseline: ``+/- 4000``
  - Maximum: ``7549``


---
## Heuristieken

- Constraint: alle connecties bereden

- Valide start state
  - Voorkeur aan onbereden connecties
  - Routes maximaal gevuld


![bg right width:675](assets/plots_def/scatterplot.png)

---

## Algoritmen
- Hillclimber
- Simulated annealing
- Plant propagation
---

## Opties
- Start state: valid/random
- Verandering: light/heavy
- Specifieke parameters

---

## Hillclimber
- Maak start-state
  - Valid of random

- Maak aanpassing
    - Light of heavy

- Vergelijk score

![bg right](assets/valid_state.png)

---
## Simulated annealing
- Acceptatiekans
- Temperatuur
- Koeling schema

---


## Plant propagation - Overview

- Genetic Algorithm
- Specifieke parameters:
  - Populatie
  - Aantal runners
  - Aantal generaties

![width:600 bg right](assets/PPA/strawberry_plant.png)

---
<!-- _paginate: skip -->
<br>
<br>
<br>
<br>

# Resulaten

---
<br>
<br>
<br>
<br>

## Resultaten - Hillclimber

---
## Resultaten - Hillclimber

Random           | Valid
:-------------------------:|:-------------------------:
![width:550](assets/plots_def/histo_hill_climber_holland_random_heavy.png) | ![width:550](assets/plots_def/histo_hill_climber_holland_valid_heavy.png)
---

## Resultaten - Hillclimber 

Light           | Heavy
:-------------------------:|:-------------------------:
![width:550](assets/plots_def/histo_hill_climber_netherlands_random_light.png) | ![width:550](assets/plots_def/histo_hill_climber_netherlands_random_heavy.png)


---
## Resultaten - Hillclimber
Dus:
- Valid is beter
- Heavy is beter

---
<br>
<br>
<br>
<br>

## Resultaten - Simulated Annealing

---

## Resultaten - Simulated Annealing

- 200 beste temperatuur
 


---

## Resultaten - Simulated Annealing

- 200 beste temperatuur
- Log vs. Linear vs. Expo

![bg right width:700](assets/plots_def/comparison_annealing_holland_200.png)

---
## Resultaten - Simulated Annealing

Lineair | Exponentieel | Logaritmisch
:------------:|:------------:|:---------:
![width:373](assets/plots_def/histo_annealing_netherlands_lineair_200_random_heavy.png) | ![width:373](assets/plots_def/histo_annealing_netherlands_exponential_200_random_heavy.png) | ![width:373](assets/plots_def/histo_annealing_netherlands_logaritmic_200_random_heavy.png)

---
## Resultaten - Simulated Annealing

- Logaritmisch

![width:700 bg right](assets/plots_def//line_annealing_holland_logaritmic_100_valid_heavy.png)


---
## Resultaten - Plant Propagation

- Parameters
- Valid vs. random


![width:600 bg right](assets/PPA/strawberry_plant.png)

---

## Resultaten - Plant Propagation

- Nog geen goede resultaten
- Niet beter dan hillclimber
- Oorzaak:
  - Mutaties gaan nog niet goed

---

## Resultaten - Plant Propagation

- Gevolg: afhankelijk van lokale minima

![bg right width:700](assets/plots_def/line_netherlands_random_sequential_30_200_3_0.png)

---
## Conclusie
- Simulated annealing is het best
  - Valid start state
- Plant propagation heeft potentie

---
## Future work
- Heuristieken implementeren
- Plant propagation finetunen

![bg right](assets/empty_state.png)

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
## Simulated annealing - random vs. valid

Random            |  Valid
:-------------------------:|:-------------------------:
  ![width:550](assets/plots_def/histo_annealing_random.png) | ![width:550](assets/plots_def/histo_annealing_valid.png)

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

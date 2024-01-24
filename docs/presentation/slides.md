---
marp : true
backgroundColor: #2C365E
color: lightblue
---

# Sociale Wetenschappers
Lieke | Rayen | Gert

---
## Case: RailNL
- Routes maken
- Constraints
<br>

- Doel: zo hoog mogelijke score

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
### Het probleem
- Doelfunctie
- Constraints

---
### Het probleem: doelfunctie
```python
K = p * 10000 - (T * 100 + Min)
```

- 10.000 als alle connecties gebruikt zijn
    - -100 voor elke route
    - -totaal aantal minuten

---
### Het probleem: constraints
- Maximum routes
- Timeframe
<br>
- Alle connecties berijden

![bg right](assets/empty_state.png)

---
### Het probleem: statespace
- Alle mogelijke routes
- Alle mogelijke combinaties van routes
- Grote statespace
- Veel lokale optima

![bg right](assets/empty_state_holland.png)

---
## Methoden

---

### Baseline

- 3 random algoritmes

- Relaxed constraints:
  - Algoritme 1 - **Tijdsframe p/route**
  - Algoritme 2 - **Hoeveelheid routes**
  - Algoritme 3 - **Alle connecties**

---

Histogram totaal            |  Boxplot alle algoritmen
:-------------------------:|:-------------------------:
  ![height:500 width:550](assets/baseline/scores_van_alle_algoritmes_holland.png) | ![height:500 width:550](assets/baseline/boxplot.png)

---
### Baseline

- ``20`` daadwerkelijke solved states

- Scores liggen tussen ``8300-8600``

- Dit is ons streven

---

### LRA

- Voor het maken van een **valide state**


- Maakt nieuwe routes tot *valide state*

- Voegt connecties toe tot *timeframe* is bereikt

- Geeft voorrang aan *ongebruikte connecties*

![bg right](assets/lra_gif.gif)

---

### Hill-climber
- Maak start-state

- Maak aanpassing
    - Verwijderen connectie
    - Toevoegen connectie
    - Verwijderen route
    - Toevoegen route

- Vergelijk score


---
### Heuristieken

- Aan de voorkant
  - Geïsoleerde stations
- Bij de evaluatie
  - Plus- en minpunten
  - Meervoudig gebruik connecties

![bg right](assets/empty_state_holland.png)

---

### Plant propagation - Overview

- Genetic Algorithm
- Hill-Climbers

---
### Plant propagation - runners
- Ver en weinig vs. dichtbij en veel
- Afstand
- Richting
  - Heuristieken
---

---
# Extra Info

--- 
### State Space - Formule

![width:500](assets/state_space/formule_trajecten.png)

![width:500](assets/state_space/formule_state_space.png)

--- 
### Baseline (extra) - Results Table

![width:1000](/AHRailNL/docs/presentation/assets/baseline/baseline_results_table.png)


---

### Baseline (extra) - Algorithm Histograms
| Algoritme 1              | Algoritme 2 | Algoritme 3 |
| :----------------: | :------: | :----: |
| ![width:350](assets/baseline/scores_van_algoritme_1_holland.png) | ![width:350](assets/baseline/scores_van_algoritme_2_holland.png) | ![width:350](assets/baseline/scores_van_algoritme_3_Holland.png)

--- 
### Baseline (extra) - Solved State Results

![width:1200px](assets/baseline/ranking_solved.png)

---
### PPA - Uitleg

Originale Paper            |  ChatGPT
:-------------------------:|:-------------------------:
  ![height:500 width:550](assets/PPA/PPA_paper_uitleg.png) | ![height:500 width:550](assets/PPA/ChatGPT_uitleg_PPA.png)

  ---
### PPA - Fitness Functions

![height:400 width:550](assets/PPA/tanh_graph.png)

![width:550](assets/PPA/tanh_function.png)

---
### PPA - Other Functions

![width:400](assets/PPA/fitness_function.png)

![width:400](assets/PPA/distance_function.png)

![width:400](assets/PPA/runner_function.png)
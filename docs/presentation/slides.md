---
marp : true
theme: gaia
class: invert
---

# Sociale Wetenschappers
Lieke | Rayen | Gert

---
## Case: RailNL
- Routes maken
- Alle connecties gebruiken
- Timeframe
- Maximum routes

-plaatje van lege visualisatie?-

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
- Alle connecties berijden
- Maximum routes
- Timeframe

-plaatje?-

---
### Het probleem: statespace
- Alle mogelijke routes
- Alle mogelijke combinaties van routes
- Grote statespace
- Veel lokale optima

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

- Dit is onze **baseline**!

---

### Heuristieken
- Geïsoleerde stations
    - Stations met 1 ongebruikte connectie
- Aantal keer heen en weer
    - Variabel
- Herhaling gebruik connecties
    - Minpunten voor meer dan één keer

---

### Hill-climber

---

### Plant propagation - Overview

- Genetic Algorithm
- Hill-Climbers

---
### Plant propagation - Fitness

- Doel-functie
- Map to ``(0,1)``

---

### Plant propagation - Runners

- Veel kindjes
- Exploration vs. Exploitation
- Het concept *Distance*

---
### Plant propagation - And repeat!!

- Filter de beste oplossingen
- Maak hier weer kindjes voor
- Etc.

---
# Extra Info

--- 
### State Space - Formule

![width:500](/AHRailNL/docs/presentation/assets/state_space/formule_trajecten.png)

![width:500](/AHRailNL/docs/presentation/assets/state_space/formule_state_space.png)

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
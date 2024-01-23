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

## Het probleem
- Doelfunctie
- Constraints

---

### Waar zit de uitdaging?
- Statespace
- Veel combinaties
- Veel lokale optima
- Kwantificeren

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
  ![height:500 width:550](/AHRailNL/docs/presentation/assets/baseline/scores_van_alle_algoritmes_holland.png) | ![height:500 width:550](/AHRailNL/docs/presentation/assets/baseline/boxplot.png)

---
### Baseline

- ``20`` daadwerkelijke solved states

- Scores liggen tussen ``8300-8600``

- Dit is onze **baseline**!

---

### Heuristieken
- Aantal keer heen en weer
- Herhaling gebruik connecties
- ...

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
| ![width:350](/AHRailNL/docs/presentation/assets/baseline/scores_van_algoritme_1_holland.png) | ![width:350](/AHRailNL/docs/presentation/assets/baseline/scores_van_algoritme_2_holland.png) | ![width:350](/AHRailNL/docs/presentation/assets/baseline/scores_van_algoritme_3_Holland.png)

--- 
### Baseline (extra) - Solved State Results

![width:1200px](/AHRailNL/docs/presentation/assets/baseline/ranking_solved.png)

---
### PPA - Uitleg

Originale Paper            |  ChatGPT
:-------------------------:|:-------------------------:
  ![height:500 width:550](/AHRailNL/docs/presentation/assets/PPA/PPA_paper_uitleg.png) | ![height:500 width:550](/AHRailNL/docs/presentation/assets/PPA/ChatGPT_uitleg_PPA.png)

  ---
### PPA - Fitness Functions

![height:400 width:550](/AHRailNL/docs/presentation/assets/PPA/tanh_graph.png)

![width:550](/AHRailNL/docs/presentation/assets/PPA/tanh_function.png)

---
### PPA - Other Functions

![width:400](/AHRailNL/docs/presentation/assets/PPA/fitness_function.png)

![width:400](/AHRailNL/docs/presentation/assets/PPA/distance_function.png)

![width:400](/AHRailNL/docs/presentation/assets/PPA/runner_function.png)
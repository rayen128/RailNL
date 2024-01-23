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
-Histogram erbij poepen-

---

### Grafiekjes


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

### Plant propagation



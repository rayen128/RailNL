# Results

## Slides

### Hill_climber

#### Holland:
    - In principe behalen ongeveer de top score -> hill_climber_holland.pgn (= max_scores)

    - Alleen we zien dat dit veel consistenter gebeurt bij de valid states
    --> dit komt omdat de greedy-heid van valid state zich heel goed leent voor Holland

#### Netherlands:
    - Random heel erg slecht, tekortkomingen van random_start duidelijk
    - Valid hele hoge score, maar duurt super


### Simulated Annealing:
    - Heavy is altijd beter (ook bij de andere shizzle)    

#### Holland:
    - Valid werkt nogsteeds beter dan random, maar dit verschil is echt een stuk minder
    - Random heeft veel minder spreiding, waarschijnlijk omdat het nu uit de lokale minima komt

    - best linear: 200, heavy, valid
    - best exponentieel: 200, heavy, valid  
    - best logaritmisch: 100/200 valid 
    --> heavy minder consistent, maar ook een paar hele hoge uitschieters

#### Netherlands:
    -  zelfde beste linear: 200, heavy (random?)
    --> wel een 'lelijkere' vorm
    - best expontentieel: 100, heavy (random?)
    - logarithmisch: 100/200, heavy 
    --> wel een stuk minder stabiel

### PPA:
    - 

### Conclusie
    - Wij 'brute-forcen' een beetje, dit is te zien aan hoe we bij holland (kleine state-space) hele hoge scores krijgen t.o.v. NL
    - Als wij heuristieken toepassen in onze situatie, dan werkt dit het beste. (greedyness, all connections)
    --> Onderbouw dit goed 

    - Beste score: 
    - Beste algoritme 


## Extra slides:
    - hill_climber NL histogrammen
    - Valid state voor NL resultaat
    - Slechte plaatjes voor Linear-Annealing


## Computing:
    - 1u nog Hill_climber NL valid runnen
    - 1u PPA NL valid?
    - PPA voor NL


## Ideeën:
    - Baseline NL
    - theoretische max score
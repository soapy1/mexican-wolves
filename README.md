# Genetic diversity in Mexican Gray Wolves Simulation

## Wolf and Pack Setup
In this simulation, wolves will have 6 loci that can have alleles with values ranging from 1 - 5 that represent the relevant genetics of the wolf. These values are taken to match the statistics analyzed in the study "Genetic Variability in Six Mexican Gray Wolf (Canis lupusbuileyi) Populations Determined by Microsatellite Markers" [1]

## Simulation Setup
## Mating
Only the alpha male and beta female of a pack mate, so one pack will only have one litter per generation. Further, if resources are too scarce, then no mating may occur.
 The pup's alleles should have some relation to that of the parents. The size of a litter is related to the genetic variability of the parents [2,3]. This logic is encapsulated in Pack.mate(). It is assumed that all pups in the litter will live to adulthood. 
## Death
 Death may occur in expected ways such as old age, lack of food, fighing, etc. All that is implied with the life expectancy attribute of the wolf. In each time step, all wolves are aged and all the wolves who have hit their life expectancy die.

## References
[1] http://www.tandfonline.com/doi/pdf/10.1080/09712119.2007.9706647

[2] http://rspb.royalsocietypublishing.org/content/royprsb/274/1623/2365.full.pdf 

[3] http://onlinelibrary.wiley.com/doi/10.1111/j.1469-1795.2007.00116.x/full

[4] http://www.wolf.org/wolf-info/basic-wolf-info/wolf-faqs/#g

[5] http://www.biologicaldiversity.org/species/mammals/Mexican_gray_wolf/natural_history.html


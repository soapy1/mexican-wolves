from wolf import Wolf, generate_random_wolf
from random import normalvariate, randrange
from math import floor
import statistics

class Pack(object):
    def __init__(self, wolves):
        self.wolves = wolves

    def age(self):
        for w in self.wolves:
            w.age += 1

    # Only the alpha male and beta female can mate. The litter size for a
    # genetically healthy set of parents is on average 7.45 pups [2] (the
    # standard deviation is arbitarily chosen. A genetically depressed set
    # of a parents may have a litter size as small as 3.40 - 6.71  on average
    def mate(self):
        if len(self.wolves) >= 2:
            if self.average_genetic_variance() > 1.5:            
                num_pups = floor(normalvariate(7.45, 2))
            else:
                num_pups = floor(normalvariate(3.40, 2))
            self.wolves.extend(Wolf(self.determine_pup_alleles()) for i in range(0,num_pups))

    def determine_pup_alleles(self):
        self.ensure_two_mating_wolves()
        mating_wolves = [w for w in self.wolves if w.can_mate==True]
        pup_alleles = {}
        assert len(mating_wolves) == 2
        assert len(mating_wolves[0].alleles) == len(mating_wolves[1].alleles)
        for k in mating_wolves[0].alleles.keys():
            pup_alleles[k] = (mating_wolves[0].alleles[k] if \
                randrange(0,2)==0 else mating_wolves[1].alleles[k])
        return pup_alleles

    # Accounting for death by old age, lack or resources, killed by
    # other animal, etc. This is all encapsulated by the life span of
    # the wolf, that is, 6 - 8 years [5]
    def deaths(self):
        wolves_to_die = []
        for w in self.wolves:
            if w.age >= w.lifespan:
                wolves_to_die.append(w)  
        for d in wolves_to_die:
            self.wolves.remove(d)

    def ensure_two_mating_wolves(self):
        if len(self.wolves) < 2:
            return
        mating_wolves = [w for w in self.wolves if w.can_mate == True]
        non_mating_wolves = [w for w in self.wolves if w.can_mate==False]
        if len(mating_wolves) >= 3:
            for i in range(0,len(mating_wolves)-2):
                mating_wolves[i].can_mate = False
        if len(mating_wolves) == 1:
            non_mating_wolves[0].can_mate = True
        if len(mating_wolves) == 0:
            non_mating_wolves[0].can_mate = True
            non_mating_wolves[1].can_mate = True

    def histogram_of_allele_variance(self):
        alleles = self.histogram_of_allele()
        for k in alleles.keys():
            alleles[k] = statistics.pvariance(alleles[k])
        return alleles

    def histogram_of_allele(self):
        alleles = {} 
        num_wolves = len(self.wolves)
        for k in ['a','b','c','d','e','f']:
            alleles[k] = [self.wolves[i].alleles[k] for i in range(0,num_wolves)]
        return alleles


def generate_pack(num_wolves):
    wolves = [generate_random_wolf() for i in range(0,num_wolves-2)]
    wolves.extend([generate_random_wolf(True) for i in range(0,2)])
    return Pack(wolves)

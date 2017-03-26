from wolf import Wolf, generate_random_wolf
from allele import Allele
from random import normalvariate, randrange
from math import floor

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
            if self.average_genetic_variance() > 1:            
                num_pups = floor(normalvariate(7.45, 2))
            else:
                num_pups = floor(normalvariate(3.40, 2))
            self.wolves.extend(Wolf(self.determine_pup_alleles()) for i in range(0,num_pups))

    def determine_pup_alleles(self):
        mating_wolves = [w for w in self.wolves if w.can_mate==True]
        pup_alleles = []
        assert len(mating_wolves[0].alleles) == len(mating_wolves[1].alleles)
        assert len(mating_wolves) == 2
        for i in range(0,len(mating_wolves[0].alleles)):
            pup_alleles.append(mating_wolves[0].alleles[i] if \
                randrange(0,2)==0 else mating_wolves[1].alleles[i])
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
        self.ensure_two_mating_wolves()

    def ensure_two_mating_wolves(self):
        mating_wolves = [w for w in self.wolves if w.can_mate == True]
        non_mating_wolves = [w for w in self.wolves if w.can_mate==False]
        if len(mating_wolves) >= 3:
            for i in range(0,len(mating_wolves)-2):
                mating_wolves[i].can_mate = False
        if len(mating_wolves) < 1:
            non_mating_wolves[1].can_mate = True
        if len(mating_wolves) < 2:
            non_mating_wolves[0].can_mate = True

    def average_genetic_variance(self):
        num_wolves = len(self.wolves)
        return sum(self.wolves[i].genetic_variance() for i in range(0,num_wolves))/num_wolves


def generate_pack(num_wolves):
    wolves = [generate_random_wolf() for i in range(0,num_wolves-2)]
    wolves.extend([generate_random_wolf(True) for i in range(0,2)])
    return Pack(wolves)

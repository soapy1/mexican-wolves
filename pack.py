from wolf import generate_random_wolf
from random import normalvariate
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
        # TODO:
        # - The success of mating is related to inbreeding [2,3]
        # - The alleles of the pups will be related the parents
        if len(self.wolves) >= 2:
            num_pups = floor(normalvariate(7.45, 2))
            self.wolves.extend(generate_random_wolf() for i in range(0,num_pups))

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

def generate_pack(num_wolves):
    return Pack([generate_random_wolf() for i in range(0,num_wolves)])


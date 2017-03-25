from allele import Allele
from wolf import Wolf, generate_random_wolf
from random import normalvariate
from math import floor

class Pack(object):
    def __init__(self, wolves):
        self.wolves = wolves

    # Only the alpha male and beta female can mate. The litter size for a
    # genetically healthy set of parents is on average 7.5 pups [2] (the
    # standard deviation is arbitarily chosen
    def mate(self):
        # TODO:
        # - The success of mating is related to inbreeding [2,3]
        # - The alleles of the pups will be related the parents
        num_pups = floor(normalvariate(7.5, 2))
        self.wolves.extend(generate_random_wolf() for i in range(0,num_pups))

def generate_pack(num_wolves):
    return Pack([generate_random_wolf() for i in range(0,num_wolves)])


from math import pow, floor, sqrt
from random import randrange, normalvariate

class Wolf(object):
    def __init__(self, loci, can_mate=False):
        # A wolf should have 6 alleles [1]
        if len(loci) > 6:
            raise ValueError("Too many alleles specified")
        self.loci = loci
        self.age = 0
        # Average life span is 6-8 years [5]
        self.lifespan = floor(normalvariate(7, 1))
        self.can_mate = can_mate


def generate_random_wolf(can_mate=False):
    # Wolf alleles range from 1 to 5
    loci = {
        [{
            'a':randrange(1,6),
            'b':randrange(1,6),
            'c':randrange(1,6),
            'd':randrange(1,6),
            'e':randrange(1,6),
            'f':randrange(1,6)
            }
        ]
    }
    return Wolf(loci, can_mate)

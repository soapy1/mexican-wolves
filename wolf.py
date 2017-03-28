from math import pow, floor, sqrt
from random import randrange, normalvariate
import statistics

class Wolf(object):
    def __init__(self, alleles, can_mate=False):
        # A wolf should have 6 alleles [1]
        if len(alleles) > 6:
            raise ValueError("Too many alleles specified")
        self.alleles = alleles
        self.age = 0
        # Average life span is 6-8 years [5]
        self.lifespan = floor(normalvariate(7, 1)) 
        self.can_mate = can_mate

    # Note: max variance is 2
    def genetic_variance(self):
        return statistics.pvariance(self.alleles.values())


    def genetic_std_dev(self):
        return sqrt(self.genetic_variance())
 
def generate_random_wolf(can_mate=False):
    # Wolf alleles range from 1 to 5
    alleles = {'a':randrange(1,6), 'b':randrange(1,6), 'c':randrange(1,6), 'd':randrange(1,6), 'e':randrange(1,6), 'f':randrange(1,6)}
    return Wolf(alleles, can_mate)


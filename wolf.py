from math import pow, floor, sqrt
from random import randrange, normalvariate
import statistics

class Wolf(object):
    def __init__(self, alleles, can_mate=False):
        # A wolf should have 5 alleles [1]
        if len(alleles) > 5:
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
    alleles = {'a':randrange(1,5), 'b':randrange(1,5), 'c':randrange(1,5), 'd':randrange(1,5), 'e':randrange(1,5)}
    return Wolf(alleles, can_mate)

